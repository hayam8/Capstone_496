import shortcutdatabase
import keyboard
from level import Level

#level params: name, instructions, valid shortcuts, time limit

level1Shortcuts = [shortcutdatabase.openSearch]
level1 = Level("Level 1", "Find and open the Notepad application", level1Shortcuts, 5)

level2Shortcuts = [shortcutdatabase.selectAll, shortcutdatabase.copy, shortcutdatabase.openSearch, shortcutdatabase.paste]
level2 = Level("Level 2", "Copy all the test from the open window and paste it in a notepad document", level2Shortcuts, '5')

level3Shortcuts = [shortcutdatabase.openSearch, shortcutdatabase.openNewWindow, shortcutdatabase.closeTab, shortcutdatabase.openPrivateWindow, shortcutdatabase.moveCursorToURLBar]
level3 = Level("Level 3", "1. Open a Firefox window \n2. Open a new window \n3. Close that window \n4. Open a private window \n5. Navigate to the URL bar \n6. Type in website", level3Shortcuts, 10)


