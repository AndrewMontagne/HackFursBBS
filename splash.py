#!/usr/bin/env python

import urwid
import urwid.raw_display
import urwid.web_display
from urwid import escape
import os

class simple_display(urwid.raw_display.Screen):

    def get_cols_rows(self):
        if "COLUMNS" in os.environ:
            return int(os.getenv('COLUMNS')), int(os.getenv('LINES'))
        else:
            return super().get_cols_rows()


def exit_app(key):
    if (key == 'esc'):
        raise urwid.ExitMainLoop()


def handleRegistrationButton(button):
    registerButton.original_widget.set_label(u'Registration Closed')


def handleExitButton(button):
    raise urwid.ExitMainLoop()

palette = [
    ('banner', 'white', 'black'),
    ('buttonf', 'black', 'white'),
    ('button', 'black', 'dark gray'),
    ('bg', 'black', 'black'),]

blank = urwid.Divider()

logo = urwid.Text(('banner', u''' ██╗ ██╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗   ██╗██████╗ ███████╗
████████╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║   ██║██╔══██╗██╔════╝
╚██╔═██╔╝███████║███████║██║     █████╔╝ █████╗  ██║   ██║██████╔╝███████╗
████████╗██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗╚════██║
╚██╔═██╔╝██║  ██║██║  ██║╚██████╗██║  ██╗██║     ╚██████╔╝██║  ██║███████║
 ╚═╝ ╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝'''), align='center')

subtext = urwid.Text(('banner', u'-=-=- Established 2019 -=-=-'), align='center')

registerButton = urwid.Button('Register', handleRegistrationButton)
registerButton = urwid.AttrMap(registerButton, 'button', 'buttonf')

exitButton = urwid.Button('Exit', handleExitButton)
exitButton = urwid.AttrMap(exitButton, 'button', 'buttonf')

buttonPile = urwid.Pile([registerButton, blank, exitButton])
buttonPile = urwid.Padding(buttonPile, align='center', width=24)

pile = urwid.Pile([logo, blank, subtext, blank, buttonPile])

center = urwid.Filler(pile, valign='middle', height='pack')
center = urwid.AttrMap(center, 'bg')

screen = simple_display()

print(chr(27) + "[?1049h")
urwid.MainLoop(center, palette, screen, unhandled_input=exit_app).run()
print(chr(27) + "[2J")
print(chr(27) + "[?1049l")



