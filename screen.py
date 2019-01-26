import time
from pynput.keyboard import Key, Controller


keyboard = Controller()

def clearScreen():
	"""
	Simulates the user pressing cmd k to actually clear the screen
	As opposed to printing a new screen so it looks like it cleared
	"""

	keyboard.press(Key.cmd)
	keyboard.press('k')
	keyboard.release('k')
	keyboard.release(Key.cmd)
	time.sleep(0.01)