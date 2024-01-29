import cv2
import time

# Open the webcam (you can specify the device index, typically 0 for the default webcam)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Display the frame (optional)
    cv2.imshow('Webcam Feed', frame)

    # Save the frame to a file (adjust the file path as needed)
    cv2.imwrite('images/frame_capture.jpg', frame)

    time.sleep(10)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()