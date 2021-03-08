import forms, datetime
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sknvns-vo w-nvpoenovwenovwpovn s'

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Stinger14@localhost/e4l_test'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://igotdvwfrjomru:6b9944648415a332b9e5cdf2442386bc9c18139103ebdc6557bac0886a570f2a@ec2-52-203-165-126.compute-1.amazonaws.com:5432/dcq2cjnuaud3h8'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    country = db.Column(db.String(200))
    language = db.Column(db.String(200))
    interests = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username, password, first_name, last_name, country, language, interests):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.language = language
        self.interests = interests


@app.route('/register', methods=["GET", "POST"])
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        data = User(
            form.username.data, form.password.data, form.first_name.data, 
            form.last_name.data, form.country.data, form.language.data,
            form.interests.data
            )
        db.session.add(data)
        db.session.commit()
        return render_template('index.html', user=User.query.filter_by(username=form.username.data).first())
    return render_template('register.html', form=form)


@app.route('/', methods=["GET", "POST"])
@app.route('/login', methods=["GET", "POST"])
def index():
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if form.password.data == user.password:
            return render_template('index.html', user=user, friends=User.query.all())
    return render_template('login.html', form=form)


@app.route('/<friend>', methods=["GET", "POST"])
def friend(friend):
    user = User.query.filter_by(username=friend).first()
    return render_template('index.html', user=user, friends=User.query.all())

@app.route('/data', methods=["GET"])
def user_data():
    user = User.query.filter_by(username="Jonah_Poulson").first()
    return render_template('data.html', user=user)

@app.route('/about', methods=["GET"])
def about():
    user = User.query.filter_by(username="Jonah_Poulson").first()
    return render_template('about.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
    friends = User.query.all()
    for friend in friends:
        print(friend.first_name)