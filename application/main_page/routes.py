from flask import Blueprint
from .controller import show_form


main_blueprint = Blueprint('/to-do-list', __name__, template_folder='templates')


@main_blueprint.route('/to-do-list')
def greeting():
    return show_form()

