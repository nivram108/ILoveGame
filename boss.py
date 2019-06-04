from pynput.keyboard import Key, Listener, Controller, KeyCode
import action_simulator.action_combination as action_combination
import pyautogui
import ctypes
import time
import random
import threading
import sys
keyboard = Controller()

flag = False
cycle = 20
sleep = 55
size = 0
counter = 0
MAX_SIZE = 7
out_x = 3839
out_y = 1079
xx = [0,0,0,0,0,0,0,0,0]
yy = [0,0,0,0,0,0,0,0,0]
def load(): 
	global xx, yy, size, MAX_SIZE
	size = 5
	xx = [	74,	970,1317,1971,3491,2410,3406,148, 148]
	yy = [1064,1064, 801, 139, 179, 867, 870, 341, 341]
def escape():
	action_combination.single_command.press('ctrl')
	action_combination.single_command.press_and_release('alt')
	action_combination.single_command.release('ctrl')
	time.sleep(0.01)
def flush():
	sys.stdout.flush()
def click():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
def on_press_attack(key):
	a = 0
def on_release_attack(key):
	global flag 
	global xx, yy, size, MAX_SIZE, counter
	if key == Key.f4:
		escape()
		ctypes.windll.user32.SetCursorPos(xx[2],yy[2])
		click()
	elif key == Key.f5:
		escape()
		ctypes.windll.user32.SetCursorPos(xx[3],yy[3])
		click()
	elif key == Key.f6:
		escape()
		ctypes.windll.user32.SetCursorPos(xx[4],yy[4])
		click()
	elif key == Key.f7:
		escape()
		ctypes.windll.user32.SetCursorPos(xx[5],yy[5])
		click()
	elif key == Key.f8:
		escape()
		ctypes.windll.user32.SetCursorPos(xx[6],yy[6])
		click()
	elif key == Key.f9:
		escape()
	elif key == Key.page_down:
		if counter == 4 - 4 :
			escape()
			ctypes.windll.user32.SetCursorPos(xx[2],yy[2])
			click()
			counter = counter + 1
		elif counter == 5 - 4 :
			escape()
			ctypes.windll.user32.SetCursorPos(xx[3],yy[3])
			click()
			counter = counter + 1
		elif counter == 6 - 4 :
			escape()
			ctypes.windll.user32.SetCursorPos(xx[4],yy[4])
			click()
			counter = counter + 1
		elif counter == 7 - 4 :
			escape()
			ctypes.windll.user32.SetCursorPos(xx[5],yy[5])
			click()
			counter = counter + 1
		elif counter == 8 - 4 :
			escape()
			ctypes.windll.user32.SetCursorPos(xx[6],yy[6])
			click()
			counter = counter + 1
		elif counter == 9 - 4 :
			escape()
			ctypes.windll.user32.SetCursorPos(xx[7],yy[7])
			click()
			counter = 0
		
	elif key == Key.f2:
		load()
	elif key == Key.delete:
		if xx[0] > 0:
			ctypes.windll.user32.SetCursorPos(xx[0],yy[0])
			click()
		if xx[1] > 0:
			ctypes.windll.user32.SetCursorPos(xx[1],yy[1])
			click()
	elif key == Key.shift_l:
		xx[size] = pyautogui.position()[0]
		yy[size] = pyautogui.position()[1]
		print (str(size) + " position: " + str(xx[size]) + ", " + str(yy[size]))
		size = size + 1
		if size > MAX_SIZE:
			size = 0
		
		flush()

	
# Collect events until released
with Listener(
		on_press=on_press_attack,
		on_release=on_release_attack) as listener_attack:
	listener_attack.join()

