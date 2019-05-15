"""
Initial design for Shortcut class.
This class is a superclass to be used to create any subclasses for specific shortcuts (e.g. Copy, Paste, Cut)
Parameters for creating a Shortcut are a list of Strings corresponding to each key-press and a String description 
for the purpose of the shortcut.

"""
__metaclass__ = type
class Shortcut:

    def __init__(self, keys, description):
        self.__keys = keys #list of key values for shortcut
        self.__description = description #description of use
        self.__hotKey = self.createShortcut()

    def getKeysList(self):
        return self.__keys

    def getKeys(self):
        return ' '.join(self.__keys)

    def getDescription(self):
        return self.__description

    def getHotKey(self):
        return self.__hotKey

    """
    This method is used when creating an instance of the Shortcut class. 
    This method takes in 0 parameters and uses information from vars in the instance of the object.
    Precondition: an instance of Shortcut class is created and self.hotKey variable is null
    Postcondition: a String object consisting of all keys for shortcut with '+' separating each key is created 
                    assigned to self.hotKey
    """
    def createShortcut(self):
        shortcutValue = []
        for i in range(len(self.__keys)):
            if i != (len(self.__keys) - 1):
                shortcutValue.append(self.__keys[i] + '+')
            else:
                shortcutValue.append(self.__keys[i])
        return ''.join(shortcutValue)

    def __str__(self):
        return self.getHotKey()