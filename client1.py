#!/usr/bin/python3

from os import strerror
from sys import argv
from ipaddress import IPv4Address, IPv6Address, AddressValueError
from socket import *

def usage():
    print(f'Wrong Usasge: {argv[0]} [server addr] [port]')

if len(argv) != 3:
    usage()
    exit(1)

#check if IP4Adress is valid
try:
    IPv4Address(argv[1])
except AddressValueError:
    print(f'IP-Address \'{argv[1]}\' is not a valid IPv4-Address')
    exit(2)
#check if port is valid(1 - 65535
try:
    port = int(argv[2])
    if not(1 <= port <= 65535):
        raise ValueError
except ValueError:
    print(f'Port \'{argv[2]}\' is not valid(1-65535)')
    exit(3)
try:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((argv[1], port))
        inp = "-"
        while inp:
            try:
                inp = input("")
                s.send((inp).encode())
            except BaseException as e:
                if hasattr(e, 'errno'):
                    print(strerror(e.errno), '\nClosing connection...')
                    exit(e.errno)
                else:
                    print('\nClosing connection...')
                    exit(5)

except ConnectionRefusedError:
    print(f'Connection to {argv[1]}:{argv[2]} was refused')
    exit(4)
