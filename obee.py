import socket

# create server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((localhost, 25572))
# open file for log
f = open('log', 'a')

# continue to listen
s.listen(5)

while True:
    # connection made
    c, addr = s.accept()

    # get and print data
    print('connected')
    data = c.recv(1024)
    if not data:
        print('ended')
        break
    
    # after connection log data
    f.write(data)

    # close connection
    c.close()
s.close()