import socket

ip = "localhost"
port = 54320

#client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client_socket.connect((ip, port)) #connects to the ip running in matlab
print('connection estabilished')

end_of_msg_char = '\n'
flag = ''

while flag != '5':

	for k in range(1):
		#print('input a message to send')
	    #message = str(input('input a number from 0 to 100 to send \nwith 5 to close the connection: '))
	    #message = input()
	    #flag = message
	    #client_socket.send(message.encode()) #sends the message to the connection

	    #dg = 30
	    message = input()
	    flag = message
	    message2 = bytes(str(message) + ' , 0.0 \n', 'utf-8')

		
		#client_socket.sendto(message, (ip, port))
	client_socket.sendto(message2, (ip, port))
	
	print('message received')
	message = ''
	message = message + end_of_msg_char
	client_socket.send(message.encode()) #sends the message to the connection
print('connection closed')
client_socket.close()  # close the connection


# message=b"Hello, World!"
# message=struct.pack('<d',dg)    # 'ieee-754 double' to 'bytes'
