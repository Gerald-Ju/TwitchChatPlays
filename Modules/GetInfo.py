import getpass

class GetInfo:
    def getToken(self):
        token = getpass.getpass("\n-----------------------\n"
                                "|   Get OAUTH Token   |\n"
                                "-----------------------\n"
                                "\n  - Go to https://twitchapps.com/tmi/ and login to Twtich if you don't have one\n"
                                "\n  - Example: oauth:43rip6j6fgio8n5xly1oum1lph8ikl1\n"
                                "\n  - Ctrl + Shift + V to Paste into Terminal or Right Click\n"
                                "\nPaste OAUTH Token Here and press Enter: ").lower()

        print(len(token) * '*')
        return token

    def getChannelName(self):
        channel_name = input("\n-------------------------\n"
                        "|   Type Channel Name   |\n"
                        "-------------------------\n"
                        "\n  - E.g: xQc\n"
                        "> ").lower().replace(" ", "")

        return channel_name
    
    def getNumber(self):
        while True:
            try:
                number = int(input("\n---------------------------\n"
                                "|   Type Number from 1-10   |\n"
                                "--------------------------\n"
                                "\n  - 1 Means a very slow chat speed\n"
                                "\n  - 10 Means a very fast chat speed\n"
                                "> "))
            except ValueError:
                print("\nInvalid Input.\n")
                
            else:
                if number not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    print("\nInvalid Input.\n")
                else:
                    return number

    def menu(self):
        token = self.getToken()
        channel_name = self.getChannelName()
        number = self.getNumber()
        return token, channel_name, number
        