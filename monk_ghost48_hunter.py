import action_simulator.action_combination as action_combination
import time
import random
import image_comp.object_locator as object_locator

## begin definition ##
base_interval_move = 2 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60

key_attack = 'space'
key_buff = 'b'
key_movement_skill = 'shift'
key_dialog = 'y'
class_type = "MAGE"
## endof definition## 

def stricted_pee():
	
	while object_locator.at_map_hunt():
	#exit
		action_combination.move_with_skill('left', key_movement_skill, 10)
		action_combination.portal('right', 8)
			
	action_combination.pee()
	while not object_locator.at_map_hunt():
		action_combination.move_with_skill('right', key_movement_skill, 10)	
		action_combination.portal('left', 8)

def emg_dec():
	emergency = object_locator.emergency_detector()
	if emergency :
		action_combination.move_with_skill('left', key_movement_skill, 15)
		flag = False
		while flag == False:
			flag = object_locator.lamp_detector()
			action_combination.move_with_skill('right', key_movement_skill, 1)
		action_combination.move_with_skill('up', key_movement_skill, 1)
		lamp_x = object_locator.char_lamp()[0]
		char_x = object_locator.char_lamp()[1]
		if char_x - lamp_x > 400:
			action_combination.move_with_skill('left', key_movement_skill, 2)
		elif char_x - lamp_x > 200:
			action_combination.move_with_skill('left', key_movement_skill, 1)
		time.sleep(0.5)
		action_combination.buff(key_dialog)
		time.sleep(0.5)
		action_combination.ea()
		
def hunt():
	time.sleep(3)
	action_combination.buff(key_buff)
	action_combination.buff('t')
	while True:
		time_start = time.clock()
		for buff_loop in range(0, 7):
			emg_dec()
			for x in range(0, 7):
				move_up = random.uniform(0, 100)
				action_combination.attack(key_attack, base_interval_move + random.uniform(-0.5, 0.5))
				action_combination.move_with_skill('right', key_movement_skill, 3 + int(random.uniform(-1, 1)))
				if move_up > 85:
					action_combination.move_with_skill('up', key_movement_skill, 2)
				elif move_up > 70:
					action_combination.move_with_skill('up', key_movement_skill, 1)
					
			for x in range(0, 11):
				move_up = random.uniform(0, 100)
				action_combination.attack(key_attack, base_interval_move + random.uniform(-0.5, 0.5))
				action_combination.move_with_skill('left', key_movement_skill, 3 + int(random.uniform(-1, 1)))
				if move_up > 35:
					action_combination.move_with_skill('up', key_movement_skill, 3)
				elif move_up > 20:
					action_combination.move_with_skill('up', key_movement_skill, 2)
			
			while not object_locator.at_map_hunt():
				action_combination.move_with_skill('right', key_movement_skill, 10)	
				action_combination.portal('left', 8)		
				
			action_combination.buff(key_buff)
			action_combination.buff('t')
			time.sleep(5 + random.uniform(-0.5, 0.5))
			
		stricted_pee()

