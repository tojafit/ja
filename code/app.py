from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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


class CreateTeam(Resource):
    def post(self):
        request_data = request.get_json()
        team_name = request_data['team_name']
        member_email = request_data['member_email']
        for team in organizations['teams']:
            if team['name'] == team_name:
                return {'status': "Team name already present"}, 404
        team = {'name': team_name , 'members': [{'email':member_email}]}
        organizations['teams'].append(team)
        return 200


class JoinTeam(Resource):
    def post(self):
        request_data = request.get_json()
        team_name = request_data['team_name']
        member_email = request_data['member_email']
        for team in organizations['teams']:
            if team['name'] == team_name:
                team['members'].append(member_email)
                return 200
        return {'status': "Invalid team name"}, 404


api.add_resource(CreateTeam, '/create_team')
api.add_resource(JoinTeam, '/join_team')

app.run(port=5000)



