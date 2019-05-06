import level, time
#Level Runnable
class LevelRunnable:

    #Attributes
    levelToRun = level
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
        if (self.levelToRun.getName() == "" or self.levelToRun.getIntructions() == "" or self.levelToRun.GetValidShortcuts() == " " or
            self.levelToRun.getNumTargetActions() == 0 or self.levelToRun.getTimeLimit() == 0):

            print("Error, selected level is missing data")
            return False
        #if not missing any data, return true
        return True

    #Begin running level
    def runLevel(self):
        self.isLevelRunning = True
        startTime = time.time() #begin timer

        while self.isLevelRunning == True: #while level not complete
            if (True == True): #this is where the UI listener will be implemented
                self.userInput.append("ctrl+c") #placeholder for testing updating userInput
                self.userActions += 1
                self.isLevelRunning = False #stop level

        endTime = time.time() #end timer
        self.elapsedTime = endTime - startTime #record elapsed time