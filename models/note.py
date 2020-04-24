from db import db
from datetime import datetime
from sqlalchemy.ext.serializer import Serializer

class NoteModel(db.Model):
    __tablename__='notes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False,nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    note = db.Column(db.String(5000), unique=False, nullable=False)
    created_date = db.Column(db.Date, nullable=False,
        default=datetime.utcnow)
    updated_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, title, author, note):
        self.title=title
        self.author=author
        self.note=note
    
    def json(self):
        return {"Title":self.title, "Author":self.author, "Note":self.note}

    @classmethod
    def filter_by_author(cls,author):
        return cls.query.filter_by(author=author).all()

    @classmethod
    def filter_by_date(cls, date):
        return cls.query.filter_by(date=date).all()

    @classmethod
    def filter_by_title(cls, title):
       return cls.query.filter_by(title=title).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

