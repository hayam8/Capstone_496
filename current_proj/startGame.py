import eel
import shortcutdatabase
from listener import Listener
from levellistener import LevelListener
import leveldatabase

eel.init('web')
shortcut_list = shortcutdatabase.getShortcutDatabaseList()
current_index = -1
level = leveldatabase.level1

@eel.expose
def startGame():
    listener = Listener('user_output.txt', shortcut_list)
    listener.start()
    return getNextLevel()

@eel.expose
def getNextLevel():
    global current_index
    current_index += 1
    current_shortcut = shortcut_list[current_index]
    return current_shortcut.getDescription()

@eel.expose
def getEncyclopedia():
    return shortcutdatabase.getAllShortcutsString()


@eel.expose
def startLevels():
    level_listener = LevelListener('user_output_levels.txt', level)
    level_listener.start()


eel.start('index.html', size=(1000, 550))