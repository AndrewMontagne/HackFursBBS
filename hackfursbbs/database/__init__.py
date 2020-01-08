from .pubkey import Pubkey
from .users import User
from sqlobject import *
import pymysql

sqlhub.processConnection = connectionForURI('mysql://hackfursbbs:password@127.0.0.1/hackfursbbs?driver=pymysql')

