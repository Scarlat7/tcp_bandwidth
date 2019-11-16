#!/usr/bin/env python

import socket
import argparse
import time as t


parser = argparse.ArgumentParser(description='Client for bandwidth test.')
parser.add_argument('-p', '--port', type=int, help='server connection port', required=True)
parser.add_argument('-t', '--time', type=int, help='how long the test will run (in seconds)')

args = parser.parse_args()

TCP_IP = 'localhost'
TCP_PORT = args.port 
DEFAULT_TIME = 120
TIME =  DEFAULT_TIME if (args.time == None) else args.time
MESSAGE = "X"*1024

# Creates TCP socket (SOCK_STREAM) with AF_INET address family (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects to the server
s.connect((TCP_IP, TCP_PORT))

print("Connected to server {} on port {}".format(TCP_IP, TCP_PORT))

start = t.time()

while(t.time() - start < TIME):
	
	# Sends 1024 byte message
	s.send(MESSAGE.encode())

# Closes socket
s.close()
