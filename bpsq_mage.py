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

class_type = "MAGE"
## endof definition## 
def run():
	print('mage run')
	time.sleep(1)
	action_combination.move_with_skill('right', key_movement_skill, 1)
	action_combination.attack('space', 20)
	print('strom done')
	sys.stdout.flush()
	for x in range(0, 4):
		print('loop : ' + str(x))
		sys.stdout.flush()
		action_combination.move_with_skill('left', key_movement_skill, 2)
		action_combination.move_with_skill('right', key_movement_skill, 1)
		action_combination.attack('c', 10)
	action_combination.attack('c', 5)
	#action_combination.attack('c', 60)
	action_combination.press_and_release('f')
	action_combination.press_and_release('f')
	time.sleep(0.5)
	action_combination.attack('t', 2)
	print('mage exit')