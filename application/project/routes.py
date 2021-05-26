import os

from flask import Blueprint
from flask_security import login_required
import application.project.controller as controller

template_dir = os.path.abspath('../templates')
project_blueprint = Blueprint('project', __name__, url_prefix='/project', template_folder=template_dir)


@project_blueprint.route('/my')
@login_required
def show_projects():
    return controller.show_projects()


@project_blueprint.route('/new', methods=['POST', 'GET'])
@login_required
def create_project():
    return controller.create_project()


@project_blueprint.route('/<project_id>')
@login_required
def show_project(project_id):
    return controller.show_project(project_id)


@project_blueprint.route('/<project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    return controller.edit_project(project_id)


@project_blueprint.route('/<project_id>/delete')
@login_required
def delete_project(project_id):
    return controller.delete_project(project_id)
