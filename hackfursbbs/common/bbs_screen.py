import urwid.raw_display
import os


class BbsScreen(urwid.raw_display.Screen):

    def get_cols_rows(self):
        return int(os.getenv('COLUMNS')), int(os.getenv('LINES'))
