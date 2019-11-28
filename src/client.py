#!/usr/bin/env python

import socket
import argparse
import time as t

def client(args):
	MEGA = 2**20
	TCP_IP = 'localhost'
	TCP_PORT = args.port 
	DEFAULT_TIME = 120
	MSG_SIZE = 1024
	TIME =  DEFAULT_TIME if (args.time == None) else args.time

	# Creates TCP socket (SOCK_STREAM) with AF_INET address family (host, port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connects to the server
	s.connect((TCP_IP, TCP_PORT))

	print("Connected to server {} on port {}".format(TCP_IP, TCP_PORT))

	start = t.time()
	data_sent = 0

	while(t.time() - start < TIME):

		start_inst = t.time()

		# Sends 1024-byte message
		s.send(b'X'*MSG_SIZE);

	# Closes socket
	s.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Client for bandwidth test.')
	parser.add_argument('-p', '--port', type=int, help='server connection port', required=True)
	parser.add_argument('-t', '--time', type=int, help='how long the test will run (in seconds)')

	args = parser.parse_args()

	client(args)