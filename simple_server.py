import socket
import sys
import action_simulator.action_combination as action_combination
import bpsq_mage
import bpsq_bishop
import time

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
	data = input('input string to start')
	counter = len(data);
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
		if counter == 0:
			data = input('input string to start')
			counter = len(data);
			print('3...')
			sys.stdout.flush()
			time.sleep(1)
			print('2...')
			sys.stdout.flush()
			time.sleep(1)
			print('1...')
			sys.stdout.flush()
			time.sleep(1)
		# receive data stream. it won't accept data packet greater than 1024 bytes
		#data = conn.recv(1024).decode()
#		if not data:
#			# if data is not received break
#			break
		#print("from connected user: " + str(data))
		#sys.stdout.flush()
		#leave all

		#enter
		print('enter')
		sys.stdout.flush()

	print("EXIT")
	sys.stdout.flush()
	for x in range(0, client_count):
		conn_list[x].close()

if __name__ == '__main__':
	server_program()
