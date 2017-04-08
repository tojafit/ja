from flask import Flask, jsonify

app = Flask(__name__)


teams = [
    {
        'name' : 'team1',
        'members' : [
            {
                'email' : 'stengali'
            },
            {
                'email' : 'aggarwal'
            }
        ]
    },
    {
        'name' : 'team2'
    }
]



@app.route('/')  # 'http://www.tojafit.com/'
def home():
    return "Hello, world!"


# GET method to check if the team name is already taken.
@app.route('/checkTeamName/<string:teamName>')
def check_team_name(teamName):
    pass


# POST method to create new team. This method requires unique teamName.
@app.route('/createTeam', methods=['POST'])
def create_team():
    pass


@app.route('/getTeamList')
def get_team_list():
    return jsonify({'teams':teams})


@app.route('/joinTeam',methods=['POST'])
def join_team():
    pass

app.run(port=5000)
