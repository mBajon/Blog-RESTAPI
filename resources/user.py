from flask_restful import request, reqparse, Resource
from werkzeug.security import safe_str_cmp
from models.user import UserModel


parser = reqparse.RequestParser()
parser.add_argument(
        'username',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )
parser.add_argument(
        'password',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )
class user(Resource):
    data = parser.parse_args() 
    def post(self):
        user = UserModel.find_by_username(data['username'])