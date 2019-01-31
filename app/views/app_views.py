""" Main app views file."""
from flask import Flask
from .entry_views import entry_bp
from .user_views import auth_bp

def create_app():
    """
    App factory for my app.
    """
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/api/v1/auth')
    app.register_blueprint(entry_bp, url_prefix='/api/v1')

    return app