class ConnectInfo:
    def __init__(self, token, channel) -> None:
        self.server = "irc.chat.twitch.tv"
        self.port = 6667
        self.nickname = 'getTwitchChatMessages'
        self.token = rf"{token}"
        self.channel = rf"#{channel}"
    
    def getServer(self):
        return self.server
    
    def getPort(self):
        return self.port
    
    def getNickname(self):
        return self.nickname
    
    def getToken(self):
        return self.token
    
    def getChannel(self):
        return self.channel