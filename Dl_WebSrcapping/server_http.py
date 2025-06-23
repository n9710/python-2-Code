from socket import *
def createServer():
    serversocket = socket()
    serversocket.bind(('localhost',9000))
    serversocket.listen()
    while(1):
        (clientsocket, address) = serversocket.accept()
        
        rd = clientsocket.recv(5000).decode()
        print(rd)
        
        data = "HTTP/1.1 200 OK\r\n"
        data += "Content-Type: text/html; charset=utf-8\r\n"
        data += "\r\n"
        data += "<html><body>Hello World</body></html>\r\n\r\n"
        clientsocket.send(data.encode())
    serversocket.close()
print('Access http://localhost:9000')
createServer()
