from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class ContatoForm(FlaskForm):
    name = StringField('Nome',validators=[DataRequired()])
    email = StringField('E-mail',validators=[DataRequired(), Email()])
    subject = StringField('Assunto',validators=[DataRequired()])
    message = StringField('Menssagem',validators=[DataRequired()])
    submit = SubmitField('Enviar')

