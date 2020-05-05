from models.author import AuthorModel
from flask_jwt import JWT, jwt_required
from flask_restful import Resource, reqparse

class Author(Resource):
    parser = reqparse.RequestParser()

    def post(self, name):
        if AuthorModel.filter_by_name(name):
            return {"message":"author with that name already exists"},409

        data=Author.parser.parse_args()
        author=AuthorModel(name)

        try:
            author.save_to_db()
        except Exception:
            return {'message':'can not save the note'},500
        
        return author.json(), 201   




    
