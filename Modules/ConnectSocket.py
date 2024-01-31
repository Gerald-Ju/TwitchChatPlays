import socket
import logging
import re
import requests
import time
from Modules.ConnectInfo import ConnectInfo
from Modules.GetMessages import GetMessages
from Modules.GetInfo import GetInfo

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', 
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

class ConnectSocket:
    def checkOauth(self, response):
        pattern = r":tmi\.twitch\.tv NOTICE \* :(.*)"
        match = re.search(pattern, response)
        if match:
            auth_result = match.group(1) 
            if auth_result == "Login authentication failed":
                print(f"OAUTH Result: {auth_result}\n")
                return False
        else: 
            return True
        
    def checkChannel(self, channel_name):
        contents = requests.get('https://www.twitch.tv/' + channel_name).content.decode('utf-8')
        
        if 'isLiveBroadcast' in contents:
            return True
        else:
            return False
        
    def cleanMessage(self, response):
        # Two Regex Patterns, both work
        # pattern = r":([^!]+)!\S+@\S+ PRIVMSG #(\S+) :([\s\S]+)$"
        pattern = r":(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)"
        match = re.search(pattern, response)
        if match:
            # username = match.group(1)
            # channel = match.group(2)
            # message = match.group(3)
            # print(f"Channel: {channel} \nUsername: {username} \nMessage: {message}\n")

            message = match.group(3)
            print(f"Message: {message}\n")
            return message
        else:
            print("No Match Found")
        
    def connectToSocket(self):
        getInfo = GetInfo()
        token, channel_name, number = getInfo.menu()
        self.checkOauth(token)
        try:    
            connectInfo = ConnectInfo(token, channel_name)
            sock = socket.socket()

            sock.connect((connectInfo.getServer(), connectInfo.getPort()))
            sock.send(f"PASS {connectInfo.getToken()}\n".encode('utf-8'))
            sock.send(f"NICK {connectInfo.getNickname()}\n".encode('utf-8'))
            sock.send(f"JOIN {connectInfo.getChannel()}\n".encode('utf-8'))
        except socket.error as exc:
            print(f"Caught exception socket.error {exc}")

        else:
            if self.checkChannel(channel_name):
                auth = sock.recv(1024).decode("utf-8")
                if self.checkOauth(auth):
                    try:
                        getMessages = GetMessages()
                        print("\nValid Oauth Token\n")
                        print(f"\n{channel_name} is live.\n")
                        print("\n------------------------------\n"
                            "|   Successfully Connected   |\n"
                            "------------------------------\n")
                        while True:
                            response = sock.recv(2048).decode("utf-8")

                            if response.startswith("PING"):
                                sock.send("PONG\n".encode("utf-8"))
                            elif len(response) > 0:
                                # Uncomment to write messages to file
                                # logging.info(response)
                                message = self.cleanMessage(response)
                                getMessages.getNumMsgs(message, number)

                    except KeyboardInterrupt:
                        print("\nControl+C Detected\nExiting Now\n")
                        sock.close()
                        time.sleep(2)
                else:
                    print("\nInvalid OAUTH Token\n")
                    print("\nExiting Now\n")
                    sock.close()
                    time.sleep(2)
            else:
                print(f"\n{channel_name} is not live.\nCheck name for spelling errors.\n")
                print("\nExiting Now\n")
                sock.close()
                time.sleep(2)