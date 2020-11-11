import urwid
from hackfursbbs.common.bbs_screen import BbsScreen
import time


def exit_app(key):
    if key == 'esc':
        raise urwid.ExitMainLoop()


def tick(loop, user_data=None):
    # Rounding down then adding 1/10th of a second to prevent timer drift
    current_time = int(time.time() * 10) / 10.0
    loop.set_alarm_at(current_time + 0.1, tick)
    loop.current_applet._every_tick()


class AppLoop(urwid.MainLoop):

    default_palette = [
        ('buttonf', 'black', 'white'),
        ('button', 'black', 'dark gray'),
        ('input', 'white', 'dark gray'),
        ('inputf', 'black', 'light gray'),
    ]

    def __init__(self, _default_applet, username=None):
        self.current_applet = _default_applet
        super().__init__(None, self.default_palette, BbsScreen(), unhandled_input=exit_app)

    def run(self):
        print("\x1b[?1049h")
        self.current_applet.start_applet(self)
        self.set_alarm_in(0.1, tick)
        super().run()
        print("\x1b[?1049l")

    def launch_applet(self, _new_applet):
        self.current_applet.stop_applet()
        self.current_applet = _new_applet
        self.current_applet.start_applet(self)