# Import external libraries
from flask import Blueprint, render_template

# Set auth blueprint
auth = Blueprint("auth", __name__)


# Sign-up route
@auth.route("/sign-up")
# Sign up fuction
# Returns sign up page
def sign_up():
    return render_template("sign_up.html")

# Login route
@auth.route("/login")
# Login fuction
# Returns login page
def login():
    return render_template("login.html")

# Logout route
@auth.route("/logout")
# Logout fuction
# Returns logout page
def logout():
    return render_template("logout.html")