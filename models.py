import datetime
from flask_login import UserMixin
from peewee import *
from psycopg2 import *



DATABASE = PostgresqlDatabase('postgres://igotdvwfrjomru:6b9944648415a332b9e5cdf2442386bc9c18139103ebdc6557bac0886a570f2a@ec2-52-203-165-126.compute-1.amazonaws.com:5432/dcq2cjnuaud3h8')

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