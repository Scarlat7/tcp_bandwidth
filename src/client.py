#!/usr/bin/env python

import socket
import argparse
import time as t

def client(ip, port, time):
	TCP_IP = ip
	TCP_PORT = port
	MSG_SIZE = 1024
	TIME = time

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
		s.send(b'X'*MSG_SIZE)

	# Closes socket
	s.close()