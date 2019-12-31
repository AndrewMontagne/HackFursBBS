class BaseApplet:

    main_loop = None
    main_widget = None
    tick_rate = 0
    tick_count = 0
    in_foreground = False
    applet_name = "BBS Applet"

    def enter_foreground(self):
        self.in_foreground = True
        self.change_widget(self.main_widget)
        print("\x1b]2;" + self.applet_name + "\x07")
        return

    def enter_background(self):
        self.in_foreground = False
        return

    def change_widget(self, _new_widget):
        self.main_widget = _new_widget
        if self.in_foreground:
            self.main_loop.widget = self.main_widget

    def every_tick(self):
        if self.tick_rate < 0:
            return
        self.tick_count += 1
        if self.tick_count >= self.tick_rate:
            self.tick()
            self.tick_count = 0

    def tick(self):
        return

    def start(self, _main_loop):
        self.main_loop = _main_loop
        self.enter_foreground()

    def exit(self):
        self.main_loop = None
        self.main_widget = None
