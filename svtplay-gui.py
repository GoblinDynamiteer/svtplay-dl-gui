# import the library
from appJar import gui
from config import get_setting
from config import get_setting_section_keys
import subprocess
import os
import pyperclip

class svplay_dl:
    def __init__(self, dl_dir, get_subs, remux):
        self.process = None;
        self.dl_dir = dl_dir
        self.remux = remux
        self.get_subs = get_subs
    def run(self, link):
        if self.process and self.check_process():
            print("Process running!")
            return
        self.process = subprocess.Popen("svtplay-dl " + \
            " -S --remux -o " + self.dl_dir + " " + link)
    def check_process(self):
        if self.process.poll() is None:
            return True
        return False

def submit_button_press(button):
    if button == "Cancel":
        app.stop()
    else:
        link = app.getEntry("Link")
        path = app.getEntry("Output Dir")
        if not path:
            path = default_download_path
        if not link:
            print("No link")
            return
        svpdl.run(link)

class clipboard:
    def __init__(self, app):
        self.last_clip = ""
        self.app = app
        self.urls = get_setting_section_keys("sites")

    def check(self):
        contents = pyperclip.paste()
        if contents != self.last_clip:
            print("got clip: {}".format(contents))
            self.last_clip = contents
            if self.is_valid_url(contents):
                self.app.setEntry("Link", contents)
            else:
                print("Not valid")

    def is_valid_url(self, string):
        for site_string in self.urls:
            for url in site_string:
                if url in string:
                    return True
        return False

app = gui("svtplay-dl GUI", "700x400")
default_download_path = get_setting("paths", "defaultpath")
svpdl = svplay_dl(default_download_path, get_subs=True, remux=True)
clip = clipboard(app)

app.setPadding([20,20])
app.addLabel("title", "svtplay-dl")
app.addLabelEntry("Link")
app.addDirectoryEntry("Output Dir")
app.setEntryDefault("Output Dir", default_download_path)
app.addButtons(["Download", "Cancel"], submit_button_press)
app.registerEvent(clip.check)
app.go()
