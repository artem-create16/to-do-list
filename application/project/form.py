from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ProjectCreating(FlaskForm):
    """Creating new project"""
    title = StringField('Title', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    short_description = StringField('Short_description', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])