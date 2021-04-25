from flask import Blueprint

# from .controller import show_form, controller_greeting_route

login_blueprint = Blueprint('/login', __name__, template_folder='templates')


@login_blueprint.route('/login', methods=['POST', 'GET'])
def greeting():
    pass
    # return show_form()
