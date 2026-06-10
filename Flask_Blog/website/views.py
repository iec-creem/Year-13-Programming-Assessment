# Import external libraries
from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

# Set blueprint
views = Blueprint("views", __name__)


# Default/home route
@views.route("/")
@views.route("/home")
@views.route("/index")
# Home route function
# Returns home.html
def home():
    return render_template("home.html", user=current_user)