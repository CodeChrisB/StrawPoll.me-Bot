# StrawPoll.me-Bot

### Wait what bot? 

Its a bot for [StrawPoll.me](https://strawpoll.me)

But its not the standard vote bot. This Bot creates polls, in fact a lot polls.

---

### But why ?

StrawPoll.me is using Id's to save their Polls. They started with Id = 1 and always added +1 for every Poll that got created afterwards. We can access these Polls with [http://www.strawpoll.me/1](http://www.strawpoll.me/1), where 1 Is the ID

The idea here is that there are some cool poll-numbers to get like 
20000000 (a friend of mine has this) or 

23456789 (thats my id). 

If we now create 1 Millions Polls we surely have some cool Poll ID's

---
### How to use ?
 You will need Python: https://www.python.org/

- Open a terminal 
- Navigate to the folder containing strawBot.py
- Enter the command : pip install requests (this has to be done only once)
- Enter the command : python .\strawBot.py

If you want to change the question and the anwsers just open the data.py File. More Information about what to change is inside the File

The amount of polls created can be changed in the strawBot.py file. Its on the top of the file where it says:

amount = 100000

You can change the value to a limited amount I'd say everything that has more than 10 Zero's is useless because it would takes month to create that many Polls. The bot is able to create 250.000 Polls per Hour.

---
## Have a nice day
### Your CCB

