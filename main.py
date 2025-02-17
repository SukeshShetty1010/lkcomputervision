import cv2
from lkcomputervision import MediaPipeHandler

# Initialize the MediaPipeHandler
mp = MediaPipeHandler()

# Capture video from the webcam (you can also specify a video file path)
cap = cv2.VideoCapture(0)  # 0 represents the default webcam

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    if not ret:
        break  # Break the loop if we can't read a frame

    # Process the frame to track hands
    result = mp.trackHands(frame)

    # Retrieve the frame with hand landmarks drawn on it
    frame_with_landmarks = result["frame"]

    # Display the frame with landmarks
    cv2.imshow("Hand Tracking", frame_with_landmarks)

    # Exit the loop when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
