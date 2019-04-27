import action_simulator.action_combination as action_combination
import time
import random
import socket
import sys
## keep pressing space

## begin definition ##
my_name = 'sage'
base_interval_move = 0.1 # try to move every interval_move second
base_interval_buff = 180 # try to buff every interval_buff second
base_interval_pee = 60
key_cd = 0.1
key_press_interval = 0.02

key_attack = 'space'
key_dialog = 'd'
key_buff = 't'
key_movement_skill = 'shift'

class_type = "MAGE"
## endof definition## 


def client_program():
    print(socket.gethostname())
    #host = '10.0.0.164'
    host = '10.0.0.225'
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
        if data == 'outt' or data == my_name:
            move()
            leave()
        elif data == 'mov':
            move()
        elif data == 'out':
            leave()
        sys.stdout.flush()
        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection
    
def heal():
    action_combination.attack('d', key_press_interval)
def move():
    action_combination.move_with_skill((False), (False), 'left', key_movement_skill, 5)
    action_combination.move_with_skill((False), (False), 'right', 'v', 1)
def leave():

    time.sleep(0.2)
    action_combination.attack(key_dialog, key_press_interval)
    time.sleep(0.2)
    action_combination.attack('right', key_press_interval)
    time.sleep(0.2)
    action_combination.attack(key_dialog, key_press_interval)

if __name__ == '__main__':
    print("run")
    client_program()