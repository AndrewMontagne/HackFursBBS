import urwid
from hackfursbbs.common.base_applet import BaseApplet

class Register(BaseApplet):

    def __init__(self):
        super().__init__()

        self.tick_rate = 10
        self.applet_name = "Registration"

        blank = urwid.Divider()

        list = urwid.SimpleFocusListWalker([
            blank,
            urwid.Text("""Welcome to the HackFurs BBS!

This is a modern, SSH-based Bulletin Board System (BBS). We're still working on things, but if you would like to be involved in helping us with this project, you can contribute fix and feature pull requests and issues on our GitHub repository at: https://github.com/AndrewMontagne/HackFursBBS

For now, the only rules are as follows:
- Treat other BBS users with kindness and respect.
- Do not use our BBS to conduct illegal activities.

Thanks, and have fun!"""),
            blank,
            urwid.Padding(
                urwid.Columns([
                    (10, urwid.Pile([
                        urwid.Text('Username:', align='right'),
                        blank,
                        urwid.Text('Password:', align='right'),
                    ])),
                    urwid.Pile([
                        urwid.AttrMap(urwid.Edit(' '), 'input', 'inputf'),
                        blank,
                        urwid.AttrMap(urwid.Edit(' ', mask="*"), 'input', 'inputf'),
                    ]),
                ], dividechars=3),
                align='center', width=40)
        ])
        listbox = urwid.ListBox(list)
        listbox = urwid.AttrMap(listbox, 'banner')
        padding = urwid.Padding(listbox, align='center', width=60)
        padding = urwid.AttrMap(padding, 'bg')

        self.main_widget = padding