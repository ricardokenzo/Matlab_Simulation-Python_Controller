import socket

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 54320)) #connects to the ip running in matlab
print('connection estabilished')

end_of_msg_char = '\n'
flag = ''

while flag != '5':

	for k in range(1):
		#print('input a message to send')
	    message = str(input('input a number from 0 to 100 to send \nwith 5 to close the connection: '))
	    flag = message
	    client_socket.send(message.encode()) #sends the message to the connection
	
	print('message received')
	message = ''
	message = message + end_of_msg_char
	client_socket.send(message.encode()) #sends the message to the connection
print('connection closed')
client_socket.close()  # close the connection


