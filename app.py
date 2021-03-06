from flask import Flask, jsonify, request

app = Flask(__name__)


organizations = {
    'teams' : [
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
}



@app.route('/')  # 'http://www.tojafit.com/'
def home():
    return "Hello, world!"


# GET method to check if the team name is already taken.
@app.route('/checkTeamName/<string:team_name>')
def check_team_name(team_name):
    for team in organizations['teams']:
        if team['name'] == team_name:
            return jsonify(False)
    return jsonify(True)


# POST method to create new team. This method requires unique teamName.
@app.route('/createTeam', methods=['POST'])
def create_team():
    request_data = request.get_json()
    new_team = {
        'name' : request_data['name']
    }
    organizations['teams'].append(new_team)
    return jsonify(new_team)



@app.route('/getTeamList')
def get_team_list():
    return jsonify({'teams':organizations['teams']})


@app.route('/joinTeam',methods=['POST'])
def join_team():
    flag = False
    request_data = request.get_json()
    team_name = request_data['team_name']
    print(team_name)
    new_member = {
        'email' : request_data['email']
    }
    for team in organizations['teams']:
        print("inside loop")
        if team['name'] == team_name:
            team['members'].append(new_member)
            flag = True
    if flag:
        return jsonify(organizations)

    return jsonify('Failure')

app.run(port=5000)
