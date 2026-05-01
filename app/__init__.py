from flask import Flask, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from datetime import timedelta

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Set permanent session
    @app.before_request
    def make_session_permanent():
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=5)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Use full blueprint endpoint
    login_manager.login_view = 'main.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'warning'

    @login_manager.unauthorized_handler
    def unauthorized():
        flash('You must be logged in to access this page.', 'warning')
        return redirect(url_for('main.login'))

    from app.routes import main
    app.register_blueprint(main)

    return app
