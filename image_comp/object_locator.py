import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from . import screenshot_generator


def bpsq_all_out():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/all_out.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.9
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)


	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False
	#for pt in zip(*loc2[::-1]):
	#	cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
	#	print pt[0], pt[1]
	#	
def in_bpsq():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/in_bpsq.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.9
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)


	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False
	
def at_fm():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/at_fm.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.9
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)


	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False
	
def absent_hchs0001():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/hchs0001.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.99
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)

	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False
	
def absent_hchs0002():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/hchs0002.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.99
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)

	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False

def absent_tmp666():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/tmp666.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.99
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)

	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False
	
def absent_ctb666():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/ctb666.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.99
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)

	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False
	
def absent_marvin0318():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('./src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('./src/marvin0318.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.99
	#print(res)
	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)

	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print (pt[0], pt[1])
		return True
	return False


def emergency_detector():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('././src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	template = cv.imread('././src/emergency1.jpg',0)
	w, h = template.shape[::-1]
	#w2, h2 = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.8

	loc = np.where( res >= threshold)
	#loc2 = np.where( res2 >= 0.6)


	for pt in zip(*loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
		#print pt[0], pt[1]
		return True
	return False
	#for pt in zip(*loc2[::-1]):
	#	cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
	#	print pt[0], pt[1]
	#	
	cv.imwrite('res.png',img_rgb)
def lamp_detector():
	screenshot_generator.screenshot()
	
	img_rgb = cv.imread('././src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	lamp = cv.imread('././src/lamp.jpg',0)
	lamp_w, lamp_h = lamp.shape[::-1]
	#w2, h2 = template.shape[::-1]
	lamp_res = cv.matchTemplate(img_gray, lamp, cv.TM_CCOEFF_NORMED)
	#res2 = cv.matchTemplate(img_gray,template2,cv.TM_CCOEFF_NORMED)
	threshold = 0.8

	lamp_loc = np.where( lamp_res >= threshold)
	#loc2 = np.where( res2 >= 0.6)


	for pt in zip(*lamp_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + lamp_w, pt[1] + lamp_h), (0,0,255), 2)
		#print pt[0], pt[1]
		return True
	return False

def char_lamp():
	screenshot_generator.screenshot()
	lamp_position_x = -1
	char_position_x = -1
	
	img_rgb = cv.imread('././src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	lamp = cv.imread('././src/lamp.jpg',0)
	lamp_w, lamp_h = lamp.shape[::-1]
	lamp_res = cv.matchTemplate(img_gray, lamp, cv.TM_CCOEFF_NORMED)
	lamp_threshold = 0.8
	
	lamp_loc = np.where( lamp_res >=lamp_threshold )
	for pt in zip(*lamp_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + lamp_w, pt[1] + lamp_h), (0,0,255), 2)
		lamp_position_x = pt[0]
		break
	
	char_harmed_left = cv.imread('././src/char_harmed_left.jpg',0)
	char_harmed_left_w, char_harmed_left_h = char_harmed_left.shape[::-1]
	char_harmed_left_res = cv.matchTemplate(img_gray, char_harmed_left, cv.TM_CCOEFF_NORMED)
	char_threshold = 0.8
	
	char_harmed_left_loc = np.where( char_harmed_left_res >=char_threshold )
	for pt in zip(*char_harmed_left_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + char_harmed_left_w, pt[1] + char_harmed_left_h), (0,0,255), 2)
		char_position_x = pt[0]
		return lamp_position_x , char_position_x 
	
	char_idle_left = cv.imread('././src/char_idle_left.jpg',0)
	char_idle_left_w, char_idle_left_h = char_idle_left.shape[::-1]
	char_idle_left_res = cv.matchTemplate(img_gray, char_idle_left, cv.TM_CCOEFF_NORMED)
	
	char_idle_left_loc = np.where( char_idle_left_res >=char_threshold )
	for pt in zip(*char_idle_left_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + char_idle_left_w, pt[1] + char_idle_left_h), (0,0,255), 2)
		char_position_x = pt[0]
		return lamp_position_x , char_position_x 
	
	char_harmed_right = cv.imread('././src/char_harmed_right.jpg',0)
	char_harmed_right_w, char_harmed_right_h = char_harmed_right.shape[::-1]
	char_harmed_right_res = cv.matchTemplate(img_gray, char_harmed_right, cv.TM_CCOEFF_NORMED)
	
	char_harmed_right_loc = np.where( char_harmed_right_res >=char_threshold )
	for pt in zip(*char_harmed_right_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + char_harmed_right_w, pt[1] + char_harmed_right_h), (0,0,255), 2)
		char_position_x = pt[0]
		return lamp_position_x , char_position_x 
	
	char_idle_right = cv.imread('././src/char_idle_right.jpg',0)
	char_idle_right_w, char_idle_right_h = char_idle_right.shape[::-1]
	char_idle_right_res = cv.matchTemplate(img_gray, char_idle_right, cv.TM_CCOEFF_NORMED)
	
	char_idle_right_loc = np.where( char_idle_right_res >=char_threshold )
	for pt in zip(*char_idle_right_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + char_idle_right_w, pt[1] + char_idle_right_h), (0,0,255), 2)
		char_position_x = pt[0]
		return lamp_position_x , char_position_x 
		

def at_map_hunt():
	screenshot_generator.screenshot()
	map_hunt_position_x = -1
	
	img_rgb = cv.imread('././src/screenshot.jpg')
	img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
	map_hunt = cv.imread('././src/map_hunt.jpg',0)
	map_hunt_w, map_hunt_h = map_hunt.shape[::-1]
	map_hunt_res = cv.matchTemplate(img_gray, map_hunt, cv.TM_CCOEFF_NORMED)
	map_hunt_threshold = 0.95
	
	map_hunt_loc = np.where( map_hunt_res >=map_hunt_threshold )
	for pt in zip(*map_hunt_loc[::-1]):
		cv.rectangle(img_rgb, pt, (pt[0] + map_hunt_w, pt[1] + map_hunt_h), (0,0,255), 2)
		map_hunt_position_x = pt[0]
		print('at map')
		return True
	print('not at map')
	return False
	
	