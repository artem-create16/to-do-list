import os

from flask import Blueprint, render_template, request

from application.models import Project

template_dir = os.path.abspath('../templates')
main_blueprint = Blueprint('main', __name__, template_folder=template_dir)


@main_blueprint.route('/')
def index():
    search = request.args.get('search')
    if search:
        projects = Project.query.filter(
            Project.title.contains(search) |
            Project.subject.contains(search) |
            Project.description.contains(search) |
            Project.short_description.contains(search)
        ).order_by(Project.created_at.desc()).all()
    else:
        projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('main/index.html', title='Index', projects=projects)
