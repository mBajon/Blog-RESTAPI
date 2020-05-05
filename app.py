from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from db import db
from resources.note import Note
from resources.note import NoteList
from resources.author import Author

app=Flask(__name__)
api=Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='maciek'
#jwt=JWT(app,authenticate,identity)

api.add_resource(Note,'/Note/<string:title>')
api.add_resource(NoteList,'/Notes')
api.add_resource(Author,'/Author/<string:name>')
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__=="__main__":
    db.init_app(app)
    app.run(debug=True)