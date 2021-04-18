import os

from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))

db = SQLAlchemy(app)
migrate = Migrate(app, db)
