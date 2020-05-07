from models.author import AuthorModel
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, reqparse

def _author(name):
    return AuthorModel.filter_by_name(name)

def _author_json(name):
    author = AuthorModel.filter_by_name(name)
    return author.json()

class Author(Resource):
    parser = reqparse.RequestParser()

    def post(self, name):
        if _author(name):
            return {"message":"author with that name already exists"},409

        data=Author.parser.parse_args()
        author=AuthorModel(name)

        try:
            author.save_to_db()
        except Exception:
            return {'message':'can not save the note'},500
        
        return author.json(), 201   
    
    def get(self, name):
        
        if _author(name):
            return _author_json(name),200
        return {"message":"No author with that name"},404 

    def delete(self, name):
        if _author:
            _author.delete_from_db()
                    
        return {"message":"Author:{} was deleted".format(name)},200

