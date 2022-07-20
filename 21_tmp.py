#!/usr/bin/python3

import socket
import time
import getpass
from slack_sdk import WebClient

hostname = ' '.join(socket.gethostname().split(".")[:2])
username = getpass.getuser()
curr_time = time.strftime('%H:%M %Y-%m-%d', time.localtime())

status = username + " last seen in " + hostname + " at " + curr_time
# print(status)


json = {
	"status_text": "genom",
}
slack_token="xoxp-2545119925479-3821563305507-3821788389155-8253b8016a3ba769d4313a0a99fe7335"
client = WebClient(token=slack_token)
user="U03Q5GK8ZEX"
response = client.users_profile_set(user=user, profile=json )

