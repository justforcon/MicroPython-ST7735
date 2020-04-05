import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    response = 'test'
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    print(dir(cl))
    try:
        print(cl.readline())
    except OSError as e:
        print(e)
    cl.send(response)
    cl.close()