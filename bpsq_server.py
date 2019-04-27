import socket
import sys
import action_simulator.action_combination as action_combination
import bpsq_mage
import bpsq_bishop

key_dialog = 'd'
key_press_interval = 0.2
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
	data = input(' input anything to get ready ')
	print('3...')
	sys.stdout.flush()
	time.sleep(1)
	print('2...')
	sys.stdout.flush()
	time.sleep(1)
	print('1...')
	sys.stdout.flush()
	time.sleep(1)
	while True:
		# receive data stream. it won't accept data packet greater than 1024 bytes
		#data = conn.recv(1024).decode()
#		if not data:
#			# if data is not received break
#			break
		#print("from connected user: " + str(data))
		#sys.stdout.flush()
		
		#enter
		enter_bpsq()
		time.sleep(2)
		
		#run all
		data = 'start'
		for x in range(0, client_count):
			conn_list[x].send(data.encode())
			
		#run self
		bpsq_mage.run()
		
		#leave all
		data = 'outt'
		for x in range(0, client_count):
			conn_list[x].send(data.encode())
		
		#leave self
		move()
		leave()
		time.sleep(3)
		
	print("EXIT")
	sys.stdout.flush()
	for x in range(0, client_count):
		conn_list[x].close()
		
def enter_bpsq():
	time.sleep(key_press_interval)
    action_combination.press_and_release(key_dialog)
    time.sleep(key_press_interval)
    action_combination.press_and_release('down')
    time.sleep(key_press_interval)
	action_combination.press_and_release('down')
    time.sleep(key_press_interval)
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