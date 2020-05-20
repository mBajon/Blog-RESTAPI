from flask_restful import request, reqparse, Resource
from werkzeug.security import safe_str_cmp
from models.user import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required,
    jwt_required,
    get_raw_jwt
    )
#from blacklist import BLACKLIST

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
    
    def post(self):
        data = parser.parse_args()
        if UserModel.find_by_username(data['username']) is not None:
            return {"message":"user is already registered"},400
        
        user =  UserModel(**data)
        user.save_to_db()
        return {"message":"user {} registered".format(data['username'])},201

class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message":"user was not found"},404
        return user.json(),200
    
    @classmethod
    def delete(cls, username):
        user =  UserModel.find_by_username(username)
        if user is None:
            return {"message":"user not found"},400
        user.delete_from_db()
        return {"message":"user {} was deleted".format(username)},200

