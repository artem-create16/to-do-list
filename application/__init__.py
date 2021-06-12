import os

import flask_login
from dotenv import load_dotenv
from flask import Flask
from flask_admin import Admin
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = flask_login.LoginManager()
mail = Mail()


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = str(os.getenv("WORK_MAIL"))
    app.config['MAIL_PASSWORD'] = str(os.getenv("WORK_MAIL_PASSWORD"))
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    with app.app_context():
        from application.main.routes import main_blueprint
        from application.auth.routes import auth_blueprint
        from application.project.routes import project_blueprint
        from application.task.routes import task_blueprint
        from application.models import User, Task, Project
        from .admin import AdminView, HomeAdminView
        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(project_blueprint)
        app.register_blueprint(task_blueprint)
        # commands
        from application.core.commands import seed_db
        app.cli.add_command(seed_db)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    admin = Admin(app, name='To do list', url='/', index_view=HomeAdminView(name='Home'))

    admin.add_view(AdminView(User, db.session, name='Users',
                             endpoint='User'))
    admin.add_view(AdminView(Project, db.session, name='Projects',
                             endpoint='Project'))
    admin.add_view(AdminView(Task, db.session, name='Tasks',
                             endpoint='Task'))

    return app
