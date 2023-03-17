from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import AddUserForm, LoginForm
from werkzeug.exceptions import Unauthorized

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users_login'
app.config['SECRET_KEY'] = "SECRET!"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def redirect_to_register_page():
    return redirect('/register')


@app.route('/register', methods=["GET", "POST"])
def show_register_form():
    form = AddUserForm()
    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(name, pwd)
        new_user.email = email
        new_user.first_name = first_name
        new_user.last_name = last_name
        db.session.add(new_user)
        db.session.commit()
        session["username"] = new_user.username
        return redirect('/')
    return render_template("add_user.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def show_login_form():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.username.data
        pwd = form.password.data

        user = User.authenticate(name, pwd)
        if user:
            session["username"] = user.username
            return redirect('/secret')
        else:
            form.username.errors = ["Bad name/password"]
    return render_template("login.html", form=form)


@app.route('/secret')
def show_login_msg():
    if "username" not in session:
        raise Unauthorized()
    else:
        return redirect(f'/users/{session["username"]}')


@app.route('/logout')
def logout():
    session.pop("username")
    return redirect('/')


@app.route('/users/<username>')
def show_user_detail(username):
    user = User.query.get_or_404(username)
    return render_template('user_detail.html', user=user)
