#!/usr/bin/env python

import urwid
from time import gmtime, strftime
from .base_applet import BaseApplet


def time_string():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


class SplashScreen(BaseApplet):

    def handle_registration_button(self, button):
        self.change_widget(self.overlay)

    def handle_exit_button(self, button):
        raise urwid.ExitMainLoop()

    def handle_popup_button(self, button):
        self.change_widget(self.center)

    def tick(self):
        self.subtext.set_text(('banner', time_string()))
        self.main_loop.draw_screen()

    def __init__(self):
        super().__init__()

        self.tick_rate = 10
        self.applet_name = "# hack furs dot sh"

        self.blank = urwid.Divider()
        self.palette = [
            ('banner', 'white', 'black'),
            ('buttonf', 'black', 'white'),
            ('button', 'black', 'dark gray'),
            ('bg', 'black', 'black'),
        ]

        self.logo = urwid.Text(('banner', u''' ██╗ ██╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗   ██╗██████╗ ███████╗
████████╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║   ██║██╔══██╗██╔════╝
╚██╔═██╔╝███████║███████║██║     █████╔╝ █████╗  ██║   ██║██████╔╝███████╗
████████╗██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗╚════██║
╚██╔═██╔╝██║  ██║██║  ██║╚██████╗██║  ██╗██║     ╚██████╔╝██║  ██║███████║
 ╚═╝ ╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝'''), align='center')

        self.subtext = urwid.Text(('banner', time_string()), align='center')

        self.registerButton = urwid.Button('Register', self.handle_registration_button)
        self.registerButton = urwid.AttrMap(self.registerButton, 'button', 'buttonf')

        self.exitButton = urwid.Button('Exit', self.handle_exit_button)
        self.exitButton = urwid.AttrMap(self.exitButton, 'button', 'buttonf')

        self.buttonPile = urwid.Pile([self.registerButton, self.blank, self.exitButton])
        self.buttonPile = urwid.Padding(self.buttonPile, align='center', width=24)

        self.pile = urwid.Pile([self.logo, self.blank, self.subtext, self.blank, self.buttonPile])

        self.center = urwid.Filler(self.pile, valign='middle', height='pack')
        self.center = urwid.AttrMap(self.center, 'bg')

        self.popuptext = urwid.Text(('banner', u'Registration is currently closed,\nplease check back in 2020!'),
                                    align='center')
        self.popupbutton = urwid.Button('Okay', self.handle_popup_button)
        self.popupbutton = urwid.AttrMap(self.popupbutton, 'button', 'buttonf')
        self.popupbutton = urwid.Padding(self.popupbutton, 'center', 8)
        self.popuppile = urwid.Pile([self.blank, self.popuptext, self.blank, self.popupbutton, self.blank])

        self.overlay = urwid.Overlay(urwid.Filler(urwid.LineBox(self.popuppile), valign='middle', height='pack'),
                                     self.center, align='center', width=40, valign='middle', height=8)

        self.main_widget = self.center



