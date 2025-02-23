from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, validators
from wtforms.validators import InputRequired

class ContactForm(FlaskForm):
    name = StringField('Name',
    validators = [InputRequired()])

    # placeholder = "Please enter your e-mail address.",
    email = EmailField('E-mail',
    [validators.DataRequired(), 
    validators.Email()])

    subject = StringField('Subject',
    validators = [InputRequired()])

    message = StringField('Message',
    validators = [InputRequired()])