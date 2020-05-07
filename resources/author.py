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
    
    def get(self, name):
        author = AuthorModel.filter_by_name(name)
        if author:
            return author.json(),200
        return {"message":"No author with that name"},404 

    def delete(self, name):
        author=AuthorModel.filter_by_name(name)
        if author:
            author.delete_from_db()
                    
        return {"message":"Author:{} was deleted".format(name)},200

