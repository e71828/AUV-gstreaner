#!/usr/bin/env python
import threading
import time
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import GLib, Gtk, GObject


class Application(Gtk.Application):

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        self.progress = Gtk.ProgressBar(show_text=True)

        window.set_child(self.progress)
        window.present()

        thread = threading.Thread(target=self.example_target)
        thread.daemon = True
        thread.start()

    def update_progess(self, i):
        self.progress.pulse()
        self.progress.set_text(str(i))
        return False

    def example_target(self):
        i = 0
        while True:
            GLib.idle_add(self.update_progess, i)
            time.sleep(0.2)
            i = i + 1


app = Application()
app.run()
