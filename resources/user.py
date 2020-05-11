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
class UserRegister(Resource):
    data = parser.parse_args() 
    def post(self):
        if UserModel.find_by_username(data['username']):
            return {"message":"user is already registered"},400
        UserModel.save_to_db(**data)
        return {"message":"user successfully registered"},200

class UserLogin(Resource):
    data = parser.parse_args()
    
    def get(self, user_id):
        user =  UserModel.find_by_id(user_id)
        if not user:
            return {"message":"user not found"},400
        return user.json(),200


