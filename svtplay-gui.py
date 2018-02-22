# import the library
from appJar import gui
import os

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        link = app.getEntry("Link")
        path = app.getEntry("Output Dir")
        if path is "":
            path = svtplay_path
        print("Link:", link)
        print("Dir: ", path)
        os.system("svtplay-dl " + " -S --remux -o " + path + " " + link)

svtplay_path = "C:\\svtplay-dl\\"

# create a GUI variable called app
app = gui("svtplay-dl GUI", "300x400")
app.setPadding([20,20])

app.addLabel("title", "svtplay-dl")
app.addLabelEntry("Link")
app.addDirectoryEntry("Output Dir")
app.setEntryDefault("Output Dir", svtplay_path)

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.go()
