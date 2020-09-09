import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 8888

dg=30
# message=b"Hello, World!"
# message=struct.pack('<d',dg)    # 'ieee-754 double' to 'bytes'
message = bytes(str(float(dg)) + ' , 0.0 \n', 'utf-8')


print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % message)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(message, (UDP_IP, UDP_PORT))