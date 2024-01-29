import threading
import time
import cv2


import check_luminancy
import save_to_database
import detect_face
import app


image_path ="images/frame_capture.jpg"
image = cv2.imread(image_path)
cropped_frame = cv2.resize(image, (352, 240), interpolation=cv2.INTER_LINEAR)

luminancy = True
face = True
userinput = False
luminancy_threshold = 0.04
user_input = ''

stop_threads = False
lock = threading.Lock()



def periodic_task():
    while not stop_threads:
        while not check_luminancy.get_average_luminance(image_path, luminancy_threshold):
            if user_input=='exit':
                break
            print("not enough light")
            time.sleep(1)
            luminancy = False

        while not detect_face.get_face(image_path):
            if user_input=='exit':
                break
            print("no face")
            time.sleep(1)
            face = False
        if user_input!='exit':
            save_to_database.connect_to_database(image_path)
            time.sleep(10)


def user_input_task():
    global stop_threads
    global user_input
    while not stop_threads:
        user_input = input("Enter 'exit' to stop the script: \n")
        if user_input.lower() == 'exit':
            print("Exiting the script.")
            with lock:
                stop_threads = True


def start_collecting_data():
    # Create two threads
    periodic_thread = threading.Thread(target=periodic_task)
    user_input_thread = threading.Thread(target=user_input_task)

    # Start the threads
    periodic_thread.start()
    user_input_thread.start()

    # Wait for the user input thread to finish (the periodic thread will continue running)
    user_input_thread.join()

    # Wait for the periodic thread to finish
    periodic_thread.join()
    #check_variables_thread.join()

    print("All threads are done.")


def run_main(luminancy, userinput):
    while not (luminancy and userinput):
        luminancy = check_luminancy.get_average_luminance(image_path, luminancy_threshold)
        if not luminancy:
            print("Please adjust lighting")
            time.sleep(5) # adjust this to be every second
                
        if luminancy:
            print("Lighting good")
            
            user_input1 = input("Enter 'start' to start the script: \n")
            if user_input1.lower() == 'start':
                userinput = True
                start_collecting_data()

run_main(luminancy, user_input)