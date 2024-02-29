import cv2

# Load the Haar cascade classifier for face detection
cascPath = "face.xml"
face_cascade = cv2.CascadeClassifier(cascPath)

# Create a video capture object for the default webcam
url = 'http://172.16.5.170:81/stream'

# Open the video stream
cap = cv2.VideoCapture(url)

while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image using the Haar cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw squares around the faces detected
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the video feed with the squares drawn
    cv2.imshow('Video Feed', frame)

    # Wait for a key press to exit the program
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()