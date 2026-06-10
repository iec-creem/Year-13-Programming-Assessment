# Import external libraries
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Import database
from . import db

# Import from .models user
from .models import User


# Set auth blueprint
auth = Blueprint("auth", __name__)


# Sign-up route
@auth.route("/sign-up", methods=['GET', 'POST'])
# Sign up fuction
# Returns sign up page
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        # Check that the email and username are unique
        
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()
        
        # Validation of password, username, and email
        
        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) <8:
            flash('Password is too short.', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(email) < 4:
            flash('Email is not valid.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='scrypt:32768:8:1'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Your account has been created!', category='success')
            return redirect(url_for('views.home', user=current_user))
        
    return render_template("sign_up.html")

# Login route
@auth.route("/login", methods=['GET', 'POST'])
# Login fuction
# Returns login page
def login():
    # Gets email and password from login form
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Queries database to receive user information using email address
        user = User.query.filter_by(email=email).first()
        # Checks email and password
        if user:
            # If correct log in user and redirect to home page
            if check_password_hash(user.password, password):
                flash('You have logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home', user=current_user))
            # If incorrect password flash error
            else:
                flash('Incorrect Password.', category='error')
        # If incorrect email flash error
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)

# Logout route
@auth.route("/logout")
@login_required
# Logout fuction
# Returns logout page
def logout():
    logout_user()
    flash('You have been logged out!', category='success')
    return redirect(url_for('views.home'))