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
    loop.widget = overlay


def handleExitButton(button):
    raise urwid.ExitMainLoop()


def handlePopupButton(button):
    loop.widget = center

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

popuptext = urwid.Text(('banner', u'Registration is currently closed,\nplease check back here later!'), align='center')
popupbutton = urwid.Button('Okay', handlePopupButton)
popupbutton = urwid.AttrMap(popupbutton, 'button', 'buttonf')
popupbutton = urwid.Padding(popupbutton, 'center', 8)
popuppile = urwid.Pile([blank, popuptext, blank, popupbutton, blank])

overlay = urwid.Overlay(urwid.Filler(urwid.LineBox(popuppile), valign='middle', height='pack'), center,
    align='center', width=40,
    valign='middle', height=8)

screen = simple_display()

print(chr(27) + "[?1049h")
loop = urwid.MainLoop(center, palette, screen, unhandled_input=exit_app)
loop.run()
print(chr(27) + "[?1049l")



