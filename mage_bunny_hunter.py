import action_simulator.action_combination as action_combination
import time
import random

## begin definition ##
base_interval_move = 0.5 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60
mode = 'bunny_hunter'
key_attack = 'space'
key_buff = 't'
key_movement_skill = 'shift'

class_type = "MAGE"
## endof definition## 

time.sleep(3)
duration_right = [3, 3, 3, 4, 1]
skill_wait = 1.5
while True:
	time_start = time.clock()
	for buff_loop in range(0, 5):
		for move_loop in range(0, 8):
			
			#attack
			for x in range(0,5):
				if x != 0 and x != 4:
					action_combination.attack(key_attack, base_interval_move + random.uniform(-0.05, 0))
					time.sleep(skill_wait)
				if x != 3:
					action_combination.move_with_skill((False), (False), 'left', key_movement_skill, 3)
				elif x == 4:
					action_combination.move_with_skill((False), (False), 'left', key_movement_skill, 3)
				else:
					action_combination.move_with_skill((False), (False), 'left', key_movement_skill, 5)
			
			for x in range(0,4):
				if x != 0:
					action_combination.attack(key_attack, base_interval_move + random.uniform(-0.05, 0))
					time.sleep(skill_wait)
				if x != 3:
					action_combination.move_with_skill((move_loop % 2 == 0), (x == 1 or x == 3), 'right', key_movement_skill, duration_right[x])
					#action_combination.move_with_skill(False, False, 'right', key_movement_skill, duration_right[x])
				else:
					action_combination.move_with_skill((move_loop % 2 == 0), (x == 1 or x == 3), 'right', key_movement_skill, duration_right[x])
					#action_combination.move_with_skill(False, False, 'right', key_movement_skill, duration_right[x])
				
		action_combination.buff(key_buff)
		time.sleep(2 + random.uniform(-0.5, 0.5))
		action_combination.buff('f')
	