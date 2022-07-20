#!/usr/bin/python3

import socket
import time
import getpass
from slack_sdk import WebClient
import ssl

hostname = ' '.join(socket.gethostname().split(".")[:2])
username = getpass.getuser()
curr_time = time.strftime('%H:%M %Y-%m-%d', time.localtime())

status = username + " last seen in " + hostname + " at " + curr_time
status = "new status"

json = {
	"status_text": status,
}
with open('identity', 'r') as file:
	slack_token, user_id = file.read().splitlines()
	file.close()

ssl._create_default_https_context = ssl._create_unverified_context
client = WebClient(token=slack_token)
response = client.users_profile_set(user=user_id, profile=json)
