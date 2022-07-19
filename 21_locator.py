#!/usr/bin/python3

import socket
import time
# import sys
import getpass

# try:
# 	import requests
# except ImportError:
# 	sys.exit()

hostname = ' '.join(socket.gethostname().split(".")[:2])
username = getpass.getuser()
curr_time = time.strftime('%H:%M %Y-%m-%d', time.localtime())

status = username + " last seen in " + hostname + " at " + curr_time
print(status)

