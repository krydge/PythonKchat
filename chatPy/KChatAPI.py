from flask import Flask
from flask import request
from chat import createMember

app = Flask(__name__)
@app.route('/healthCheck')
def health():
    print(request.json)
    return 'kchat up and running'

@app.route('/createMember/<membername>')
def Member(membername):
    member = createMember(membername)
    return member.getUserName()
if __name__== '__main__':
    app.run()