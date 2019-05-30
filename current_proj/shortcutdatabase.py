from shortcut import Shortcut
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["shortkeys"]
shortcutDB = db["shortcuts"]


# Shortcuts Database in module

# General shortcuts
selectAll = Shortcut(['Ctrl', 'A'], 'Select all items in a document or window')
copy = Shortcut(['Ctrl', 'C'], 'Copy the selected item')
refreshWindow = Shortcut(['Ctrl', 'R'], 'Refresh the active window')
paste = Shortcut(['Ctrl', 'V'], 'Paste the selected item')
cut = Shortcut(['Ctrl', 'X'], 'Cut the selected item')
redo = Shortcut(['Ctrl', 'Y'], 'Redo an action')
undo = Shortcut(['Ctrl', 'Z'], 'Undo an action')
zoomIn = Shortcut(['Ctrl', '+'], 'Zoom in')
zoomOut = Shortcut(['Ctrl', '-'], 'Zoom out')
cursorToNextWord = Shortcut(['Ctrl', 'Right'], 'Move cursor to the beginning of the next word')
cursorToPreviousWord = Shortcut(['Ctrl', 'Left'], 'Move cursor to the beginning of the previous word')
cursorToNextParagraph = Shortcut(['Ctrl', 'Down'], 'Move cursor to the beginning of the next paragraph')
cursorToPreviousParagraph = Shortcut(['Ctrl', 'Up'], 'Move cursor to the beginning of the previous paragraph')
switchBetweenAllTabs = Shortcut(['Ctrl','Alt', 'Tab'], 'Use the arrow keys to switch between all open apps')
switchTabs = Shortcut(['Alt', 'Tab'], 'Switch between open apps')


# Windows key shortcuts
showOrHideDesktop = Shortcut(['Win','D'], 'Display and hide the desktop')
openFileExplorer = Shortcut(['Win','E'], 'Open File Explorer')
lockPC = Shortcut(['Win','L'], 'Lock your PC or switch people')
minimizeAll = Shortcut(['Win','M'], 'Minimize all windows')
lockOrientation = Shortcut(['Win','O'], 'Lock device orientation')
openRunDialog = Shortcut(['Win','P'], 'Open the Run dialog box')
openSearch = Shortcut(['Win', 'S'], 'Open search charm to search Windows or the web')
cycleThroughTaskbar = Shortcut(['Win','T'], 'Cycle through apps on the taskbar')
cycleThroughNotifications = Shortcut(['Win','V'], 'Cycle through notifications')
cycleThroughRecentApps = Shortcut(['Win','Tab'], 'Cycle through recently used apps (except desktop apps')
cycleThroughRecentAppsReverse = Shortcut(['Win','Shift', 'Tab'], 'Cycle through recently used apps in reverse order (except desktop apps')
maximize = Shortcut(['Win','Up'], 'Maximize the window')
minimize = Shortcut(['Win','Down'], 'Minimize window')
maximizeToLeft = Shortcut(['Win', 'Left'], 'Maximizes current window to left side of screen')
maximizeToRight = Shortcut(['Win', 'Right'], 'Maximizes current window to right side of screen')
stretchWindow = Shortcut(['Win', 'Shift', 'Up'], 'Stretch desktop window to the top and bottom of screen')
switchInputLanguage = Shortcut(['Win', 'Space'], 'Switch input language and keyboard layout')



# File explorer shortcuts

openNewWindow = Shortcut(['Ctrl', 'N'], 'Open a new window')
closeWindow = Shortcut(['Alt', 'F4'], 'Close open window')
closeTab = Shortcut(['Ctrl', 'W'], 'Close current tab')
openPrivateWindow = Shortcut(['Ctrl', 'Shift', 'P'], 'Open a private browser window')
moveCursorToURLBar = Shortcut(['Ctrl', 'E'], 'Move cursor to URL bar and highlight all text in it')

def getShortcutByName(name):
    target = shortcutDB.find_one({"name": name})
    keys = target["keys"]
    description = target["description"]
    shortcut = Shortcut(keys, description)
    return shortcut

def getAllShortcuts():
    #collection = client.db.shortcutDB #mongoDB database collection
    shortcuts = [] #list of shortcuts to be returned
    for entry in shortcutDB.find():
        keys = entry["keys"]
        description = entry["description"]
        shortcutToAdd = Shortcut(keys, description)
        shortcuts.append(shortcutToAdd)
    return shortcuts

def getListOfAllShortcutsString():
    # collection = client.db.shortcutDB #mongoDB database collection
    shortcuts = []  # list of shortcuts to be returned
    for entry in shortcutDB.find():
        keys = entry["keys"]
        description = entry["description"]
        shortcutToAdd = Shortcut(keys, description)
        shortcuts.append(shortcutToAdd.getShortcut())
    return shortcuts

def getListOfShortcuts():
    return __listOfShortcuts

def getAllShortcutsString():
    return __allShortcutsString

__listOfShortcuts = getAllShortcuts()
__allShortcutsString = '\n'.join(getListOfAllShortcutsString())

def getShortcutDatabaseList():
    return __listOfShortcuts

"""
for i in getShortcutDatabaseList():
    print(i.getKeys())

print(len(getShortcutDatabaseList()))
"""
# print(__listOfShortcuts)
# test = getShortcutByName("copy")
# x = shortcutDB.find_one({"name":"copy"})
# print(test)

# print(copy)
# print(moveCursorToURLBar)
# listOfShortcuts = getAllShortcuts()
# print(listOfShortcutsString)
#_listOfShortcuts = getAllShortcuts()
# print('\n'.join(listOfShortcutsString))
# strings = ' '.join(str(listOfShortcuts))
# print(strings)
# print(listOfShortcuts)
# for i in listOfShortcuts:
#    print(i)
# shortcut tests
# selectAll.__description = "nothing"

# print(selectAll.getDescription())
# print(selectAll.__description)



"""
genShortcuts = [
    {"name": "selectAll", "keys": ['Ctrl', 'A'], "description": "Select all items in a document or window"},
    {"name": "copy", "keys": ['Ctrl', 'C'], "description": "Copy the selected item"},
    {"name": "refreshWindow", "keys": ['Ctrl', 'R'], "description": "Refresh the active window"},
    {"name": "paste", "keys": ['Ctrl', 'V'], "description": "Paste the selected item"},
    {"name": "cut", "keys": ['Ctrl', 'X'], "description": "Cut the selected item"},
    {"name": "redo", "keys": ['Ctrl', 'Y'], "description": "Redo an action"},
    {"name": "undo", "keys": ['Ctrl', 'Z'], "description": "Undo an action"},
    {"name": "zoomIn", "keys": ['Ctrl', '+'], "description": "Zoom in"},
    {"name": "zoomOut", "keys": ['Ctrl', '-'], "description": "Zoom out"},
    {"name": "cursorToNextWord", "keys": ['Ctrl', 'Right'], "description": "Move cursor to the beginning of the next word"},
    {"name": "cursorToPreviousWord", "keys": ['Ctrl', 'Left'], "description": "Move cursor to the beginning of the previous word"},
    {"name": "cursorToNextParagraph", "keys": ['Ctrl', 'Down'], "description": "Move cursor to the beginning of the next paragraph"},
    {"name": "cursorToPreviousParagraph", "keys": ['Ctrl', 'Up'], "description": "Move cursor to the beginning of the previous paragraph"},
    {"name": "switchBetweenAllTabs", "keys": ['Ctrl','Alt', 'Tab'], "description": "Use the arrow keys to switch between all open apps"},
    {"name": "switchTabs", "keys": ['Alt', 'Tab'], "description": "Switch between open apps"}
]

winShortcuts = [
    {"name": "showOrHideDesktop", "keys": ['Win','D'], "description":"Display and hide the desktop"},
    {"name": "openFileExplorer", "keys": ['Win','E'], "description": "Open File Explorer"},
    {"name": "lockPC", "keys": ['Win','L'], "description": "Lock your PC or switch people"},
    {"name": "minimizeAll", "keys": ['Win','M'], "description": "Minimize all windows"},
    {"name": "lockOrientation", "keys": ['Win','O'], "description": "Lock device orientation"},
    {"name": "openRunDialog", "keys": ['Win','P'], "description": "Open the Run dialog box"},
    {"name": "openSearch", "keys": ['Win', 'S'], "description": "Open search charm to search Windows or the web"},
    {"name": "cycleThroughTaskbar", "keys": ['Win','T'], "description": "Cycle through apps on the taskbar"},
    {"name": "cycleThroughNotifications", "keys": ['Win','V'], "description": "Cycle through notifications"},
    {"name": "cycleThroughRecentApps", "keys": ['Win','Tab'], "description": "Cycle through recently used apps (except desktop apps"},
    {"name": "cycleThroughRecentAppsReverse", "keys": ['Win','Shift', 'Tab'], "description": "Cycle through recently used apps in reverse order (except desktop apps"},
    {"name": "maximize", "keys": ['Win','Up'], "description": "Maximize the window"},
    {"name": "minimize", "keys": ['Win','Down'], "description": "Minimize window"},
    {"name": "maximizeToLeft", "keys": ['Win', 'Left'], "description": "Maximizes current window to left side of screen"},
    {"name": "maximizeToRight", "keys": ['Win', 'Right'], "description": "Maximizes current window to right side of screen"},
    {"name": "stretchWindow", "keys": ['Win', 'Shift', 'Up'], "description": "Stretch desktop window to the top and bottom of screen"},
    {"name": "switchInputLanguage", "keys": ['Win', 'Space'], "description": "Switch input language and keyboard layout"}
]

fExpShortcuts = [
    {"name": "openNewWindow", "keys": ['Ctrl', 'N'], "description": "Open a new window"},
    {"name": "closeWindow", "keys": ['Alt', 'F4'], "description": "Close open window"},
    {"name": "closeTab", "keys": ['Ctrl', 'W'], "description": "Close current tab"},
    {"name": "openPrivateWindow", "keys": ['Ctrl', 'Shift', 'P'], "description": "Open a private browser window"},
    {"name": "moveCursorToURLBar", "keys": ['Ctrl', 'E'], "description": "Move cursor to URL bar and highlight all text in it"}
]
"""

