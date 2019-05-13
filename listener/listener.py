from pynput import keyboard
"""
Listener object has a start and stop method that controls when the listener is active. It will append any key that is
being held down to a list for held down keys and when the key is released the list is appended to an output file.
Normal character keys are written as they appear and special keys are parsed to their string representation for smoother
reading. 
"""
class Listener():

	def __init__(self):
		self.output = open('user_output.txt', 'w+')
		"""Dictionary with Key codes from keyboard library representing various buttons that may not correspond to letters
		Includes modifier keys and function keys
		Dictionary with Key code keys and parsed string values to convert key codes to readable values
		class pynput.keyboard.Key[source] (Key) : String (value)
		"""
		self.keyDic = {
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
			keyboard.Key.home: 'Home',
			keyboard.Key.insert : 'Insert',
			keyboard.Key.left : 'Left',
			keyboard.Key.menu : 'Menu',
			keyboard.Key.num_lock : 'NumLock',
			keyboard.Key.page_down : 'PgDn',
			keyboard.Key.page_up : 'PgUp',
			keyboard.Key.pause : 'Pause',
			keyboard.Key.print_screen : 'PrtSc',
			keyboard.Key.right : 'Right',
			keyboard.Key.scroll_lock : 'SclLck',
			keyboard.Key.shift : 'Shift',
			keyboard.Key.shift_l : 'Shift',
			keyboard.Key.shift_r : 'Shift',
			keyboard.Key.space : 'Space',
			keyboard.Key.tab : 'Tab',
			keyboard.Key.up : 'Up'
		}

		self.__pressed = []

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
			self.__pressed.append(self.keyDic.get(key))

	"""
	When keyboard key is released the key is parsed to either the corresponding char value or String value of key 
	taken from keyDic and written to output file
	"""
	def on_release(self, key):
		# Stops listener
		if(key == keyboard.Key.esc):
			return False
		#removes duplicate keys added from being pressed down from list
		self.__pressed = list(dict.fromkeys(self.__pressed))
		#write list of current pressed keys to file as string
		self.writeToFile(' '.join(self.__pressed))
		self.writeToFile('\n')
		#unpopulate current pressed keys
		self.__pressed = []

	"""
	Method to start the Listener
	"""
	def start(self):
		with keyboard.Listener(on_press = self.on_press, on_release = self.on_release) as listener:
			listener.join()

	def stop(self):
		return False


listen = Listener()
listen.start()