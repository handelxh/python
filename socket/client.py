import socket
import os
sock = socket.socket()
sock.connect(('220.181.111.85',80))
import time
time.sleep(2)
strs=raw_input('input:')
sock.send(strs)
# time.sleep(2)
print sock.recv(1024)
# strs=raw_input('please input')
# sock.send(strs)
# time.sleep(5)

# sock.send('4')
# print sock.recv(1024)
# time.sleep(2)

sock.close()
