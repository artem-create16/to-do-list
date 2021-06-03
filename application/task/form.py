from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class TaskForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    description = StringField('Description')
    creator_id = StringField('Creator_id', validators=[DataRequired()])
    assignee_id = SelectField('Assignee_id', validators=[DataRequired()])
    submit = SubmitField('Create')