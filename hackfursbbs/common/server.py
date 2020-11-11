import asyncssh
import os
import sys
import pyotp


def get_user(username):
    users = list(User.select(User.q.username == username).limit(1))
    if len(users) == 1:
        return users[0]
    else:
        return None


class MySFTPServer(asyncssh.SFTPServer):
    def __init__(self, chan):
        root = '/tmp/sftp/' + chan.get_extra_info('username')
        os.makedirs(root, exist_ok=True)
        super().__init__(chan, chroot=root)


class MySSHServer(asyncssh.SSHServer):
    def connection_made(self, conn):
        print('SSH connection received from %s.' %
              conn.get_extra_info('peername')[0])

    def connection_lost(self, exception):
        if exception:
            print('SSH connection error: ' + str(exception), file=sys.stderr)
        else:
            print('SSH connection closed.')

    def begin_auth(self, username):
        return username != "anonymous"  # user does not require auth to connect

    def validate_public_key(self, username, key):
        print(username + ' ' + key.get_algorithm() + ' ' + key.get_fingerprint())
        user = get_user(username)
        if user is None:
            return False

        for pubkey in user.pubkeys:
            if pubkey.fingerprint == key.get_fingerprint() and pubkey.type == key.get_algorithm():
                return True
        return False

    def public_key_auth_supported(self):
        return True

    def password_auth_supported(self):
        return True

    def validate_password(self, username, password):
        user = get_user(username)
        if user:
            totp = pyotp.TOTP(user.totp_secret)
            return totp.verify(password)
        else:
            return False

    def kbdint_auth_supported(self):
        return False
