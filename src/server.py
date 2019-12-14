#!/usr/bin/env python

import socket
import argparse
import time as t

def server(port):
	TCP_IP = 'localhost'
	TCP_PORT = port
	MB = 2**20
	KB = 2**10
	BUFFER_SIZE = 10*KB

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
	fp = open(log_file, 'w')

	start = t.time()
	total_recv = 0

	# Actually continues until no more data is sent through the socket
	while True:

		# Receives message from client
		data = conn.recv(BUFFER_SIZE)
		total_recv += len(data)

		if not data:
			# Closes connection
			conn.close()

			# Closes log file
			fp.close()

			exit(0);

		# Writes bandwidth to log file
		stop = t.time()

		if stop - start >= 1 : # 1 second
			bandwidth = (total_recv*8) // int(((stop - start)*MB)) # 8 for byte->bit conversion
			fp.write("{} Mbit/s\n".format(bandwidth))	

			total_recv = 0
			start = t.time()