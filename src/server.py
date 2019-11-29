#!/usr/bin/env python

import socket
import argparse
import time as t

def server(port):
	TCP_IP = 'localhost'
	TCP_PORT = args.port 
	BUFFER_SIZE = 1024*1024	# 1 MB ==> 1024 messages from client

	# Creates TCP socket (SOCK_STREAM) with AF_INET address family (host, port)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Binds this port to the socket
	s.bind((TCP_IP, TCP_PORT))

	# Start listening through this socket
	s.listen(0)	# at most zero queued connections

	print("Listening on port {}".format(TCP_PORT))

	# Accepts a connection request
	conn, addr = s.accept()

	print("Connection accepted with address {}".format(addr))

	# Log file name 
	log_file = 'tcp_bandwidth_port_{}.log'.format(port)
	fp = open(log_file, 'a')

	total_data = 0
	start = time()

	# Actually continues until no more data is sent through the socket
	while True:

		# Receives message from client
		data = conn.recv(BUFFER_SIZE)
		total_data += data

		if !data:
			# Closes connection
			conn.close()

			# Closes log file
			fp.close()

			exit(0);

		# Writes bandwidth to log file
		stop = time()
		bandwidth = total_data // (stop - start)
		fp.write("{} B/s".format(bandwidth))