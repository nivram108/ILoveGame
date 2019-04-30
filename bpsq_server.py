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
		#leave all
		
		#enter
		print('enter')
		sys.stdout.flush()
		enter_bpsq()
		
		#check in
		while object_locator.in_bpsq() == False:
			#busy
			continue
		
		#run all
		print('start')
		sys.stdout.flush()
		data = 'start'
		for x in range(0, client_count):
			conn_list[x].send(data.encode())
			
		#run self
		print('run')
		sys.stdout.flush()
		action_combination.move_with_skill('right', key_movement_skill, 1)
		action_combination.attack('c', 25)
		for x in range(0, 5):
			action_combination.attack('c', 10)
			action_combination.move_with_skill('left', key_movement_skill, 2)
			action_combination.move_with_skill('right', key_movement_skill, 1)
		
		
		print('out')
		sys.stdout.flush()
		data = 'outt'
		for x in range(0, client_count):
			conn_list[x].send(data.encode())
		
		#leave self
		print('self leave')
		sys.stdout.flush()
		move()
		leave()
		
		time.sleep(10)
		if object_locator.at_fm() == False:
			# self crash or not exit, try exit again
			print('self leave again')
			sys.stdout.flush()
			move()
			leave()
			time.sleep(10)
			
			if object_locator.at_fm() == False:
				data = input(' something went wrong ')
				print('3...')
				sys.stdout.flush()
				time.sleep(1)
				print('2...')
				sys.stdout.flush()
				time.sleep(1)
				print('1...')
				sys.stdout.flush()
				time.sleep(1)
			elif object_locator.bpsq_all_out() == False:
				#someone not exit
				time_intergrate = 0
				if object_locator.absent_hchs0001() == False:
					time.sleep(2.5)
					time_intergrate = time_intergrate + 2.5
					data = 'hchs0001'
					print(data)
					for x in range(0, client_count):
						conn_list[x].send(data.encode())
						
				if object_locator.absent_hchs0002() == False:
					time.sleep(2.5)
					time_intergrate = time_intergrate + 2.5
					data = 'hchs0002'
					print(data)
					for x in range(0, client_count):
						conn_list[x].send(data.encode())
						
				if object_locator.absent_tmp666() == False:
					time.sleep(2.5)
					time_intergrate = time_intergrate + 2.5
					data = 'tmp666'
					print(data)
					for x in range(0, client_count):
						conn_list[x].send(data.encode())
						
				if object_locator.absent_ctb666() == False:
					time.sleep(2.5)
					time_intergrate = time_intergrate + 2.5
					data = 'ctb666'
					print(data)
					for x in range(0, client_count):
						conn_list[x].send(data.encode())
						
				if object_locator.absent_marvin0318() == False:
					time.sleep(2.5)
					time_intergrate = time_intergrate + 2.5
					data = 'marvin0318'
					print(data)
					for x in range(0, client_count):
						conn_list[x].send(data.encode())
				time.sleep(10 + time_intergrate)
				if object_locator.bpsq_all_out() == False:
					data = input(' something went wrong ')
					print('3...')
					sys.stdout.flush()
					time.sleep(1)
					print('2...')
					sys.stdout.flush()
					time.sleep(1)
					print('1...')
					sys.stdout.flush()
					time.sleep(1)
		elif object_locator.bpsq_all_out() == False:
			#someone not exit
			time_intergrate = 0
			if object_locator.absent_hchs0001() == False:
				time.sleep(2.5)
				time_intergrate = time_intergrate + 2.5
				data = 'hchs0001'
				print(data)
				for x in range(0, client_count):
					conn_list[x].send(data.encode())
					
			if object_locator.absent_hchs0002() == False:
				time.sleep(2.5)
				time_intergrate = time_intergrate + 2.5
				data = 'hchs0002'
				print(data)
				for x in range(0, client_count):
					conn_list[x].send(data.encode())
					
			if object_locator.absent_tmp666() == False:
				time.sleep(2.5)
				time_intergrate = time_intergrate + 2.5
				data = 'tmp666'
				print(data)
				for x in range(0, client_count):
					conn_list[x].send(data.encode())
						
			if object_locator.absent_ctb666() == False:
				time.sleep(2.5)
				time_intergrate = time_intergrate + 2.5
				data = 'ctb666'
				print(data)
				for x in range(0, client_count):
					conn_list[x].send(data.encode())
					
			if object_locator.absent_marvin0318() == False:
				time.sleep(2.5)
				time_intergrate = time_intergrate + 2.5
				data = 'marvin0318'
				print(data)
				for x in range(0, client_count):
					conn_list[x].send(data.encode())
			time.sleep(10 + time_intergrate)
			if object_locator.bpsq_all_out() == False:
				data = input(' something went wrong ')
				print('3...')
				sys.stdout.flush()
				time.sleep(1)
				print('2...')
				sys.stdout.flush()
				time.sleep(1)
				print('1...')
				sys.stdout.flush()
				time.sleep(1)
		
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