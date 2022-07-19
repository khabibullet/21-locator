#!/usr/bin/python3

import socket
import time
import sys

# try:
# 	import requests
# except ImportError:
# 	sys.exit()

hostname = ' '.join(socket.gethostname().split(".")[:2])
date = '.'.join([str(time.localtime().tm_year),
				str(time.localtime().tm_mon),
				str(time.localtime().tm_mday)])
time = ':'.join([str(time.localtime().tm_hour),
				str(time.localtime().tm_min)])
status = "Last seen in " + hostname + " at " + time + " (" + date + ")"
print(status)

