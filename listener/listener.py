from pynput import keyboard
from transitions import Machine
import logging
import shortcutdatabase
import shortcut
from shortcut import Shortcut

"""
Listener object has a start and stop method that controls when the listener is active. It will append any key that is
being held down to a list for held down keys and when the key is released the list is appended to an output file.
Normal character keys are written as they appear and special keys are parsed to their string representation for smoother
reading. 
"""
class Listener():
	"""
	Dictionary with Key codes from keyboard library representing various buttons that may not correspond to letters
	Includes modifier keys and function keys
	Dictionary with Key code keys and parsed string values to convert key codes to readable values
	class pynput.keyboard.Key[source] (Key) : String (value)
	"""
	__keyDic = {
		keyboard.Key.alt: 'Alt',
		keyboard.Key.alt_gr: 'Alt',
		keyboard.Key.alt_l: 'Alt',
		keyboard.Key.alt_r: 'Alt',
		keyboard.Key.backspace: 'Backspace',
		keyboard.Key.caps_lock: 'CapsLk',
		keyboard.Key.cmd: 'Win',
		keyboard.Key.cmd_l: 'Win',
		keyboard.Key.cmd_r: 'Win',
		keyboard.Key.ctrl: 'Ctrl',
		keyboard.Key.ctrl_l: 'Ctrl',
		keyboard.Key.ctrl_r: 'Ctrl',
		keyboard.Key.delete: 'Delete',
		keyboard.Key.down: 'Down',
		keyboard.Key.end: 'End',
		keyboard.Key.enter: 'Enter',
		keyboard.Key.esc: 'Esc',
		keyboard.Key.f1: 'F1',
		keyboard.Key.f2: 'F2',
		keyboard.Key.f3: 'F3',
		keyboard.Key.f4: 'F4',
		keyboard.Key.f5: 'F5',
		keyboard.Key.f6: 'F6',
		keyboard.Key.f7: 'F7',
		keyboard.Key.f8: 'F8',
		keyboard.Key.f9: 'F9',
		keyboard.Key.f10: 'F10',
		keyboard.Key.f11: 'F11',
		keyboard.Key.f12: 'F12',
		keyboard.Key.home: 'Home',
		keyboard.Key.insert: 'Insert',
		keyboard.Key.left: 'Left',
		keyboard.Key.menu: 'Menu',
		keyboard.Key.num_lock: 'NumLock',
		keyboard.Key.page_down: 'PgDn',
		keyboard.Key.page_up: 'PgUp',
		keyboard.Key.pause: 'Pause',
		keyboard.Key.print_screen: 'PrtSc',
		keyboard.Key.right: 'Right',
		keyboard.Key.scroll_lock: 'SclLck',
		keyboard.Key.shift: 'Shift',
		keyboard.Key.shift_l: 'Shift',
		keyboard.Key.shift_r: 'Shift',
		keyboard.Key.space: 'Space',
		keyboard.Key.tab: 'Tab',
		keyboard.Key.up: 'Up'
		}

	def __init__(self, file, validKeys):
		#configuring format to log time of completion for shortcuts
		logging.basicConfig(filename = file, filemode = 'w+', level=logging.DEBUG, format = '%(asctime)s: %(message)s')
		self.validShortcuts = validKeys
		self.currentShortcut = 0
		self.totalShortcuts = len(validKeys)
		self.__pressed = []
		self.completedShortcuts = [] #list of completed shortcuts by user

	"""
	Writes to output file
	"""
	def writeToFile(self, key):
		self.output.write(key)

	"""
	When keyboard key is pressed the key is parsed to either the corresponding char value or String value of key 
	taken from keyDic and written to output file
	"""
	def on_press(self, key):
		try:
			# alphanumeric key
			self.__pressed.append(key.char.upper())
		except AttributeError:
			# special key
			self.__pressed.append(self.__keyDic.get(key))

	"""
	When keyboard key is released the key is parsed to either the corresponding char value or String value of key 
	taken from keyDic and written to output file
	"""
	def on_release(self, key):
		if(key == keyboard.Key.esc): # Stops listener
			return self.stop()

		try:
			# check to see if the current list of held down keys match the keys required for the current shortcut
			if (self.checkCompletedCurrentShortcut(self.__pressed, self.validShortcuts[self.currentShortcut].getKeys())):
				self.__pressed = list(
					dict.fromkeys(self.__pressed))  # removes duplicate keys added from being pressed down from list
				keys = str(' '.join(self.__pressed))  # convert list to string

				logging.info(keys)  # log the completed shortcut to file with timestamp

				self.completedShortcuts.append(self.validShortcuts[self.currentShortcut])
				self.currentShortcut += 1
		except AttributeError:
			if(self.checkCompletedCurrentShortcut(self.__pressed, self.validShortcuts[self.currentShortcut])):
				self.__pressed = list(
					dict.fromkeys(self.__pressed))  # removes duplicate keys added from being pressed down from list
				keys = str(' '.join(self.__pressed))  # convert list to string

				logging.info(keys)  # log the completed shortcut to file with timestamp

				self.completedShortcuts.append(self.validShortcuts[self.currentShortcut])
				self.currentShortcut += 1

		self.__pressed = []	# clear current pressed keys
		if(self.checkCompleted()):#stops listening once shortcuts have been completed
			return self.stop()

	"""
	Method that takes the list of current pressed keys as a list and compares it to the current pending shortcut task
	If keys match, shortcut is marked as complete and increment to next shortcut to complete
	"""
	def checkCompletedCurrentShortcut(self, currentKeys, shortcutToMatchKeys):
		return currentKeys == shortcutToMatchKeys

	"""
	This method is used while the listener is active after start() has been called.

	"""
	def updateTasks(self):
		return

	"""
	Method to start the Listener
	"""
	def start(self):
		with keyboard.Listener(on_press = self.on_press, on_release = self.on_release) as listener:
			listener.join()

	"""
	Method that stops the listener once it has been started
	"""
	def stop(self):
		return False

	"""
	Getter method to access list of completed shortcuts
	"""
	def getCompletedShortcuts(self):
		return self.completedShortcuts

	"""
	Method to check if tasks have been completed by comparing the total number of valid shortcuts to the number
	of shortcuts completed
	"""
	def checkCompleted(self):
		return self.currentShortcut == self.totalShortcuts






"""
listener tests
"""
#listen = Listener('user_output.txt', [shortcutdatabase.openSearch, shortcutdatabase.maximizeToLeft])
#listen.start()
