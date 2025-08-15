from app import db, login_manager
from sqlalchemy import Integer, String, DateTime, Boolean
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id:int):
    return User.query.get(user_id)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.Integer, nullable=True)
    password = db.Column(db.Integer, nullable=True)
    
    

class Contato(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True,)
    name = db.Column(String, nullable=True)
    email = db.Column(String, nullable=True)
    subject = db.Column(String, nullable=True)
    message = db.Column(String, nullable=True)
    
    date_sended = db.Column(DateTime, default=datetime.utcnow())
    answered = db.Column(Boolean, default=False)

    # def __repr__(self):
    #     return f" name: {self.name} \n email: {self.email} \n subject: {self.subject} \n message: {self.message}"
    
    