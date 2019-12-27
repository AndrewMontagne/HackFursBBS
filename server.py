#!/usr/bin/env python3

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

    def connection_lost(self, exc):
        if exc:
            print('SSH connection error: ' + str(exc), file=sys.stderr)
        else:
            print('SSH connection closed.')

    def begin_auth(self, username):
        return False  # user does not require auth to connect


async def handle_client(process):
    process.stdin.channel.set_line_mode(False)

    env=process.env
    env['TERM'] = process.get_terminal_type()
    env['COLUMNS'] = str(process.get_terminal_size()[0])
    env['LINES'] = str(process.get_terminal_size()[1])
    env['SHELL'] = '/bin/bash'
    env['USER'] = 'andrew'

    bc_proc = subprocess.Popen(['python3', 'splash.py'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, env=env, start_new_session=True, encoding=None)

    await process.redirect(stdin=bc_proc.stdin, stdout=bc_proc.stdout,
                           stderr=bc_proc.stderr)
    await process.stdout.drain()
    process.exit(0)


async def start_server(port):
    print("Starting server on port " + str(port) + "...")
    await asyncssh.listen('', port, server_host_keys=['ssh_host_key'],
                          #sftp_factory=MySFTPServer,
                          #allow_scp=True,
                          server_factory=MySSHServer,
                          process_factory=handle_client)

loop = asyncio.get_event_loop()

port = 2022

if len(sys.argv) > 1:
    port = int(sys.argv[1])

try:
    loop.run_until_complete(start_server(port))
except (OSError, asyncssh.Error) as exc:
    sys.exit('Error starting server: ' + str(exc))

loop.run_forever()
