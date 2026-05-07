# Import external libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Create app function
# Returns app

def create_app():
    app = Flask(__name__)
    
    # Import views from views.py
    from .views import views
    from .auth import auth
    
    # Register blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    return app