import action_simulator.action_combination as action_combination
import time
import random
import image_comp.object_locator as object_locator

## begin definition ##
base_interval_move = 10 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60
mode = 'ninja_hunter'

key_attack = 'space'
key_buff = 'b'
key_movement_skill = 'shift'

class_type = "MAGE"
## endof definition## 
def hunt():
	time.sleep(3)
	duration_right = [3, 3, 2, 5]
	while True:
		time_start = time.clock()
		for buff_loop in range(0, 4):
			for move_loop in range(0, 8):
				
				#attack
				action_combination.attack(key_attack, base_interval_move + random.uniform(-0.5, 0.5))
				#time.sleep(2)
				action_combination.move_with_skill((False), (False), 'left', key_movement_skill, 4)
				action_combination.attack(key_attack, base_interval_move + random.uniform(-0.5, 0.5))
				#time.sleep(2)
				action_combination.move_with_skill((False), (False), 'right', key_movement_skill, 4)
				
			action_combination.buff(key_buff)
			action_combination.pee()
			time.sleep(5 + random.uniform(-0.5, 0.5))
			
		action_combination.pee()
		action_combination.pee("XD")
	