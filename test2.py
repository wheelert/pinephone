import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Custom Commands")

        self.button = Gtk.Button(label="Enable Data")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)
        
        #exit button
        self.button2 = Gtk.Button(label="Exit")
        self.button2.connect("clicked", self.AppClose)
        self.add(self.button2)
        
        
        

    def on_button_clicked(self, widget):
        print("Hello World")
        
    def AppClose(self, widget):
        exit()


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
