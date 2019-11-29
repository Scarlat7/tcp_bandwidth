#!/usr/bin/env python
import argparse
from threading import Thread
from server import server
from client import client
from time import sleep

def coordinator(args):
	port = args.port
	threads = []

	for i in range(args.clients,0,-1):
		threads.append(Thread(target = server, args = (port+i)))
		threads.append(Thread(target = server, args = (port+i,i)))

	for i in range(args.clients):
		threads[2*i].start()
		threads[2*i+1].start()
		sleep(1)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Coordinator for bandwidth test.')
	parser.add_argument('-p', '--port', type=int, help='server connection port', required=True)
	parser.add_argument('-c', '--clients', type=int, help='number of parallel connections', required=True)

	args = parser.parse_args()

	server(args)