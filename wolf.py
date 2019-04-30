from pynput.keyboard import Key, Listener, Controller
import action_simulator.action_combination as action_combination
import time
import random
import threading
import sys
key_attack = 'space'
press_interval = 0.03
keyboard = Controller()
flag = False

def flush():
	sys.stdout.flush()
def attack():
	'''global stop_event
	counter = 0
	while not stop_event.is_set():
		print(counter)
		flush
		counter = counter + 1
	'''
	global flag
	while flag == True:
		action_combination.attack(key_attack, 0.1)
		#print('go')
		#flush()
		#time.sleep(0.5)
	#action_combination.press_and_release(key_attack)
	#action_combination.press_and_release(key_attack)
	#keyboard.press_and_release(Key.space)
	#flag = True
	
def on_press(key):
	x = 1
def on_release(key):
	global flag 
	if key == Key.num_lock :
		print('EXIT')
		sys.stdout.flush()
		# Stop listener
		return False
	elif key == Key.caps_lock:
		if flag == False:
			flag = True
			t = threading.Thread(target = attack)
			t.start()
			print('bingo')
			sys.stdout.flush()
		else:
			flag = False
		

# Collect events until released
with Listener(
		on_press=on_press,
		on_release=on_release) as listener:
	listener.join()
	
