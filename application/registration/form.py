from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.widgets import PasswordInput


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField("Email",  validators=[DataRequired(), Email("Invalid email")])
    password = StringField('Password', validators=[DataRequired()], widget=PasswordInput(hide_value=False))
