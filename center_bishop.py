from pynput.keyboard import Key, Listener, Controller, KeyCode
import action_simulator.action_combination as action_combination
import time
import random
import threading
import sys
key_attack = 'space'
press_interval = 0.03
keyboard = Controller()
flag = False
cycle = 90
sleep = 55
cool_down = 0.25
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
	counter = 0
	while flag == True:
		counter = counter + cool_down
		#action_combination.attack(key_attack, 1/30)
		if counter > cycle:
			#break
			counter = 0
			action_combination.press_and_release('t')
			time.sleep(2)
			action_combination.press_and_release('y')
		else:
			action_combination.press_and_release(key_attack)
			time.sleep(cool_down)
		#print('go')
		#flush()
		#time.sleep(0.5)
	#action_combination.press_and_release(key_attack)
	#action_combination.press_and_release(key_attack)
	#keyboard.press_and_release(Key.space)
	#flag = True
	
def on_press_attack(key):
	global flag 
	if key == Key.tab or key == Key.left or key == Key.right or key == KeyCode('x') or key == Key.insert:
		action_combination.set_disable_press()
		flag = False
def on_release_attack(key):
	global flag 
	if key == Key.num_lock :
		print('EXIT')
		sys.stdout.flush()
		# Stop listener
		return False
	elif key == Key.shift_r:
		if flag == False:
			flag = True
			action_combination.set_enable_press()
			t = threading.Thread(target = attack)
			t.start()
			print('>>>>>>>>>>start')
			sys.stdout.flush()
		else:
			flag = False
			print('-----------------------------------------------------------------------------------------------')
			print('pause------------------------------------------------------------------------------------------')
			print('-----------------------------------------------------------------------------------------------')
			sys.stdout.flush()
			action_combination.set_disable_press()

# Collect events until released
with Listener(
		on_press=on_press_attack,
		on_release=on_release_attack) as listener_attack:
	listener_attack.join()
	
