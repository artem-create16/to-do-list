from flask import render_template, redirect, url_for, request
from flask_login import current_user

from application import db
from application.models import Project
from application.models import User
from application.project.form import ProjectForm


def show_tasks():
    pass