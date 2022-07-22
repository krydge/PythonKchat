from  chat import Member

def createMember(Member:Member):
    query = f"insert into member(UserName) values ({Member.getUserName()}) "
    

def getMemberById(Member:Member):
    query = f'select * from member where ID = {Member.getUserId()}'
    queryResults = 'Not implimented yet'
    return queryResults

def getMemberByName(Member:Member):
    query = f'select * from member where UserName = {Member.getUserName()}'
    pass

def deleteMember(Member):
    pass

def updateMember(Member):
    pass

def createConversation(Conversation):
    pass

def getConversationById(ConversationID):
    pass

def deleteConversation(Conversation):
    pass

def createMessage(Message):
    pass

def updateMessage(Message):
    pass

def deleteMessage(Message):
    pass