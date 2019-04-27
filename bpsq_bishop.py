import action_simulator.action_combination as action_combination
import time
import random
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
	action_combination.attack(key_purify, 75)
	action_combination.attack(key_heal, 15)