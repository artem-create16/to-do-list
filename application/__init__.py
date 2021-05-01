import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from .main_page.routes import main_blueprint
        from .login.routes import login_blueprint
        from .registration.routes import registration_blueprint
        from .db_model import User, Tasks, Projects
        app.register_blueprint(main_blueprint)
        app.register_blueprint(login_blueprint)
        app.register_blueprint(registration_blueprint)

    db.init_app(app)
    migrate.init_app(app, db)
    return app
