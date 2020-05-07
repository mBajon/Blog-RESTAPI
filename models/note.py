from db import db
from datetime import datetime
from models.author import AuthorModel

class NoteModel(db.Model):
    __tablename__='notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False,nullable=False)
    note = db.Column(db.String(5000), unique=False, nullable=False)
    created_date = db.Column(db.Date, nullable=False,
        default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=True)
    author_id=db.Column(db.Integer, db.ForeignKey('authors.id'))
    author=db.relationship('AuthorModel')


    def __init__(self, title, author_id, note):
        self.title=title
        self.author_id=author_id
        self.note=note
    
    def json(self):
        author=AuthorModel.filter_by_id(self.author_id)
        if author is not None:
            return {"Title" : self.title, "Author": author.name, "Note" : self.note} 
        return {"message: "} 

    @classmethod
    def filter_by_author(cls,author):
        return cls.query.filter_by(author=author).all()

    @classmethod
    def filter_by_title(cls, title):
       return cls.query.filter_by(title=title).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

