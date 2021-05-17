from flask_admin import Admin
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin

from wtforms import PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp
from flask import url_for, redirect
from flask_login import current_user


class ProjectView(ModelView):

    def is_accessible(self):
        return current_user.is_admin()
