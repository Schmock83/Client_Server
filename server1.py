#!/usr/bin/python3

from os import strerror
from sys import argv
from socket import *

def usage():
    print(f'Wrong Usage: {argv[0]} [port]')

if len(argv) != 2:
    usage()
    exit(1)

#check if port is valid(1-65535)
try:
    port = int(argv[1])
    if not(1 <= port <= 65535):
        raise ValueError
except ValueError:
    print(f'Port \'{argv[1]}\' is not valid(1-65535)')
    exit(3)

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(('localhost', port))
    s.listen()
    try:
        while True:
            con, addr = s.accept()
            with con:
                print(f'Connected to {addr[0]}:{addr[1]}')
                while True:
                    data = con.recv(1024) #?
                    if not data:
                        break
                    else:
                        print(data.decode())
            print(f'Connection to {addr[0]}:{addr[1]} closed by remote host')
    except:
        print('\nBye')
