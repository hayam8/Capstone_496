"""
Initial design for Shortcut class.
This class is a superclass to be used to create any subclasses for specific shortcuts (e.g. Copy, Paste, Cut)
Parameters for creating a Shortcut are a list of Strings corresponding to each key-press and a String description 
for the purpose of the shortcut.

"""
__metaclass__ = type
class Shortcut:

    def __init__(self, keys, description):
        self.keys = keys #list of key values for shortcut
        self.description = description #description of use
        self.hotKey = self.createShortcut() 

    def getKeys(self):
        return self.keys

    def getDescription(self):
        return self.description

    def getHotKey(self):
        return self.hotKey

    """
    This method is used when creating an instance of the Shortcut class. 
    This method takes in 0 parameters and uses information from vars in the instance of the object.
    Precondition: an instance of Shortcut class is created and self.hotKey variable is null
    Postcondition: a String object consisting of all keys for shortcut with '+' separating each key is created 
                    assigned to self.hotKey
    """
    def createShortcut(self):
        shortcutValue = []
        for i in range(len(self.keys)):
            if i != (len(self.keys) - 1):
                shortcutValue.append(self.keys[i] + '+')
            else:
                shortcutValue.append(self.keys[i])
        return ''.join(shortcutValue)


