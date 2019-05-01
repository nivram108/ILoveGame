import pyautogui
import keyboard
import time
import threading
import sys
## begin define const
enable = True
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


def keep_pressing_key(key):
	global enable
	while enable == True :
		keyboard.press_and_release(key)
		time.sleep(1.0 / const_keep_pressing_freq)
	
	#print('stop pressing')
	#sys.stdout.flush()

def set_disable_press():
	global enable
	enable = False
	#print('disable')
	#sys.stdout.flush()

def set_enable_press():
	global enable
	enable = True	

def keep_pressing(key, duration):
	"""	Emulate pressing a key for a time 
	"""
	global enable
	if enable == False:
		return
	#enable = True
	t = threading.Thread(target = keep_pressing_key, args = [key])
	#print('START pressing')
	#sys.stdout.flush()
	t.start()
	timer = threading.Timer(duration, set_disable_press)
	timer.start()
	time.sleep(duration)
	enable = True
	#stop_pressing_key()
	#global enable
	
	#timer.cancel()
	#t.join()
	
	

	
