## **21 locator**

### **Locating student**

**Problem**

There are a lot of machines in 21school campus, which you can use to study. When student is logging in school machine, some information in his/her **school website profile**, such as **host machine number** and **login time**, is automatically updating. Thus, you can find your friend, if he/she is currently working on campus machine, or another student, whos work you should grade. This functionality is implemented via **42's API**, which is **not working** correctly with Kazan 21school campus machines anymore.

**Solution**

Since student have got a Slack profile in the school Slack workspcae, he can set **profile status** manually. At the same time **environment variables list** contains host machine number. It's not convenient to set profile status manually each time student logs in and logs out machine. **Slack API** gives us possibility to set profile status programmatically sending web request to Slack.
<br><br>

## **Platform**

Mac OS (x86)
<br><br>

## **Components**

**21_locator.py** script gets host machine environment variable info (host machine id and execution date). 

**add_cron.sh** and **remove_cron.sh** scripts add/remove cronjob to exucute 21_locator.py script with 1 minute interval. 

**identity** file contains slack workspace user private token and id.
<br><br>
## **Cronjob**

adding cronjob
```console
host@name:~$ bash add_cron.sh
```
removing cronjob
```console
host@name:~$ bash remove_cron.sh
```
