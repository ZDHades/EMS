from flask import Flask, app
from werkzeug.utils import append_slash_redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)

    login.init_app(app)
    login.login_view  = 'authentication.login'
    login.login_message_category = 'warning'

    with app.app_context():
        from .import routes, models
    
    return app
