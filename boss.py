from pynput.keyboard import Key, Listener, Controller, KeyCode
import pyautogui
import time
import random
import threading
import sys
keyboard = Controller()

flag = False
cycle = 20
sleep = 55
size = 0
MAX_SIZE = 1
xx = [0,0,0,0,0,0,0,0,0]
yy = [0,0,0,0,0,0,0,0,0]
def flush():
	sys.stdout.flush()

def on_press_attack(key):
	a = 0
def on_release_attack(key):
	global flag 
	global xx, yy, size, MAX_SIZE
	if key == Key.delete:
		index = 0
		while index <= MAX_SIZE:
			if xx[index] > 0 :
				pyautogui.click(x=xx[index], y = yy[index])
			index = index + 1
	elif key == Key.f1:
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

