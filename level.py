import shortcutdatabase

#Level class
class Level:

    #constructor
    def __init__(self, name, des, valid, limit):
        self.name = name
        self.instructions = des
        self.validShortcuts = valid
        self.timeLimit = limit
        self.numTargetActions = len(self.validShortcuts)
        #self.targetTime = timeToBeat

    
    def setNumTargetActions(self, shortcuts):
        self.numTargetActions = len(shortcuts)

    def getName(self):
        return self.name

    def getInstructions(self):
        return self.instructions

    def getNumTargetActions(self):
        return self.numTargetActions

    def getTimeLimit(self):
        return self.timeLimit

    def getValidShortcuts(self):
        shortcuts = []
        for i in range(len(self.validShortcuts)):
            shortcuts.append(str(self.validShortcuts[i]))
            if(i != (len(self.validShortcuts) - 1)):
                shortcuts.append("\n")
        return ''.join(shortcuts)

    #display level info
    def display(self):
        print(self.getName(), "\n" + self.getInstructions(),
              "\nGoal Shortcuts: ", "\n" + self.getValidShortcuts(), "\nTarget Number of Actions: ", self.getNumTargetActions(),
              "\nTime Limit: ", self.getTimeLimit(), "sec")

    

    
    def displayLevel(self):
        print(self.getName(), "\n" + self.getInstructions(), 
        "Goal Shortcuts: ", self.getValidShortcuts(), " Target Number of Actions: ", self.getNumTargetActions(),
        " Time Limit: ", self.getTimeLimit(), "sec")