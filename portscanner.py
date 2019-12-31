#!/usr/bin/python3

import socket, sys
from datetime import datetime

if len(sys.argv) < 2:
	print("Invalid number of arguments")
	quit()
else:
	target = socket.gethostbyname(sys.argv[1]) # resolve DNS if given a hostname

print(f'Port Scanning host at {target}:')
print(f'Time started: {datetime.now()}')
print()

for port in range(1,10000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(1)
	result = s.connect_ex((target, port))
	if result == 0:
		print(f'Port {port} is open!')
	s.close()
