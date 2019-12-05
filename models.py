from peewee import *

DATABASE = SqliteDatabase('investments.sqlite')


class Stock(Model):
    name = CharField()
    company = CharField()
    amount = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class ETF(Model):
    name = CharField()
    company = CharField()
    country = CharField()
    amount = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Bond(Model): 
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