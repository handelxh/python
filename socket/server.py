import socket
det = ('localhost', 8003)
sock = socket.socket()
sock.bind(det)
sock.listen(5)
connection,address = sock.accept()
while True:
    buf = connection.recv(3)
    if buf == '1':
        connection.send('welcome to server')
    elif buf == 'fuck':
        break
    else:
        connection.send('fuck off')

sock.close()
