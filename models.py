import datetime
from flask_login import UserMixin
from peewee import *
from psycopg2 import *


DATABASE = SqliteDatabase('lms.db')

class User(UserMixin, Model):
    id = AutoField()
    username = CharField(unique=True)
    password = CharField(max_length=100)
    first_name = TextField()
    last_name = TextField()
    date_created = DateTimeField(default=datetime.datetime.now)
    country = TextField()
    language = TextField()
    interests = TextField()

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, username, password, first_name, last_name, date_created, country, language, interests):
        try:
            cls.create(
                username=username,
                password=password,
                first_name = first_name,
                last_name = last_name,
                date_created=date_created,
                country=country,
                language=language,
                interests=interests
            )
        except IntegrityError:
            print("User already Exists")

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    User.create_user("Jonah123", "password", "Jonah", "Poulson", datetime.datetime.now(), "United States", "English/Korean", "Guitar and Anime")
    DATABASE.close()
