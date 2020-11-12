from peewee import *

from . import Base

class User(Base):
    username = CharField(16, unique=True, null=False)
    authkeys_url = TextField()
