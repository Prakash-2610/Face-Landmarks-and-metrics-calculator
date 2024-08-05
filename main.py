import cv2
from camera_processing import process_frame
from user_interaction import get_user_choice

def main():
    choice = get_user_choice()
    
    if choice is None:
        return

    # Open the webcam
    cap = cv2.VideoCapture(0)  # Change to the video file path if needed

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame based on user choice
        processed_frame = process_frame(frame, choice)
        cv2.imshow("Face Mesh", processed_frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
