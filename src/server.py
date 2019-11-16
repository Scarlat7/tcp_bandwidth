#!/usr/bin/env python

import socket
import argparse
import time as t

parser = argparse.ArgumentParser(description='Client for bandwidth test.')
parser.add_argument('-p', '--port', type=int, help='server connection port', required=True)

args = parser.parse_args()

TCP_IP = 'localhost'
TCP_PORT = args.port 
BUFFER_SIZE = 1024

# Creates TCP socket (SOCK_STREAM) with AF_INET address family (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binds this port to the socket
s.bind((TCP_IP, TCP_PORT))

# Start listening through this socket
s.listen(0)	# at most zero queued connections

print("Listening on port {}".format(TCP_PORT))

# Continues indefinitely, use CTRL+C to abort
while(True):
	#NOT_IMPLEMENTED_YET
	pass;