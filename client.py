import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect(('127.0.0.1',5553))
nickname=input()

def recieve():
    while True:
        try:
            msg=server.recv(1024).decode('utf-8')
            if msg=="Nickname":
                server.send(nickname.encode('utf-8'))
            else:
                print(msg)
        except:
            print("error")
            server.close()
            break
            
def send():
    while True:
        try:
            server.send(f'{nickname}:{input()}'.encode('utf-8'))
        except:
            print("error")
            server.close()
            break

read=threading.Thread(target=recieve)
read.start()
write=threading.Thread(target=send)
write.start()