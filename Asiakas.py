import concurrent.futures
import time
import threading
import socket

HOST = input("IP-Osoite (default: localhost): ")
if HOST == "":
    HOST = 'localhost'
nimi = input("Nimi: ")
PORT = 51525

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try:
        s.connect((HOST,PORT))
        s.send((nimi+";muodosti yhteyden").encode())
        print("Connected")
    except:
        print("Connection could not be made")

    print("Kirjoita viesti tai 'exit' lopettaaksesi palvelun\n")

    def reciever():
        while(True):
            data = s.recv(1024).decode("utf-8")
            data = data.split(';')
            if data[0] != nimi:
                print(data[0]+": " + data[1])
    def viesti():
        while True:
            viesti = input()
            s.send((nimi +';'+ viesti).encode())
            if ("exit" == viesti):
                s.send((nimi + ";poistui paikalta").encode())
                break
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(reciever)
        f2 = executor.submit(viesti)
        f1()
        f2()