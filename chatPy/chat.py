from  datetime import date
import os
import time

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

class Message:
    def __init__(self, sender, recipient, text ) -> None:
        self.Sender = sender
        self.Recipient = recipient
        self.Text = text
        self.Time = date.today()
    
    def setSender(self, sender):
        self.Sender = sender

    def setRecipient(self, recipient):
        self.Recipient =  recipient

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
    def __init__(self, members, messages = []):
        self.members = members
        self.messages = messages

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
            print(f'{message.Sender} Says:')
            print(message.Text)

    def createMessage(self,sender,text):
        if sender in self.members:
            recipient =self.members
            self.addMessage(Message(sender = sender, recipient = recipient, text = text))
        else:
            print("Unable to send message you are not a part of the conversation")
    

def createConversation(members):
    return Conversation(members)

def main():
    con = createConversation(["Kaydon","Tasha"])
    con.createMessage("Kaydon","Hey Beauty")
    con.printConversation()
    time.sleep(3)
    con.createMessage("Tasha","Hey Studd")
    con.printConversation()
    pass


if __name__ == '__main__':
    main()