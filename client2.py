#!/usr/bin/python3

import argparse
from sys import argv
from ipaddress import IPv6Address, IPv4Address, AddressValueError
from socket import *
from os import strerror

def check_port(val):
    try:
        port = int(val)
        if not(1 <= port <= 65535):
            raise argparse.ArgumentTypeError(f'\'{port}\' is not a valid Port (1-65535')
        return port
    except ValueError:
        raise argparse.ArgumentTypeError(f'\'{val}\' is not a valid Port (1-65535)')


def handle_error(e, alternate_exit_code):
    if hasattr(e, 'errno'):
        print(strerror(e.errno), '\nClosing connection...')
        exit(e.errno)
    else:
        print('\nClosing connection...')
        exit(alternate_exit_code)

parser = argparse.ArgumentParser()
parser.add_argument('port', type=check_port)
parser.add_argument('ip', metavar='IP-Address')
parser.add_argument('-ipv6', action='store_true', help='enable IPv6')
parser.add_argument('-f', nargs='*', metavar='File')

#check for ip
args = parser.parse_args()
try:
    if args.ipv6:
        IPv6Address(args.ip)
    else:
        IPv4Address(args.ip)
except AddressValueError:
    parser.error(f'IP-Address \'{args.ip}\' is not a valid IPv{6 if args.ipv6 else 4}-Address')

try:
    family = AF_INET6 if args.ipv6 else AF_INET
    with socket(family, SOCK_STREAM) as s:
        s.connect((args.ip, args.port))
        inp = "-"
        while inp:
            try:
                inp = input("")
                s.send((inp).encode())
            except BaseException as e:
                handle_error(e, 5)
except ConnectionRefusedError:
    print(f'Connection to {args.ip}:{args.port} was refused')
    exit(4)
