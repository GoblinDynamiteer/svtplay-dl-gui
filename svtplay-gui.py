# import the library
from appJar import gui
from config import get_setting
import subprocess
import os

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
            return
        svpdl.run(link)

default_download_path = get_setting("paths", "defaultpath")
svpdl = svplay_dl(default_download_path, get_subs=True, remux=True)

app = gui("svtplay-dl GUI", "300x400")
app.setPadding([20,20])
app.addLabel("title", "svtplay-dl")
app.addLabelEntry("Link")
app.addDirectoryEntry("Output Dir")
app.setEntryDefault("Output Dir", default_download_path)
app.addButtons(["Submit", "Cancel"], submit_button_press)
app.go()
