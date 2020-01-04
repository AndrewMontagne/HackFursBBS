import urwid.raw_display
import shutil
import platform
import re


class BbsScreen(urwid.raw_display.Screen):

    def get_cols_rows(self):
        return shutil.get_terminal_size()

    def write(self, data) -> None:
        if "Microsoft" in platform.platform():
            # replace urwid's SI/SO, which produce artifacts under WSL.
            # https://github.com/urwid/urwid/issues/264#issuecomment-358633735
            # Above link describes the change.
            data = re.sub("[\x0e\x0f]", "", data)
        super().write(data)