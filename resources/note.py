from flask_jwt import JWT, jwt_required
from flask_restful import Resource, reqparse
from models.note import NoteModel
import datetime

class Note(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'note',
        type=str,
        required=False,
        help='This field should not be left blank'
        )
    parser.add_argument(
        'author',
        type=str,
        required=True,
        help='This field cannot be left blank'
        )

    def post(self, title):
        if NoteModel.filter_by_title(title):
            return {"message":"note with that title already exists"},409

        data=Note.parser.parse_args()
        note=NoteModel(title, **data)

        try:
            note.save_to_db()
        except Exception:
            return {'message':'can not save the note'},500
        
        return note.json(), 201

    def put(self, title):

        note=NoteModel.filter_by_title(title)
        if note is None:
            data=Note.parser.parse_args()
            note=NoteModel(title, **data)
        else:
            Note.parser.add_argument('new_title', dest='title')
            data=Note.parser.parse_args()
            note.title=data['title']
            note.author=data['author']
            note.note=data['note']
            note.updated_date=datetime.datetime.now()
        
        try:
            note.save_to_db()
        except Exception:
            return {'message':'can not save the note'},500

        return note.json(),200

    def delete(self,title):
        note=NoteModel.filter_by_title(title)
        if note:
            note.delete_from_db()
        
        return {"message":"Note:{} was deleted".format(title)},200
        


class NoteList(Resource):
    def get(self):
        return{'Notes': list(map(lambda x: x.json(), NoteModel.query.all()))}

