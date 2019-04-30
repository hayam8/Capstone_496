from tkinter import *
from PIL import Image, ImageTk

#GUI
#Currently creates the landing page for our game

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master

    #method to exit the game
    def close_game(self):
        exit()

    #method to start level
    #def startlevel(self):


    #method to open encyclopedia
    #def encycopen(self):
        


        
root = Tk()
root.title("Short Keys")
app = Window(root)
#size of the window
root.state('zoomed')

#creating and placing the start button
SButton = Button(text="Start", command = app.startlevel)
SButton.place(x=root.winfo_screenwidth()/2 - 80, y=root.winfo_screenheight()-100)


#creating and placing the encyclopedia button
EButton = Button(text="Encylopedia", command = app.encycopen)
EButton.place(x=(root.winfo_screenwidth()/2) - 40, y=root.winfo_screenheight()-100)

#creating Quit Button
quitButton = Button(text="Quit", command = app.close_game)
quitButton.place(x=(root.winfo_screenwidth()/2) + 40, y=root.winfo_screenheight()-100)

#loads and places logo
load = Image.open("logo.png")
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.pack()

# Add a grid (for placing purposes)
mainframe = Frame(root)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Level 1', 'Level 2', 'Level 3'}
#tkvar.set() # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a Level!").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)


text2 = Text(root, height=5, width=50)

#Allows us to print description based on which option in the dropdown menu is chosen
def print_descrip(*args):
    if tkvar.get() == "Level 1":
        text2.delete("1.0",END)
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = """
        Placeholder description for Level 1
        """
        text2.insert(END, quote, 'color')
        text2.pack()
    if tkvar.get() == "Level 2":
        text2.delete("1.0",END)
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = """
        Placeholder description for Level 2
        """
        text2.insert(END, quote, 'color')
        text2.pack()
    if tkvar.get() == "Level 3":
        text2.delete("1.0",END)
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = """
        Placeholder description for Level 3
        """
        text2.insert(END, quote, 'color')
        text2.pack()

#Trace function to track with dropdown menu item is selected
tkvar.trace('w', print_descrip)

root.mainloop()  
