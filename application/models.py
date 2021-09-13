import datetime
import enum

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from application import db


class Role(enum.Enum):
    admin = 'Admin'
    user = 'User'


class Status(enum.Enum):
    to_do = 'To Do'
    in_progress = 'In Progress'
    in_review = 'In Review'
    done = 'Done'


class Species(enum.Enum):
    to_the_comment = 'To the comment'
    to_the_task = 'To the task'


class TimestampMixin(object):
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)


users_projects = db.Table(
    'users_projects',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
)


class User(UserMixin, TimestampMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    role = db.Column(ENUM(Role), nullable=False)
    projects = relationship('Project', secondary=users_projects, back_populates='users')
    comments = relationship('Comment', back_populates='author')

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)


class Project(TimestampMixin, db.Model):
    __tablename__ = 'projects'

    def __init__(self, title, subject, short_description, description):
        self.title = title
        self.subject = subject
        self.short_description = short_description
        self.description = description

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    short_description = db.Column(db.String())
    description = db.Column(db.Text)
    start_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    end_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    users = relationship('User', secondary=users_projects, back_populates='projects')
    tasks = relationship('Task', cascade="all,delete", back_populates='project')


class Task(TimestampMixin, db.Model):
    __tablename__ = 'tasks'

    def __init__(self, project_id, subject, description, creator_id, assignee_id, status):
        self.project_id = project_id
        self.subject = subject
        self.description = description
        self.creator_id = creator_id
        self.assignee_id = assignee_id
        self.status = status

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    project = relationship('Project', back_populates='tasks')
    subject = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    assignee_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(ENUM(Status), nullable=False)
    comments = relationship('Comment', back_populates='task')


class Comment(TimestampMixin, db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = relationship("User", back_populates="comments")
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'), nullable=False)
    task = relationship('Task', back_populates='comments')
    species = db.Column(ENUM(Species), nullable=False)
