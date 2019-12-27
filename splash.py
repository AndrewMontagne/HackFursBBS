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
    raise urwid.ExitMainLoop()

palette = [
    ('banner', 'white', 'black'),
    ('streak', 'black', 'black'),
    ('bg', 'black', 'black'),]

txt = urwid.Text(('banner', u'''
 ██╗ ██╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██╗   ██╗██████╗ ███████╗
████████╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██║   ██║██╔══██╗██╔════╝
╚██╔═██╔╝███████║███████║██║     █████╔╝ █████╗  ██║   ██║██████╔╝███████╗
████████╗██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██║   ██║██╔══██╗╚════██║
╚██╔═██╔╝██║  ██║██║  ██║╚██████╗██║  ██╗██║     ╚██████╔╝██║  ██║███████║
 ╚═╝ ╚═╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝
 
                       Press any key to continue...                       
                       '''), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')

screen = simple_display()

print(chr(27) + "[?1049h")
urwid.MainLoop(map2, palette, screen, unhandled_input=exit_app).run()
print(chr(27) + "[2J")
print(chr(27) + "[?1049l")



