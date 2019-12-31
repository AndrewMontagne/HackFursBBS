import asyncio
import asyncssh
import os
import subprocess
import sys


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
        return False  # user does not require auth to connect