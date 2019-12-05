import datetime
from peewee import *

DATABASE = SqliteDatabase('investments.sqlite')


class Stock(Model):
    id = PrimaryKeyField(null=False)
    name = CharField()
    company = CharField()
    amount = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class ETF(Model):
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
    DATABASE.create_tables([Stock, ETF, Bond], safe=True)
    print("TABLES Created")
    DATABASE.close()