import datetime
from peewee import *
from playhouse.db_url import connect
from flask_login import UserMixin


DATABASE = SqliteDatabase('investments.sqlite')

class User(UserMixin, Model):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)

    class Meta:
        database = DATABASE

class Stock(Model):
    id = PrimaryKeyField(null=False)
    name = CharField()
    company = CharField()
    amount = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Etf(Model):
    id = PrimaryKeyField(null=False)
    name = CharField()
    company = CharField()
    country = CharField()
    amount = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Bond(Model): 
    id = PrimaryKeyField(null=False)
    name = CharField()
    company = CharField()
    amount = FloatField()
    years = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Stock, Etf, Bond], safe=True)
    print("TABLES Created")
    DATABASE.close()