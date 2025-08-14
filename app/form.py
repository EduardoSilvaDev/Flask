from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from app import db
from app.models import Contato

class ContatoForm(FlaskForm):
    name = StringField('Nome',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    subject = StringField('Assunto',validators=[DataRequired()])
    message = StringField('Menssagem',validators=[DataRequired()])
    btn_submit = SubmitField('Enviar')

    def save(self):
        contato = Contato(
            name = self.name.data,
            email = self.email.data,
            subject = self.subject.data,
            message = self.message.data
        )
        db.session.add(contato)
        db.session.commit()
    