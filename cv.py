import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Load YOLO object detection model
def load_yolo():
    # Provide the correct path to your YOLOv3 files
    yolo_cfg = "yolov3.cfg"  # Replace with full path if not in the same folder
    yolo_weights = "yolov3.weights"  # Replace with full path if not in the same folder
    
    # Load YOLO network
    net = cv2.dnn.readNet(yolo_weights, yolo_cfg)
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getLayers()]
    return net, output_layers

# Function to detect phones using YOLO
def detect_phone(frame, net, output_layers):
    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []

    # Loop over each detected object
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Only consider detections with high confidence
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w // 2
                y = center_y - h // 2
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-maxima suppression to remove redundant overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    
    return indices, class_ids, boxes

# Function to count raised fingers
def count_fingers(landmarks):
    finger_count = 0
    
    # Check if the thumb is raised
    if landmarks[4].y < landmarks[3].y:
        finger_count += 1
    
    # Check if the index finger is raised
    if landmarks[8].y < landmarks[6].y:
        finger_count += 1
    
    # Check if the middle finger is raised
    if landmarks[12].y < landmarks[10].y:
        finger_count += 1
    
    # Check if the ring finger is raised
    if landmarks[16].y < landmarks[14].y:
        finger_count += 1
    
    # Check if the pinky is raised
    if landmarks[20].y < landmarks[18].y:
        finger_count += 1

    return finger_count

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Load YOLO model
net, output_layers = load_yolo()

while True:
    ret, frame = cap.read()
    
    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB (MediaPipe works with RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to find hands
    result = hands.process(rgb_frame)
    
    # Draw landmarks and count fingers
    if result.multi_hand_landmarks:
        for landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count the number of raised fingers
            finger_count = count_fingers(landmarks.landmark)
            cv2.putText(frame, f"Fingers Raised: {finger_count}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Detect phones using YOLO
    indices, class_ids, boxes = detect_phone(frame, net, output_layers)
    
    # Loop over all detections
    for i in range(len(indices)):
        if class_ids[indices[i][0]] == 67:  # Class ID 67 corresponds to "cell phone" in the COCO dataset
            box = boxes[indices[i][0]]
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Phone Detected", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    
    # Display the image
    cv2.imshow("Finger and Phone Detection", frame)
    
    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()