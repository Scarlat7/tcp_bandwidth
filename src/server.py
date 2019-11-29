#!/usr/bin/env python

import socket
import argparse
import time as t

def server(port):
	TCP_IP = 'localhost'
	TCP_PORT = port
	BUFFER_SIZE = 100*1024*1024	# 100 MB ==> 100K messages from client
	MB = 2**20

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

		bandwidth = total_recv // ((stop - start)*MB)
		fp.write("{} MB/s\n".format(bandwidth))	