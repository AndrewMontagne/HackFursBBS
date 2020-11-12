import urwid
from hackfursbbs.common.base_applet import BaseApplet
from hackfursbbs.common.database import User

class Register(BaseApplet):

    def _handle_none_auth_button(self, button, userdata):
        if button.get_state():
            self.alert("""We strongly advise that you supply a backup authentication method!

In the event you lose all of your public keys, we will not be able to allow you back into your account!""", 12)

    def _handle_submit_button(self, button):
        user = User.create()
        user.username = self.username_field.edit_text
        user.authkeys_url = self.gh_username_field.edit_text
        user.save()

    def __init__(self):
        super().__init__()

        self.tick_rate = 10
        self.applet_name = "Registration"

        blank = urwid.Divider()

        self.username_field = urwid.Edit('Username: ')
        self.gh_username_field = urwid.Edit('GitHub Username: ')

        backup_auth_group = []
        self.backup_auth_totp = urwid.RadioButton(backup_auth_group, "Time-Based OTP", state=False)
        self.backup_auth_none = urwid.RadioButton(backup_auth_group, "None (Not Recommended)", state=False)
        urwid.connect_signal(self.backup_auth_none, 'postchange', self._handle_none_auth_button)

        self.submit_form = urwid.Button('Submit', self._handle_submit_button)

        list = urwid.SimpleFocusListWalker([
            blank,
            urwid.Text("""\
Welcome to the HackFurs BBS!

This new, fully Open Source Bulletin Board. We're still working on things, but if you would like to be \
involved in helping us with this project, you can contribute fix and feature pull requests and issues on our GitHub \
repository at: https://github.com/AndrewMontagne/HackFursBBS"""),
            blank,
            urwid.Text("What would you like your username to be? This can be up to 16 characters long, \
and consist of alphanumeric characters."),
            blank,
            self.username_field,
            blank,
            urwid.Text("If you have an account on GitHub, we can enumerate your SSH pubkeys from there as well. \
This step is entirely optional."),
            blank,
            self.gh_username_field,
            blank,
            urwid.Text("Finally, we would like a backup method of recovering your account. \
Please pick one of the following options:"),
            blank,
            self.backup_auth_totp,
            self.backup_auth_none,
            blank,
            self.submit_form,
            blank
        ])
        listbox = urwid.ListBox(list)
        listbox = urwid.AttrMap(listbox, 'banner')
        padding = urwid.Padding(listbox, align='center', width=60)
        padding = urwid.AttrMap(padding, 'bg')

        self.main_widget = padding