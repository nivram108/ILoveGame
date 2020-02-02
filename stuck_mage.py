import action_simulator.action_combination as action_combination
import time
import random
## keep pressing space

## begin definition ##
base_interval_move = 120 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60

key_attack = 'space'
key_buff = 'b'
key_movement_skill = 'shift'

class_type = "MAGE"
## endof definition## 
time.sleep(3)



while True:
	action_combination.attack(key_attack, base_interval_move + random.uniform(-0.05, 0.05))
	time.sleep(0.5)
	action_combination.buff('t')