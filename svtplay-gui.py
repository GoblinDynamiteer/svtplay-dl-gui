# import the library
from appJar import gui
import os

def press(button):
    if button == "Cancel":
        app.stop()
    else:
        link = app.getEntry("Link")
        path = app.getEntry("Output Dir")
        print("Link:", link)
        print("Dir: ", path)
        os.system("svtplay-dl " + " -S --remux -o " + path + " " + link)

# create a GUI variable called app
app = gui("svtplay-dl GUI", "300x400")
app.setPadding([20,20])
svtplay_path = "C:\\svtplay-dl\\"
# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "svtplay-dl")
#app.setLabelBg("title", "red")
# start the GUI

app.addLabelEntry("Link")

app.addLabel("l1", "Label 1")
app.addDirectoryEntry("Output Dir")
app.setEntryDefault("Output Dir", svtplay_path)
#app.setDirectoryEntryWidth("dirinput", 300)

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)

app.go()
