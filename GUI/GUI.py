import tkinter as tk
import leveldatabase as lb
import shortcutdatabase as sb
import time
from PIL import Image, ImageTk

#Samson Haile
#GUI
#Redesigned GUI, new setup for easier pathing between pages and scalability

seconds = 0
minutes = 0

LARGE_FONT= ("Verdana", 12)
LevelVar = "Level 1"
#Main frame class on which everything is drawn
class GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #title the frame and set it open in full screen
        tk.Tk.wm_title(self, "Short Keys")
        self.state('zoomed')


        #placing a container for all objects to be placed in        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #Adding frames to a list switch between them
        for F in (startPage, encycOpen, level1Disc, level2Disc, level3Disc, level4Disc, startLevel, resultsTest):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #has the program render the landing page on start
        self.show_frame(startPage)

    #Method that swaps between frames
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.event_generate("<<ShowFrame>>")


#Class that renders the landing page        
class startPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text2 = tk.Text(self, height=5, width=50)
        text2.delete("1.0",tk.END)
        #Draws and places the logo
        load = Image.open("logo.png")
        load = load.resize((474, 191), Image.ANTIALIAS) #The (250, 250) is (height, width)
        self.image = ImageTk.PhotoImage(load)
        imagelabel = tk.Label(self, image=self.image)
        imagelabel.place(relx = .33, rely = .1)
                 
        #Create a Tkinter variable 
        tkvar = tk.StringVar(self)

        #Dictionary with options for dropdown menu
        choices = { 'Level 1', 'Level 2', 'Level 3', 'Level 4'}
        
        #create, place, and label dropdown menu
        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        tk.Label(self, text="Choose a Level!").place(relx = .47, rely = .40)
        popupMenu.place(relx = .47, rely = .45)

        #creating and placing the start button
        SButton = tk.Button(self,text="Start")
        SButton.place(relx =.44, rely=.8975)

        #creating and placing the encyclopedia button
        EButton = tk.Button(self,text="Encylopedia", command = lambda: controller.show_frame(encycOpen))
        EButton.place(relx=.47, rely=.8975)

        #creating Quit Button
        quitButton = tk.Button(self, text="Quit", command = self.clientExit)
        quitButton.place(relx=.529, rely=.8975)
        
        def callback(*args):
            if tkvar.get() == 'Level 1':
                SButton['command'] = lambda: controller.show_frame(level1Disc)    
            if tkvar.get() == 'Level 2':
                SButton['command'] = lambda: controller.show_frame(level2Disc)
            if tkvar.get() == 'Level 3':
                SButton['command'] = lambda: controller.show_frame(level3Disc)
            if tkvar.get() == 'Level 4':
                SButton['command'] = lambda: controller.show_frame(level4Disc)
                
        tkvar.trace('w', callback)
    
  
    #Quit function
    def clientExit(self):
        exit()
        

#Display encyclopedia
class encycOpen(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text2 = tk.Text(self, height=10, width=60) 
        text2.delete("1.0",tk.END)
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = sb.selectAll
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.copy 
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.paste 
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.switchTabs 
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.openSearch 
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.openNewWindow
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.closeTab
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.openPrivateWindow 
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.moveCursorToURLBar
        text2.insert(tk.END, quote, 'color')
        quote = '\n'
        text2.insert(tk.END, quote, 'color')
        quote = sb.pinLeft
        text2.insert(tk.END, quote, 'color')
        text2.place(relx = .35, rely = .55)
        

#Page to display level descriptions
class level1Disc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text2 = tk.Text(self, height=5, width=50)
        text2.delete("1.0",tk.END)

        #creating and placing the start button
        SButton = tk.Button(self,text="Start Level", command = lambda: controller.show_frame(startLevel))
        SButton.place(relx =.44, rely=.8975)
        
        #Button to take us back to start
        BButton = tk.Button(self, text = "Back To Landing Page", command=lambda: controller.show_frame(startPage))
        BButton.place(relx=.5,rely=.8975)
        
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = "Goal: " + lb.level1Description
        text2.insert(tk.END, quote, 'color')
        text2.place(relx = .35, rely = .55)
        
#Page to display level descriptions
class level2Disc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text2 = tk.Text(self, height=5, width=50)
        text2.delete("1.0",tk.END)

        #creating and placing the start button
        SButton = tk.Button(self,text="Start Level", command = lambda: controller.show_frame(startLevel))
        SButton.place(relx =.44, rely=.8975)
        
        #Button to take us back to start
        BButton = tk.Button(self, text = "Back To Landing Page", command=lambda: controller.show_frame(startPage))
        BButton.place(relx=.5,rely=.8975)
        
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = "Goal: " + lb.level2Description
        text2.insert(tk.END, quote, 'color')
        text2.place(relx = .35, rely = .55)
       
class level3Disc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text2 = tk.Text(self, height=5, width=50)
        text2.delete("1.0",tk.END)

        #creating and placing the start button
        SButton = tk.Button(self,text="Start Level", command = lambda: controller.show_frame(startLevel))
        SButton.place(relx =.44, rely=.8975)
        
        #Button to take us back to start
        BButton = tk.Button(self, text = "Back To Landing Page", command=lambda: controller.show_frame(startPage))
        BButton.place(relx=.5,rely=.8975)
        
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = "Goal: " + lb.level3Description
        text2.insert(tk.END, quote, 'color')
        text2.place(relx = .35, rely = .55)
        
class level4Disc(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text2 = tk.Text(self, height=5, width=50)
        text2.delete("1.0",tk.END)

        #creating and placing the start button
        SButton = tk.Button(self,text="Start Level", command = lambda: controller.show_frame(startLevel))
        SButton.place(relx =.44, rely=.8975)
        
        #Button to take us back to start
        BButton = tk.Button(self, text = "Back To Landing Page", command=lambda: controller.show_frame(startPage))
        BButton.place(relx=.5,rely=.8975)
        
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = "Goal: " + lb.level4Description
        text2.insert(tk.END, quote, 'color')
        text2.place(relx = .35, rely = .55)        
#Test of a level
#and pathing
class startLevel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

      

        Finish = tk.Button(self, text = "Finish!", command=lambda: controller.show_frame(resultsTest))
        Finish.place(relx=.47,rely=.2)
        
        self.bind("<<ShowFrame>>", self.on_show_frame)
    def on_show_frame(self, event):
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = tk.StringVar()               
        self.makeWidgets()
        self._start = time.time() - self._elapsedtime
        self.updateTime()
        self._running = 1
        
    def makeWidgets(self):                         
        """ Make the time label. """
        l = tk.Label(self, textvariable=self.timestr)
        self.setTime(self._elapsedtime)
        l.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def updateTime(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self.setTime(self._elapsedtime)
        self._timer = self.after(50, self.updateTime)

    def setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
      
        
    

#Test for a results page

class resultsTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Button to take us back to start
        SButton = tk.Button(self, text = "Back To Start!", command=lambda: controller.show_frame(startPage))
        SButton.place(relx=.5,rely=.2)

        #creating Quit Button
        quitButton = tk.Button(self, text="Quit", command = self.client_exit)
        quitButton.place(relx=.56, rely=.2)

    #Quit function
    def client_exit(self):
        exit()
        

app = GUI()
app.mainloop()
