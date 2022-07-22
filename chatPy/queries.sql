create Table Member(
    ID serial primary key,
    UserName Char(50) not Null,
    active boolean not null
)

create table Message(
    ID serial primary key,
    SenderId int not null,
    Recipient int not null,
    messageText Char(500) not null,
    CreatedDate Char(30) not null,
    ConversationID int not null
)

create Table Conversation(
    ID Serial primary key,
    active boolean not null
)

create table memberConversation(
    ID serial primary key,
    conversationID int not null,
    MemberId int not null
)
