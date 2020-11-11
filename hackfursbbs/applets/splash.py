#!/usr/bin/env python

import urwid, math
import time
from hackfursbbs.common.base_applet import BaseApplet
from hackfursbbs.applets.register import Register


def time_string():
    march_num = math.floor(int((time.time() - 1583020800)) / 86400)
    march_suffix = 'th'
    if march_num % 10 == 1:
        march_suffix = 'st'
    elif march_num % 10 == 2:
        march_suffix = 'nd'
    elif march_num % 10 == 3:
        march_suffix = 'rd'
    return 'March ' + str(march_num) + march_suffix + ' 2020 ' + time.strftime("%H:%M:%S", time.gmtime())


class SplashScreen(BaseApplet):

    def handle_registration_button(self, button):
        self.main_loop.launch_applet(Register())

    def handle_exit_button(self, button):
        raise urwid.ExitMainLoop()

    def tick(self):
        self.subtext.set_text(('banner', time_string()))
        self.main_loop.draw_screen()

    def __init__(self):
        super().__init__()

        self.tick_rate = 10
        self.applet_name = "Welcome!"

        self.blank = urwid.Divider()

        self.logo = urwid.Text( u''' ██╗ ██╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗   ██╗██████╗ ███████╗
████████╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║   ██║██╔══██╗██╔════╝
╚██╔═██╔╝███████║███████║██║     █████╔╝ █████╗  ██║   ██║██████╔╝███████╗
████████╗██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗╚════██║
╚██╔═██╔╝██║  ██║██║  ██║╚██████╗██║  ██╗██║     ╚██████╔╝██║  ██║███████║
 ╚═╝ ╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝''', align='center')

        self.subtext = urwid.Text(time_string(), align='center')

        self.registerButton = urwid.Button('Register', self.handle_registration_button)
        self.registerButton = urwid.AttrMap(self.registerButton, 'button', 'buttonf')

        self.exitButton = urwid.Button('Exit', self.handle_exit_button)
        self.exitButton = urwid.AttrMap(self.exitButton, 'button', 'buttonf')

        self.buttonPile = urwid.Pile([self.registerButton, self.blank, self.exitButton])
        self.buttonPile = urwid.Padding(self.buttonPile, align='center', width=24)

        self.pile = urwid.Pile([self.logo, self.blank, self.subtext, self.blank, self.buttonPile])

        self.center = urwid.Filler(self.pile, valign='middle', height='pack')
        self.center = urwid.AttrMap(self.center, 'bg')

        self.main_widget = self.center



