from flask import Flask
from flask_migrate import Migrate
from models import db
from routes import init


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    Migrate(app, db)
    db.init_app(app)
    init(app)

    return app
