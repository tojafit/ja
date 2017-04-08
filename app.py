from flask import Flask

app = Flask(__name__)


@app.route('/') # 'http://www.tojafit.com/'
def home():
    return "Hello, world!"

#GET method to check if the team name is already taken.
@app.route('/checkTeamName/<string:teamName>')
def checkTeamName(teamName):
    pass

#POST method to create new team. This method requires unique teamName.
@app.route('/createTeam', methods=['POST'])
def create_team():
    pass

@app.route('/getTeamList/<string:orgName')
def get_team_list(orgName):
    pass

@app.route('/joinTeam',methods=['POST'])
def join_team():
    pass

app.run(port=5000)
