import pyautogui
import keyboard
import time
from threading import Timer

## begin define const

const_keep_pressing_freq = 30  	# 30 input per second

## endof define const
		
def press(key):
	keyboard.press(key)
	
def release(key):
	keyboard.release(key)
	
def press_and_release(key):
	keyboard.press_and_release(key)


def type_message(string):
	"""	Type a text
	"""
	
	for character in string:
		if character.isalpha():
			press_and_release(character)
		else :
			press('shift')
			press_and_release(character)
			release('shift')

			
def keep_pressing(key, duration):
	"""	Emulate pressing a key for a time 
	"""
	
	dt = 0
	while dt < duration :
		time.sleep(1.0 / const_keep_pressing_freq)
		dt = dt + (1.0 / const_keep_pressing_freq)
		keyboard.press_and_release(key)

	
