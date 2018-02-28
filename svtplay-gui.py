# import the library
from appJar import gui
from config import get_setting
import os

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
        os.system("svtplay-dl " + " -S --remux -o " + path + " " + link)

default_download_path = get_setting("paths", "defaultpath")

app = gui("svtplay-dl GUI", "300x400")
app.setPadding([20,20])
app.addLabel("title", "svtplay-dl")
app.addLabelEntry("Link")
app.addDirectoryEntry("Output Dir")
app.setEntryDefault("Output Dir", default_download_path)
app.addButtons(["Submit", "Cancel"], submit_button_press)
app.go()
