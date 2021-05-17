import os

import flask_login
from dotenv import load_dotenv
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = flask_login.LoginManager()



def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from application.main.routes import main_blueprint
        from application.auth.routes import auth_blueprint
        from application.project.routes import project_blueprint
        from application.models import User, Task, Project
        from .admin import ProjectView
        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(project_blueprint)
        # commands
        from application.core.commands import seed_db
        app.cli.add_command(seed_db)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin = Admin(app, url='/admin')
    admin.add_view(ProjectView(Project, db.session, name='Projects',
                               endpoint="if you insert the word 'admin' here, it doesn't work"))

    return app

