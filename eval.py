import level
#Eval class
class Eval:

    #Attributes
    levelToEval = level
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
        if self.levelToEval.validShortcuts != self.parsedUserInput: #will need some way of checking the user input
            self.score = 0
            return
        else:
            self.score = 1

        #compare number of actions
        if self.numberOfUserActions <= self.levelToEval.getNumTargetActions():
            self.score += 0.5

        #compare time to complete
        if self.levelToEval.getTimeLimit() - 1 < self.userTime <= self.levelToEval.getTimeLimit():
            self.score += 0.5
        elif self.userTime <= self.levelToEval.getTimeLimit() - 2:
            self.score += 1.5

        return self.score