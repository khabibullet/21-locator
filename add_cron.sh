#!/bin/bash

scriptpath=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
cronlogs=$scriptpath/logs/cron_logs

chmod +x $scriptpath/21_locator.py
crontab -l 2>$cronlogs | grep -v "21_locator.py" > mycron
echo "*/1 * * * *" $(which python3) $scriptpath/21_locator.py "&>$scriptpath/logs/locator_logs" >> mycron
crontab mycron 2>$cronlogs
if [[ $? == "0" ]]; then
	echo "Schedule has been successfully set"
fi
rm mycron