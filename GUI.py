from tkinter import *
from listener import Listener
import shortcutdatabase

listen = Listener('user_output.txt', [shortcutdatabase.openSearch, shortcutdatabase.maximizeToLeft])

def startListener():
    print('started')
    listen.start()
def stopListener():
    print('stopped')
    listen.stop()
app = Tk()
welcome = Label(app, text="Welcome to Short Keys. Follow these instructions to learn how to test your keyboard knowledge")
welcome.pack()


startButton = Button(app, text="start listener", command=startListener)
startButton.pack()

stopButton = Button(app, text="stop listener", command=stopListener)
stopButton.pack()
app.mainloop()