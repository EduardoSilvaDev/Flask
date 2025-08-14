from app import db
from sqlalchemy import Integer, String, DateTime, Boolean
from datetime import datetime

class Contato(db.Model):
    id = db.Column(Integer, primary_key=True,)
    name = db.Column(String, nullable=True)
    email = db.Column(String, nullable=True)
    subject = db.Column(String, nullable=True)
    message = db.Column(String, nullable=True)
    
    date_sended = db.Column(DateTime, default=datetime.utcnow())
    answered = db.Column(Boolean, default=False)

    def __repr__(self):
        return f" name: {self.name} \n email: {self.email} \n subject: {self.subject} \n message: {self.message}"