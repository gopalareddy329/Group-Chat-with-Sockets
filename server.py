import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostbyname(socket.gethostname())
port=5553
server.bind((host,port))
server.listen()
print("Server is listening: ")
clients=[]
nicknames=[]
def brodcast(messege):
    for client in clients:
        client.send(messege.encode('utf-8'))

def recieve(client):
    while True:
        try:
            msg=client.recv(1024).decode('utf-8')
            brodcast(msg)
        except:
            index=clients.index(client)
            clients.remove(client)
            print(f'{nicknames[index]} is disconnected')
            nick=nicknames[index]
            nicknames.remove(nick)
            client.close()
            break

def join():
    while True:
        client_socket,adre=server.accept()
        clients.append(client_socket)
        client_socket.send("Nickname".encode('utf-8'))
        msg=client_socket.recv(1024).decode('utf-8')
        nicknames.append(msg)
        print(f"{msg} is connected")
        brodcast(f"{msg} is connected")
        thread=threading.Thread(target=recieve,args=(client_socket,))
        thread.start()

join()


            
