from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import time
import save_to_database
import sys

app = Flask(__name__)
socketio = SocketIO(app)

variable_value = 0  # Initial value
stop_threads = False
user_input = ""
image_path ="images/frame_capture.jpg"

@app.route('/')
def index():
    return render_template('index.html', variable_value=variable_value)

@socketio.on('stop_threads')
def handle_stop_threads():
    global stop_threads
    print("Stopping threads.")
    stop_threads = True
    sys.exit()

# Your logic to update the variable (this could be in response to user input, a timer, etc.)
def update_variable_logic():
    global variable_value
    while not stop_threads:
        variable_value = save_to_database.connect_to_database(image_path)
        socketio.emit('variable_updated', {'value': variable_value})
        time.sleep(5)  # Adjust the sleep time based on your requirements


if __name__ == '__main__':
    # Start the Flask SocketIO server in a separate thread
    socketio_thread = threading.Thread(target=socketio.run, args=(app,), kwargs={'debug': True, 'use_reloader': False})
    socketio_thread.start()

    # Create two threads
    periodic_thread = threading.Thread(target=update_variable_logic)

    # Start the threads
    periodic_thread.start()

    # Wait for the threads to finish
    socketio_thread.join()
    periodic_thread.join()

    print("All threads are done.")
