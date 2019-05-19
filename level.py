import shortcutdatabase
from shortcut import Shortcut

"""
The level class takes in a string name for variable, string description for what user should do, list of valid actions
that can be taken by user, and a time limit for how long the level can last
"""
class Level:

    #constructor
    def __init__(self, name, des, actions, limit):
        self.name = name
        self.instructions = des
        self.validShortcuts = []
        self.validActions = actions
        self.timeLimit = limit
        self.numTargetActions = len(self.validShortcuts)
        self.setValidShortcuts(actions)
    
    def setNumTargetActions(self, shortcuts):
        self.numTargetActions = len(shortcuts)

    def setValidShortcuts(self, input):
        shortcuts = []
        for i in input:
            if isinstance(i, Shortcut):
                shortcuts.append(i)
        self.validShortcuts = shortcuts

    def getName(self):
        return self.name

    def getInstructions(self):
        return self.instructions

    def getValidShortcuts(self):
        return self.validShortcuts

    def getValidActions(self):
        actions = []
        for i in self.validActions:
            if isinstance(i, Shortcut):
               actions.append(i.getKeys())
            else:
                actions.append(i)
        return actions

    def getTimeLimit(self):
        return self.timeLimit

    def getNumTargetActions(self):
        return self.numTargetActions

    #display level info
    def display(self):
        print(self.getName(), "\n" + self.getInstructions(),
              "\nGoal Shortcuts: ", "\n" + self.getValidShortcuts(), "\nTarget Number of Actions: ", self.getNumTargetActions(),
              "\nTime Limit: ", self.getTimeLimit(), "sec")

    

    
    def displayLevel(self):
        print(self.getName(), "\n" + self.getInstructions(), 
        "Goal Shortcuts: ", self.getValidShortcuts(), " Target Number of Actions: ", self.getNumTargetActions(),
        " Time Limit: ", self.getTimeLimit(), "sec")