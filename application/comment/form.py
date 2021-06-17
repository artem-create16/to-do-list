from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')