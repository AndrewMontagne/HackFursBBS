from peewee import *

from . import Base

class User(Base):
    id = IntegerField()
    username = CharField()