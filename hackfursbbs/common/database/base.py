from peewee import *

class Base(Model):
    class Meta:
        database = MySQLDatabase('db', user='hackfursbbs', password='password', host='mysql', port=3306)
