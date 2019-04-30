from . import single_command
import keyboard
import time
import pyautogui

## begin time interval definition ##
interval_move = 50 # try to move every interval_move second
interval_buff = 180 # try to buff every interval_buff second
interval_pee = 1800

class_type = "MAGE"


## endof time interval definition## 
def press_and_release(key):
	single_command.press_and_release(key)
def jump():
	single_command.press_and_release('alt')
def move(direction, duration):
	single_command.keep_pressing(direction, duration)
	
def move_with_skill(direction, movement_skill_key, duration):
	for i in range(0, duration):
		time.sleep(0.1)
		single_command.press(movement_skill_key + ', ' + direction)
		time.sleep(0.5)
		single_command.press(movement_skill_key)
		single_command.release(direction)
		single_command.release(movement_skill_key)
		single_command.release(movement_skill_key + ', ' + direction)	
def move_with_skill_and_jump(double_jump, jump_or_not, direction, movement_skill_key, duration):
	if jump_or_not:
		duration = duration + 1
	for i in range(0, duration):
		if i == 0 and jump_or_not == True:
			time.sleep(1)
			if double_jump == True:
				jump()
				time.sleep(1.5)
			jump()
			time.sleep(3)
		time.sleep(0.1)
		single_command.press(movement_skill_key + ', ' + direction)
		time.sleep(0.5)
		single_command.press(movement_skill_key)
		single_command.release(direction)
		single_command.release(movement_skill_key)
		single_command.release(movement_skill_key + ', ' + direction)
		
def attack(attack_key, duration):
	single_command.keep_pressing(attack_key, duration)
	
def buff(buff_key):
	single_command.press_and_release(buff_key)
	time.sleep(3)
	single_command.press_and_release('t')
def shuggle():
	dt = 0
	for x in range(0, 100):
		move('left', 0.03)
		move('right', 0.03)

		
def pee(text = "@pee"):
	time.sleep(5)
	single_command.press_and_release('enter')
	#move('left', 0.5)
	#move('left', 1.5)
	#single_command.press_and_release('1')
	single_command.type_message(text)
	single_command.press_and_release('enter')
	single_command.press_and_release('enter')
	move('left', 0.5)
	move('left', 1.5)
	time.sleep(0.5)
	single_command.press_and_release('x')

def exit_game():
	single_command.press_and_release('esc')
	time.sleep(0.5)
	single_command.press('shift, up')
	time.sleep(0.5)
	single_command.release('shift')
	single_command.release('up')
	time.sleep(0.5)
	single_command.press_and_release('enter')

