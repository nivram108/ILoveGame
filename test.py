import action_simulator.action_combination as action_combination
import time
import random
import image_comp.object_locator as object_locator
import sys

key_movement_skill = 'shift'
action_combination.move_with_skill('right', key_movement_skill, 1)
action_combination.attack('c', 25)
for x in range(0, 6):
	print('loop:' + str(x))
	sys.stdout.flush()
	action_combination.attack('c', 10)
	action_combination.move_with_skill('left', key_movement_skill, 3)
	action_combination.move_with_skill('right', key_movement_skill, 1)

action_combination.press_and_release('f')
action_combination.press_and_release('f')
time.sleep(0.5)
action_combination.attack('t', 2)