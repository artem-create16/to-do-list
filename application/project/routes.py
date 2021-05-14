import os

from flask import Blueprint
import application.project.controller as controller

template_dir = os.path.abspath('../templates')
project_blueprint = Blueprint('project', __name__, url_prefix='/project', template_folder=template_dir)


@project_blueprint.route('/project')
def show_projects():
    return controller.show_projects_controller()

@project_blueprint.route('/new')
def create_project():
    return controller.create_project_controller()


