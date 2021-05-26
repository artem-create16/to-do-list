import os
from flask import Blueprint, render_template

from application.models import Project

template_dir = os.path.abspath('../templates')
main_blueprint = Blueprint('main', __name__, template_folder=template_dir)


@main_blueprint.route('/')
def index():
    projects = Project.query.all()
    return render_template(
        'main/index.html',
        title='Index',
        projects=projects
    )

