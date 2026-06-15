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


# Create blog post route
@views.route("/create-post", methods=['GET', 'POST'])
@login_required
# Create blog post route function
# Returns create_post.html
def create_post():
    return render_template("create_post.html", user=current_user)