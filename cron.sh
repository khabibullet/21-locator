#!/bin/bash

crontab -l > mycron
echo "/1 * * * * /usr/local/bin/python3 ~/other/21_host_status.py" >> mycron
