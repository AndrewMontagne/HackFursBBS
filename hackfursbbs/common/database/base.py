from peewee import *

class Base(Model):
    class Meta:
        database = MySQLDatabase('hackfurs', user='root', password='password', host='127.0.0.1', port=3306)
