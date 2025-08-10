from app import db
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

class Contato(db.Model):
    id = db.Column(Integer, primary_key=True,)
    name = db.Column(String, nullable=True)
    email = db.Column(String, nullable=True)
    subject = db.Column(String, nullable=True)
    message = db.Column(String, nullable=True)
    
    date_sended = db.Column(DateTime, default=datetime.utcnow())
    