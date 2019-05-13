import shortcutdatabase
from level import Level

#level params: name, instructions, valid shortcuts, time limit

level1Description = "Open the Notepad application"
level1Actions = [shortcutdatabase.openSearch, 'n', 'o', 't', 'e','p', 'a', 'd', 'Enter']
level1 = Level("Level 1", level1Description, level1Actions, 5)

level2Description = "Pin the application to the left side of the screen"
level2Shortcuts = [shortcutdatabase.pinLeft]
level2 = Level("Level 2", level2Description, level2Shortcuts, 5)

level3Description = "Copy all the text from the open window \n 2. Paste it in a notepad document"
level3Shortcuts = [shortcutdatabase.selectAll, shortcutdatabase.copy, shortcutdatabase.openSearch, shortcutdatabase.paste]
level3 = Level("Level 3", level3Description, level3Shortcuts, 5)

level4Description = "1. Open a Firefox window \n2. Open a new window \n3. Close that window \n4. Open a private window \n5. Navigate to the URL bar \n6. Go to www.celinedion.com"
level4Shortcuts = [shortcutdatabase.openSearch, shortcutdatabase.openNewWindow, shortcutdatabase.closeTab, shortcutdatabase.openPrivateWindow, shortcutdatabase.moveCursorToURLBar]
level4 = Level("Level 4", level4Description, level4Shortcuts, 5)



"""
level database tests
"""
#print(level1.getValidActions())
#print('Win' in level1.getValidActions())