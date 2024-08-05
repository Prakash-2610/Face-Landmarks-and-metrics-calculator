import cv2
import mediapipe as mp
import math

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize MediaPipe Drawing Utilities
mp_drawing = mp.solutions.drawing_utils

# Define pixel size in centimeters (calibrate this value)
PIXEL_SIZE_CM = 0.05

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def get_landmark_points(landmarks, width, height):
    return [(int(landmark.x * width), int(landmark.y * height)) for landmark in landmarks.landmark]

def convert_pixels_to_cm(pixels):
    return pixels * PIXEL_SIZE_CM

def process_frame(frame, choice):
    height, width, _ = frame.shape
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect face landmarks
    results = face_mesh.process(rgb_image)
    
    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            landmark_points = get_landmark_points(landmarks, width, height)

            if choice == 1:
                # Distance between left eye and right eye
                left_eye = landmark_points[33]
                right_eye = landmark_points[263]
                eye_distance_pixels = calculate_distance(left_eye, right_eye)
                eye_distance_cm = convert_pixels_to_cm(eye_distance_pixels)
                cv2.putText(frame, f"Eye Distance: {eye_distance_cm:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            elif choice == 2:
                # Face length (distance between chin and hairline)
                chin = landmark_points[152]
                hairline = landmark_points[10]
                face_length_pixels = calculate_distance(chin, hairline)
                face_length_cm = convert_pixels_to_cm(face_length_pixels)
                cv2.putText(frame, f"Face Length: {face_length_cm:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            elif choice == 3:
                # Forehead size (distance between hairline and eyebrows)
                hairline = landmark_points[10]
                eyebrows = landmark_points[70]
                forehead_size_pixels = calculate_distance(hairline, eyebrows)
                forehead_size_cm = convert_pixels_to_cm(forehead_size_pixels)
                cv2.putText(frame, f"Forehead Size: {forehead_size_cm:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            elif choice == 4:
                # Mouth width (distance between corners of the mouth)
                left_mouth = landmark_points[61]
                right_mouth = landmark_points[291]
                mouth_width_pixels = calculate_distance(left_mouth, right_mouth)
                mouth_width_cm = convert_pixels_to_cm(mouth_width_pixels)
                cv2.putText(frame, f"Mouth Width: {mouth_width_cm:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            elif choice == 5:
                # Draw landmarks and connections only
                mp_drawing.draw_landmarks(
                    image=frame,
                    landmark_list=landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(100, 100, 0), thickness=1, circle_radius=1),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1)
                )

    return frame
