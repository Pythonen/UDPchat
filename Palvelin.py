import socket
import time

HOST = 'localhost' 
PORT = 51525
asiakkaat = []

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

s.bind((HOST, PORT))

while(True):
    MSGnADR = s.recvfrom(1024)
    usernmsg = MSGnADR[0].decode('utf-8').split(';')
    user=usernmsg[0]
    msg=usernmsg[1]
    
    address = MSGnADR[1]
    if address not in asiakkaat:
        asiakkaat.append(address)
    print(asiakkaat)

    reply = f"{user};{msg}"
    
    print(time.strftime("%X %x") + " "+user + " {}".format(msg))

    for i in asiakkaat:
        s.sendto(reply.encode(), i)