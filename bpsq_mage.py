import action_simulator.action_combination as action_combination
import time
import random
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
	action_combination.move_with_skill('right', key_movement_skill, 1)
	action_combination.attack(key_attack, 90)