#!/usr/bin/env python

import socket
import argparse
import time as t


def server(args):
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

	# Accepts a connection request
	conn, addr = s.accept()

	print("Connection accepted with address {}".format(addr))

	# Actually continues until no more data is sent through the socket
	while True:

		# Receives message from client
		data = conn.recv(BUFFER_SIZE)

		if !data:
			# Closes connection
			conn.close()

			exit(0);

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Client for bandwidth test.')
	parser.add_argument('-p', '--port', type=int, help='server connection port', required=True)
	parser.add_argument('-c', '--clients', type=int, help='number of parallel connections', required=True)

	args = parser.parse_args()

	server(args)