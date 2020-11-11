#!/usr/bin/env python3

import asyncssh, asyncio, sys, subprocess, pymysql
from hackfursbbs.common.server import MySSHServer


async def handle_client(process):
    process.stdin.channel.set_line_mode(False)

    env = process.env
    env['TERM'] = process.get_terminal_type()
    env['COLUMNS'] = str(process.get_terminal_size()[0])
    env['LINES'] = str(process.get_terminal_size()[1])
    env['SHELL'] = '/bin/bash'
    env['USER'] = 'andrew'

    bc_proc = subprocess.Popen(['sudo -E -u andrew python3 applet.py'], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               env=env, start_new_session=True, encoding=None)

    await process.redirect(stdin=bc_proc.stdin, stdout=bc_proc.stdout)
    await process.stdout.drain()
    process.exit(0)


async def start_server(port_number):
    print("Starting server on port " + str(port_number) + "...")
    await asyncssh.listen('', port, server_host_keys=['ssh_host_key'],
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
