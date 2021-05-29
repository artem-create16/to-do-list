import os
import application.task.controller as controller
from flask import Blueprint

template_dir = os.path.abspath('../templates')
task_blueprint = Blueprint('task', __name__, url_prefix='/task', template_folder=template_dir)


@task_blueprint.route('/<project_id>/create', methods=['GET', 'POST'])
def create_task(project_id):
    return controller.create_task(project_id)


@task_blueprint.route('/<task_id>/<project_id>/delete')
def delete_task(task_id, project_id):
    return controller.delete_task(task_id, project_id)
