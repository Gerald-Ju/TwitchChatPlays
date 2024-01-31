from collections import Counter
from Modules.PressKeyVK import pressKey

class GetMessages:
    def __init__(self) -> None:
        self.list_num_msgs = []
    
    def getNumMsgs(self, message, number):
        if len(self.list_num_msgs) < (number + 1):
            self.list_num_msgs.append(message)
        else:
            self.removeReturn()
                
    def removeReturn(self):
        remove_none = list(filter(lambda item: item is not None, self.list_num_msgs))
        list_five_msgs_new = [i.replace("\r", "").replace("\\", "") for i in remove_none]

        self.list_num_msgs.clear()
        self.firstWord(list_five_msgs_new)
    
    def firstWord(self, list_five_msgs_new):
        list_first_words = [i.split(" ", 1)[0] for i in list_five_msgs_new]
        self.mostCommon(list_first_words)

    def mostCommon(self, list_first_words):
        list_words_lower = list(map(str.lower,list_first_words))
        counter = Counter(list_words_lower)
        common_key = counter.most_common(1)[0]
        pressKey(common_key)


