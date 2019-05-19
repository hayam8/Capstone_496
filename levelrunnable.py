from level import Level
from listener.listener import Listener
import time
#Level Runnable
class LevelRunnable:

    #Attributes
    levelToRun = Level
    elapsedTime = 0
    userInput = []
    userActions = 0
    isLevelRunning = False

    #constructor
    def __init__(self,lev):
        self.levelToRun = lev

    #Check level data using input from UI
    #returns
    def checkLevel(self):
        #check to see if selected level is missing any data
        if (self.levelToRun.getName() == "" or self.levelToRun.getInstructions() == "" or self.levelToRun.getValidShortcuts() == " " or
            self.levelToRun.getNumTargetActions() == 0 or self.levelToRun.getTimeLimit() == 0):

            print("Error, selected level is missing data")
            return False
        #if not missing any data, return true
        return True

    #Begin running level
    def runLevel(self):
        #start level
        self.isLevelRunning = True
        startTime = time.time() #begin timer

        #create listener
        listen2Me = Listener('user_output.txt', self.levelToRun.getValidShortcutsList())
        listen2Me.start() #start listening user input and stop when shortcuts are done
        self.isLevelRunning = False

        #end level and record time,  user input, and actions
        endTime = time.time() #end timer
        self.elapsedTime = endTime - startTime #record elapsed time

        self.userInput = listen2Me.getCompletedShortcuts()
        self.userActions = len(listen2Me.completedShortcuts) #listener needs to be changed to count all actions

