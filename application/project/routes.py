import os

from flask import Blueprint
import application.project.controller as controller

template_dir = os.path.abspath('../templates')
project_blueprint = Blueprint('project', __name__, url_prefix='/project', template_folder=template_dir)


@project_blueprint.route('/my')
def show_projects():
    return controller.show_projects_controller()

@project_blueprint.route('/new', methods=['POST', 'GET'])
def create_project():
    return controller.create_project_controller()

@project_blueprint.route('/<project_id>')
def show_project(project_id):
    return controller.show_project_controller(project_id)

@project_blueprint.route('/<project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    return controller.edit_project_controller(project_id)

