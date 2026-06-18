# Import external libraries
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user

# Import database
from . import db

# Import from .models user
from .models import User, Post

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
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')
        
        if not title:
            flash('Title cannot be empty', category='error')
        elif not content:
            flash('Blog cannot be empty', category='error')
        else:
            post = Post(title=title, content=content, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home', user=current_user))
            
    
    return render_template("create_post.html", user=current_user)