#!/usr/bin/env python
import argparse
from threading import Thread
from server import server
from client import client
from time import sleep

def coordinator(args):
	threads = []
	seconds = 10

	create_threads(threads, args, seconds)
	launch_threads(threads, args, seconds)

	for i in range(max(args.servers, args.clients))
		threads[i].join()

def create_threads(threads, args, seconds):
	for i in range(args.clients,0,-1):
		threads.append(Thread(target = client, args = [args.ip, args.port+i-1, i*seconds]))

	for i in range(args.servers,0,-1):
		threads.append(Thread(target = server, args = [args.port+i-1]))

def launch_threads(threads, args, seconds):
	for i in range(args.clients):
		threads[i].start()
		sleep(seconds)

	for i in range(args.servers):
		threads[i].start()


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Coordinator for bandwidth test.')
	parser.add_argument('-p', '--port', type=int, help='server connection port', required=True)
	parser.add_argument('-c', '--clients', type=int, default=0, help='number of parallel clients', required=False)
	parser.add_argument('-s', '--servers', type=int, default=0, help='number of parallel servers', required=False)

	args = parser.parse_args()

	coordinator(args)