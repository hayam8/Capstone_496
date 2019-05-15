from shortcut import Shortcut
"""
List of shortcut objects
"""



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



#File explorer shortcuts
openNewWindow = Shortcut(['Ctrl', 'N'], 'Open a new window')
closeTab = Shortcut(['Ctrl', 'W'], 'Close current tab')
openPrivateWindow = Shortcut(['Ctrl', 'Shift', 'P'], 'Open a private browser window')
moveCursorToURLBar = Shortcut(['Ctrl', 'E'], 'Move cursor to URL bar and highlight all text in it')




#shortcut tests
#selectAll.__description = "nothing"

#print(selectAll.getDescription())
#print(selectAll.__description)


