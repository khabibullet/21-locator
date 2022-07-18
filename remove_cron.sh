#!/bin/bash

scriptpath=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
cronlogs=$scriptpath/logs/cron_logs

if [[ $(echo $(crontab -l 2>$cronlogs | grep "21_locator.py" | wc -l)) == 0 ]]; then
	echo "No schedule to remove"
	exit 0
fi
crontab -l 2>$cronlogs | grep -v "21_locator.py" > mycron
crontab mycron 2>$cronlogs
rm mycron
echo "Schedule has been succesfully removed"