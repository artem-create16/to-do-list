import datetime
import enum
from application import db
from werkzeug.security import generate_password_hash,  check_password_hash


class Role(enum.Enum):
    admin = 0
    user = 1


class Status(enum.Enum):
    to_do = 'To Do'
    in_progress = 'In Progress'
    in_review = 'In Review'
    done = 'Done'


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)


projects_tasks = db.Table(
    'projects_tasks',
    db.Column('projects_id', db.Integer, db.ForeignKey('projects.id')),
    db.Column('tasks_id', db.Integer, db.ForeignKey('tasks.id'))
)


class User(TimestampMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(db.Enum(Role), nullable=False)

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)
    #
    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)


class Projects(TimestampMixin, db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    short_description = db.Column(db.String())
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Tasks(TimestampMixin, db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
