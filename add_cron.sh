#!/bin/bash

scriptpath=$(cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)
cronlogs=$scriptpath/logs/cron_logs

if [[ $(echo $(crontab -l 2>$cronlogs | grep "21_locator.py" | wc -l)) != 0 ]]; then
	echo "Schedule already set"
	exit 0
fi
crontab -l >mycron 2>$cronlogs
chmod +x $scriptpath/21_locator.py
echo "*/1 * * * *" $(which python3) $scriptpath/21_locator.py >> mycron
crontab mycron 2>$cronlogs
if [[ $? == "0" ]]; then
	echo "Schedule has been successfully set"
fi
rm mycron