import action_simulator.action_combination as action_combination
import time
import random
import sys
## keep pressing space

## begin definition ##
base_interval_move = 120 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60

key_attack = 'c'
key_buff = 'b'
key_movement_skill = 'shift'

class_type = "idle"
## endof definition## 
def run():
	print('idle run')
	time.sleep(10)
	action_combination.press_and_release('f')
	action_combination.press_and_release('f')
	time.sleep(0.5)
	action_combination.attack('t', 2)
	print('idle exit')