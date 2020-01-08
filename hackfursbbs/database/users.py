from sqlobject import *


class User(SQLObject):
    username = StringCol()
    totp_secret = StringCol()
    preferences = StringCol()
    pubkeys = MultipleJoin("Pubkey")
