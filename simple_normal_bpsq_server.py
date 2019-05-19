import socket
import sys
import action_simulator.action_combination as action_combination
import bpsq_mage
import bpsq_bishop
import time
import image_comp.object_locator as object_locator

key_dialog = 'd'
key_movement_skill = 'shift'
key_press_interval = 1
time_delay = 5
MAX_CLIENT_COUNT = 10
conn_list = []# = {}
address_list = []# = {}
def server_program():
	# get the hostname
	host = socket.gethostname()
	port = 5010  # initiate port no above 1024

	server_socket = socket.socket()  # get instance
	# look closely. The bind() function takes tuple as argument
	server_socket.bind((host, port))  # bind host address and port together

	# configure how many client the server can listen simultaneously
	print("client count :")
	sys.stdout.flush()
	client_count = int(input())
	
	server_socket.listen(client_count)
	
	for x in range(0, client_count):
		print("wait for client " + str(x) + "...")
		sys.stdout.flush()
		conn, address = server_socket.accept()
		print("Connection from: " + str(address) + ", " + str(conn))
		conn_list.append(conn)
		address_list.append(address)
		sys.stdout.flush()
	data = ""
	while True:
		data = input(' input anything to get ready ')
		data = 'outt'
		for x in range(0, client_count):
			conn_list[x].send(data.encode())
		
		
	print("EXIT")
	sys.stdout.flush()
	for x in range(0, client_count):
		conn_list[x].close()
		
def enter_bpsq():
	time.sleep(key_press_interval)
	action_combination.press_and_release(key_dialog)
	time.sleep(time_delay)
	action_combination.press_and_release('down')
	time.sleep(key_press_interval)
	action_combination.press_and_release(key_dialog)
	
def move():
	action_combination.move_with_skill('left', key_movement_skill, 5)
	action_combination.move_with_skill('right', 'v', 1)	
def leave():
	time.sleep(key_press_interval)
	action_combination.press_and_release(key_dialog)
	time.sleep(key_press_interval)
	action_combination.press_and_release('right')
	time.sleep(key_press_interval)
	action_combination.press_and_release(key_dialog)
	
if __name__ == '__main__':
	server_program()