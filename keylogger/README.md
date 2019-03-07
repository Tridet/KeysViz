# Keylogger

Keylogger in Python. You decide when you run it and when you stop it. The idea is to record the key struck for a certain activity, so you need to run the keylogger during this activity, and you need to specify the name of the file for this activity (the keylogger will concatenate at the end of this text file).
## Installing

You need Python 3 and the library pynput :

```
sudo pip install pynput
```

## Recording

Then you need to run the command : 

```
sudo name="name_of_your_log.txt" nohup python keylogger.py &
```

The variable **name** will become the name of the log file.

The program will run quietly in the background recording your keystrokes

Finally the program is set to be closed if you strike a key that python does not recognize and then assign a "None" type. 

Make sure you have such a key on your keyboard or you can change it with any stroke you want line 24 in the keylogger code.

Before exiting, the program writes "Exiting..." in the logs, it needs to be taken into account in the parser or just remove it if you want (line 25).

## WARNING

IF YOU WANT TO ENSURE THE PRESENCE OF A NONE KEY, RUN THE COMMAND : 

```
sudo name="name_of_your_log.txt" python3 keylogger.py
```

SO YOU CAN EXIT THE CODE MANUALLY IN THE TERMINAL. OR YOU’LL HAVE TO DO SOMETHING LIKE : 

```
ps aux | grep Python 
```

AND THEN GET THE ID OF THE PROCESS TO KILL IT : kill ID

OR YOU CAN SIMPLY CHANGE WHICH KEY WILL END THE PROGRAM IN THE CODE

HAVE FUN!!!

## Credits

The keylogger is a enhanced version of the following [code](https://theembeddedlab.com/tutorials/keylogger-python/) taking advantage of the Python Logger.