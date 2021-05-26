from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectMultipleField
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    short_description = StringField('Short_description', validators=[DataRequired()])
    description = TextAreaField('Description')
    users = SelectMultipleField('Users', choices=[])
    submit = SubmitField('Sign In')
