from flask import Flask, render_template, url_for, redirect, flash, g
from flask_login import LoginManager, login_user, logout_user, login_required
from flask_bcrypt import check_password_hash

import forms
import models
import datetime

app = Flask(__name__)
app.secret_key = 'sknvns-vo w-nvpoenovwenovwpovn s'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """connnect to the database"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """close the connection to the database"""
    g.db.close()
    return response


@app.route('/<username>')
def index(username):
    user = models.User.select().where(models.User.username == username).get()
    friends = models.User.select().order_by(models.User.id.desc())
    return render_template('index.html', user=user, friends=friends)

@app.route('/<username>/about')
def about(username):
    user = models.User.select().where(models.User.username == username).get()
    friends = models.User.select().order_by(models.User.id.desc())
    return render_template('about.html', user=user, friends=friends)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        models.User.create_user(
            username=form.username.data,
            password=form.password.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            date_created=datetime.datetime.now(),
            country=form.country.data,
            language=form.language.data,
            interests=form.interests.data
        )
        user = models.User.select().where(models.User.username == form.username.data).get()
        friends = models.User.select().order_by(models.User.id.desc())
        return render_template('index.html', user=user, friends=friends)
    return render_template('register.html', form=form)

@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.username == form.username.data)
        except models.DoesNotExist:
            flash("Your Username or Password doesn't match", "error")
        else:
            if (user.password == form.password.data):
                login_user(user)
                flash("you've been logged in", "success")
                friends = models.User.select().order_by(models.User.id.desc())
                return render_template('index.html', user=user, friends=friends)
            else:
                return render_template('login.html', form=form)
                flash("Wrong username or password", "error")
    return render_template('login.html', form=form)


if __name__ == "__main__":
    models.initialize()
    app.run()

