
import socket



server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 54320))

#s.listen(5)
print('Server On\n')

flag = ''

#while True:
while flag != '5':
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, (conn_host, conn_port) = server_socket.accept()  # accept new connection
    print("Connection from: " + str(conn_host) + str(conn_port))
    #while True:

    
    while flag != '5':
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        flag = data


        if not data:
            # if data is not received break
            break

        print("from connected user: " + str(data))
        #data = input(' -> ')
        #conn.send(data.encode())  # send data to the client
        
#         # push data to arduino via serial
#         to_arduino = str(data)
#         to_arduino = to_arduino.encode("utf-8")
#         arduino.write(to_arduino)
            
        

conn.close()  # close the connection

