import action_simulator.action_combination as action_combination
import time
import random
import image_comp.object_locator as object_locator
## keep pressing space

## begin definition ##
base_interval_move = 2 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60

key_attack = 'space'
key_buff = 'b'
key_movement_skill = 'shift'

class_type = "MAGE"
## endof definition## 
time.sleep(3)



while True:
	action_combination.attack(key_attack, base_interval_move + random.uniform(-0.5, 0.5))
	