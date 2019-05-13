import tkinter as tk
from PIL import Image, ImageTk

#Samson Haile
#GUI
#Redesigned GUI, new setup for easier pathing between pages and scalability

LARGE_FONT= ("Verdana", 12)

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
        for F in (StartPage, LevelTest, ResultsTest):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        #has the program render the landing page on start
        self.show_frame(StartPage)

    #Method that swaps between frames
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#Class that renders the landing page        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        #Draws and places the logo
        load = Image.open("logo2.png")
        self.image = ImageTk.PhotoImage(load)
        imagelabel = tk.Label(self, image=self.image)
        imagelabel.place(relx = .37, rely = .1)
                 
        #Create a Tkinter variable 
        tkvar = tk.StringVar(self)

        #Dictionary with options for dropdown menu
        choices = { 'Level 1', 'Level 2', 'Level 3'}
        tkvar.set('Level 1') # set the default option

        #create, place, and label dropdown menu
        popupMenu = tk.OptionMenu(self, tkvar, *choices)
        tk.Label(self, text="Choose a Level!").place(relx = .47, rely = .40)
        popupMenu.place(relx = .47, rely = .45)
        
        
        #creating and placing the start button
        SButton = tk.Button(self,text="Start", command = lambda: controller.show_frame(LevelTest))
        SButton.place(relx =.44, rely=.8975)

        #creating and placing the encyclopedia button
        EButton = tk.Button(self,text="Encylopedia", command = self.encycopen)
        EButton.place(relx=.47, rely=.8975)

        #creating Quit Button
        quitButton = tk.Button(self, text="Quit", command = self.client_exit)
        quitButton.place(relx=.529, rely=.8975)

          
    #Checking for the level
    def LevelCheck(self):
        1+1
        
    #Quit function
    def client_exit(self):
        exit()
        
    #Placeholder stuff for opening encyclopedia
    def encycopen(self):
        text2 = tk.Text(self, height=5, width=50) 
        text2.delete("1.0",tk.END)
        text2.tag_bind('follow', '<1>', lambda e, t=text2: t.insert(END))
        quote = """
        Encyclopedia in Progress
        """
        text2.insert(tk.END, quote, 'color')
        text2.place(relx = .35, rely = .55)

#Test of a level
#and pathing
class LevelTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Creates and places a textbox for users to place
        e = tk.Entry(self)
        e.pack()
        e.focus_set()
        
        Finish = tk.Button(self, text = "Finish!", width = 10, command=lambda: controller.show_frame(ResultsTest))
        Finish.place(relx=.47,rely=.2)

    def callback():
        print (e.get()) 
    


#Test for a results page

class ResultsTest(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #Button to take us back to start
        SButton = tk.Button(self, text = "Back To Start!", width = 10, command=lambda: controller.show_frame(StartPage))
        SButton.place(relx=.5,rely=.2)

        #creating Quit Button
        quitButton = tk.Button(self, text="Quit", command = self.client_exit)
        quitButton.place(relx=.56, rely=.2)

    #Quit function
    def client_exit(self):
        exit()
        
    def callback():
        print (e.get()) 
    

app = GUI()
app.mainloop()
