#!/usr/bin/python3.8

import argparse
from socket import *
from os import strerror
import datetime

def check_port(val):
    try:
        port = int(val)
        if not(1 <= port <= 65535):
            raise argparse.ArgumentTypeError(f'\'{port}\' is not a valid Port (1-65535)')
        return port
    except ValueError:
        raise argparse.ArgumentTypeError(f'\'{val}\' is not a valid Port (1-65535)')

def handle_error(e, alternate_exit_code):
    if hasattr(e, 'errno'):
        print(strerror(e.errno), '\nClosing connection...')
        exit(e.errno)
    else:
        print(e)
        print('Closing connection...')
        exit(alternate_exit_code)

def receive_file(file_info, con): #file_info[0] = file_name, file_info[1] = file_size
    print(f'Receiving file: {file_info[0]} - {file_info[1]} Bytes')
    time = datetime.datetime.isoformat(datetime.datetime.now(), sep='_')
    file_name = time + '___' + file_info[0]
    with open(file_name, 'wb') as f:
        print(f'Saving file as: {file_name}')
        f.write(con.recv(int(file_info[1])))


parser = argparse.ArgumentParser()
parser.add_argument('port', type=check_port)
parser.add_argument('-ipv6', action='store_true', help='enable only IPv6')
parser.add_argument('-ipv4', action='store_true', help='enable only IPv4')

args = parser.parse_args()

family = AF_INET if (args.ipv4 and not args.ipv6) else AF_INET6
dualstack = True if not(args.ipv4 ^ args.ipv6) else False

try:
    with create_server(("", args.port), family=family, dualstack_ipv6=dualstack) as s:
        while True:
            con, addr = s.accept()
            with con:
                print(f'\nConnected to {addr[0]}:{addr[1]}')
                while True:
                    data = (con.recv(1024).decode())
                    splitted = data.split('\n')
                    if not data:
                        break
                    elif splitted[0] == 'File_transfer':
                        receive_file(splitted[1:3], con)
                    else:
                        print(data)
                print(f'Connection to {addr[0]}:{addr[1]} closed by remote host')
except error as e:
    handle_error(e, 3)
except KeyboardInterrupt:
    print('\nBye')
    exit(0)
except Exception as e:
    handle_error(e, 6)
