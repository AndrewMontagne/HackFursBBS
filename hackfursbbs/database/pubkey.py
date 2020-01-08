from sqlobject import *


class Pubkey(SQLObject):
    user = ForeignKey("User")
    type = StringCol()
    fingerprint = StringCol()
