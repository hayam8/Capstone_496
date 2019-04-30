import time
#Level class
class Level:

    #Attributes
    name = ""
    description = ""

    validShortcuts = []
    goalShortcuts = []

    targetNumActions = 0
    targetTime = 0

    #constructor
    def __init__(self, name, des, valid, goals, targetNumAct, timeToBeat):
        self.name = name
        self.description = des
        self.validShortcuts = valid
        self.goalShortcuts = goals
        self.targetNumActions = targetNumAct
        self.targetTime = timeToBeat
    
    #display level info
    def display(self):
        print(self.name, "\n", self.description, "\n Vailid Shortcuts: \n", self.validShortcuts,
              "\n Goal Shortcuts: \n", self.goalShortcuts, "\n Target Number of Actions: \n", self.targetNumActions,
              "\n Target Time: \n", self.targetTime, "sec")


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
        if (self.levelToRun.name == "" or self.levelToRun.description == "" or self.levelToRun.validShortcuts == False or
            self.levelToRun.goalShortcuts == False or self.levelToRun.targetNumActions == 0 or self.levelToRun.targetTime == 0):

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


#Eval class
class Eval:

    #Attributes
    levelToEval = Level
    parsedUserInput = ""
    numberOfUserActions = 0
    userTime = 0
    score = 0

    #constructor
    def __init__(self, level, userInput, numAct, userTime):
        self.levelToEval = level
        self.parsedUserInput = userInput
        self.numberOfUserActions = numAct
        self.userTime = userTime

    #Display Eval info
    def display(self):
        print(" \n Number of Actions: \n", self.numberOfUserActions, " \n Time to Complete: \n", "%.2f" % self.userTime," \n Your score is: \n", self.score)

    #Generate Evaluation score
    def evaluate(self):
        #check for valid/required actions
        if self.levelToEval.goalShortcuts != self.parsedUserInput or self.levelToEval.validShortcuts != self.parsedUserInput: #will need some way of checking the user input
            self.score = 0
            return
        else:
            self.score = 1

        #compare number of actions
        if self.numberOfUserActions <= self.levelToEval.targetNumActions:
            self.score += 1

        #compare time to complete
        if self.userTime <= self.levelToEval.targetTime:
            self.score += 1

        return


#Tests
#tests for Levels
testLevel1 = Level("Level 1", "The first level", ["ctrl+c"], ["ctrl+c"], 3, 15)
testLevel1.display()
testLevel1.name = "Level 2"
testLevel1.display()

#tests for Level Runnable
testRun1 = LevelRunnable(testLevel1)
if testRun1.checkLevel() == True:
    testRun1.runLevel()
print("%.2f" % testRun1.elapsedTime)

#tests for Eval
testEval1 = Eval(testLevel1, testRun1.userInput, testRun1.userActions, testRun1.elapsedTime)
testEval1.evaluate()
testEval1.display()

