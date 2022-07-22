from datetime import date
from random import randint
import os
import time


def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Message:
    def __init__(self, sender, recipient, text) -> None:
        self.Sender = sender
        self.Recipient = recipient
        self.Text = text
        self.Time = date.today()

    def setSender(self, sender):
        self.Sender = sender

    def setRecipient(self, recipient):
        self.Recipient = recipient

    def setText(self, text):
        self.Text = text

    def getSender(self):
        return self.Sender

    def getRecipient(self):
        return self.Recipient

    def getText(self):
        return self.Text

    def setTime():
        return date.today()


class Conversation:
    def __init__(self, members, messages=[], id = ''):
        self.members = members
        self.messages = messages
        self.uniqID = date.isoformat(
            date.today())+str(members[0]) + str(randint(100, 999))

    def addMessage(self, message):
        self.messages.append(message)

    def addMember(self, member):
        self.members.append(member)

    def getMessages(self):
        return self.messages

    def getMembers(self):
        return self.members

    def printConversation(self):
        clearScreen()
        for message in self.messages:
            print(f'{message.Sender.getUserName()} Says:')
            print(message.Text)

    def createMessage(self, sender, text):
        if sender in self.members:
            recipient = self.members
            self.addMessage(
                Message(sender=sender, recipient=recipient, text=text))
        else:
            print("Unable to send message you are not a part of the conversation")

    def getUniqId(self):
        return self.uniqID


class Member:
    def __init__(self, username, id = ''):
        self.userName = username
        self.userId = str(username)+date.isoformat(date.today()
                                                   ) + str(randint(100, 999))

    def getUserId(self):
        return self.userName

    def getUserName(self):
        return self.userName

    def setUserName(self, username):
        self.userName = username


def createConversation(members):
    return Conversation(members)


def createMember(username):
    return Member(username)


def mainMenue():
    cancel = False
    while not cancel:
        print(f'1 Create a new conversation')
        print(f'2 View Conversation')
        print(f'3 Create a Member')
        print(f'4 Cancel')
        choice = input()
        if int(choice) == 1 or int(choice) == 2 or int(choice) == 3:
            if int(choice) == 1:
                MenueCreateConversation()
            if int(choice) == 2:
                viewConversation(conversation) 
            if int(choice) == 3:
                pass
            if int(choice) == 4:
                cancel = True
        else:
            print(f'{choice} is not a valid choice')


def MenueCreateConversation():
    cancel = False
    while not cancel:
        print(f'1 Add Memeber to the conversation')
        print(f'2 send a Message to the conversation')
        print(f'3 Cancel')
        choice = input
        if int(choice) == 1 or int(choice) == 2:
            if int(choice) == 1:
                pass
            if int(choice) == 2:
                pass
            if int(choice) == 3:
                cancel = True
        else:
            print(f'{choice} is not a valid choice')


def main():
    k = createMember("KaydonStubbs")
    t = createMember("TashaStubbs")
    con = createConversation([k, t])
    time.sleep(3)
    con.createMessage(k, "Hey Beauty")
    con.printConversation()
    time.sleep(3)
    con.createMessage(t, "Hey Studd")
    con.printConversation()
    time.sleep(3)
    con.createMessage("Bob", "Hey Studd")
    con.printConversation()
    time.sleep(3)
    print(con.getUniqId())


if __name__ == '__main__':
    main()
 