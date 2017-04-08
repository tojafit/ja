from flask import Flask

app = Flask(__name__)

@app.route('/') # 'http://www.tojafit.com/'
def home():
    return "Hello, world!"

@app.route('/') # 'http://www.tojafit.com/'
def home():
    return "Hello, world!"

@app.route('/checkTeamName/<string:teamName>')
def checkTeamName(teamName):
    pass

@app.route('/createTeam', methods=['POST'])
def createTeam():
    pass

app.run(port=5000)
