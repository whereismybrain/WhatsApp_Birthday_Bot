import glob
import random

class Init_Messages:
    def __init__(self):
        self.message_list = glob.glob("messages/*.txt")
        self.messages = self.setup()

    def setup(self):
        tmp = []
        for msg in self.message_list:
            with open(msg, 'r') as file:
                text = file.read().replace('\n', '')
            tmp.append(text)
        return tmp

class randomize_messages(Init_Messages):
    def __init__(self, already_sent):
        Init_Messages.__init__(self)
        self.already_sent = already_sent
        self.return_value = self.randomize()

    def randomize(self):
        while True:
            self.chosen_index = random.choice(range(len(self.messages)))
            if self.chosen_index not in self.already_sent:
                break
        self.chosen_message = self.messages[self.chosen_index]
        return [self.chosen_index, self.chosen_message]

    def __call__(self):
        return self.return_value
