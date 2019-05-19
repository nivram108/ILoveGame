import action_simulator.action_combination as action_combination
import bpsq_mage
import bpsq_bishop
import bpsq_idle
import time
import random
import socket
import sys
import account_name
## keep pressing space

## begin definition ##
my_name = account_name.my_name
base_interval_move = 0.1 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60
key_cd = 0.1
key_press_interval = 1

key_attack = 'space'
key_dialog = 'd'
key_buff = 't'
key_movement_skill = 'shift'

class_type = 'marvin0318'
## endof definition## 
	

def client_program():
	print(socket.gethostname())
	#host = '10.0.0.164'
	#host = '192.168.91.1'
	#host = '127.0.0.1'
	host = socket.gethostname()
	port = 5010# socket server port number
	#client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
	client_socket = socket.socket()  # instantiate
	print('...instantiate')
	sys.stdout.flush()
	client_socket.connect((host, port))  # connect to the server
	print('...connect to the server')
	sys.stdout.flush()
	#message = input(" -> ")  # take input
	while True:
		#client_socket.send(message.encode())  # send message
		data = client_socket.recv(1024).decode()  # receive response

		print('Received from server: ' + data)  # show in terminal
		if data == 'outt':
			move()
			leave()
	client_socket.close()  # close the connection
	
def move():
	action_combination.move_with_skill('left', key_movement_skill, 5)
	action_combination.move_with_skill('right', 'v', 1)
def leave():
	time.sleep(random.uniform(0, 2.5))
	time.sleep(key_press_interval)
	action_combination.press_and_release(key_dialog)
	time.sleep(key_press_interval)
	action_combination.press_and_release('right')
	time.sleep(key_press_interval)
	action_combination.press_and_release(key_dialog)

if __name__ == '__main__':
	print("run")
	client_program()