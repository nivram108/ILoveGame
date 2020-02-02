import action_simulator.action_combination as action_combination
import time
import random
import sys
## keep pressing space

## begin definition ##
base_interval_move = 120 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60

key_heal = 'x'
key_purify = 'a'
key_buff = 'b'
key_movement_skill = 'shift'

class_type = "bishop"
## endof definition## 

def run():
	print('bishop run')
	sys.stdout.flush()
	for x in range(0, 5):
		print('loop : ' + str(x))
		sys.stdout.flush()
		action_combination.attack(key_purify, 10)
		time.sleep(0.2)
		action_combination.move_with_skill('left', key_movement_skill, 2)
		action_combination.move_with_skill('right', key_movement_skill, 1)
	action_combination.attack(key_heal, 15)
	action_combination.attack('t', 2)
	print('bishop exit')
	sys.stdout.flush()