from peewee import *

from . import Base, User

class Otp(Base):
    user = ForeignKeyField(User, null=False)
    interval = IntegerField(null=False)
    pubkey = TextField(null=False)
