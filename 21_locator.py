from cmath import log
import socket
import time
import sys
import os

try:
	import requests
except ImportError:
	print("Python \"requests\" module is missing!")
	sys.exit()


hostname = ' '.join(socket.gethostname().split(".")[:2])
date = '.'.join([str(time.localtime().tm_year),
				str(time.localtime().tm_mon),
				str(time.localtime().tm_mday)])
time = ':'.join([str(time.localtime().tm_hour),
				str(time.localtime().tm_min)])
status = "Last seen in " + hostname + " at " + time + " (" + date + ")"

logfile = open(os.path.abspath(os.path.dirname(__file__)) + "/logs/tmp_logs", "a")
logfile.write(status + "\n")
logfile.close()

