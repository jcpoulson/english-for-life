from flask_wtf import Form
from models import User
from wtforms import TextField, DateTimeField, PasswordField, StringField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

class RegisterForm(Form):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    first_name = TextField("First Name", validators=[DataRequired()])
    last_name = TextField("Last Name", validators=[DataRequired()])
    country = TextField("Country", validators=[DataRequired()])
    language = TextField("Language/Languages", validators=[DataRequired()])
    interests = TextField("Interests", validators=[DataRequired()])