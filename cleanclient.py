import socket
import struct

ip = "localhost"
port = 54320

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client_socket.connect((ip, port)) #connects to the ip running in matlab
#print('connection estabilished')

flag = ''

while flag != '5': 
	message = input()
	#message2 = bytes(str(float(message)) + ', 0.0 \n', 'utf-8')

	message2 = bytes(str(message) + ', 0.0 \n', 'utf-8')

	client_socket.send(message2)
	print('message received')
	flag = message



#	message = input()
#	flag = message
	#message2 = bytes(str(float((message)) + ' , 0.0', 'utf-8')
#	message2 = str(float(message)) + '\n'

	#message = bytes(str(float(dg)) + ' , 0.0 \n', 'utf-8')
		

	#client_socket.sendto(message2, (ip, port))
#	client_socket.send(message2)

	
	#print('message received')
	#message = ''
	#message = message + end_of_msg_char
	#client_socket.send(message.encode()) #sends the message to the connection
print('connection closed')
client_socket.close()


