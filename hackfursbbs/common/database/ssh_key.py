from peewee import *

from . import Base, User

class SshKey(Base):
    user = ForeignKeyField(User, null=False)
    kind = CharField(16, null=False)
    pubkey = TextField(null=False)
