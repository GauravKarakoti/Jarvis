import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import numpy as np
def computer_vision():
                                                                            
    ser = serial.Serial('COM3', 9600)
    detector = HandDetector(detectionCon=0.8, maxHands=1)
    video = cv2.VideoCapture(0)
    num_servos = 2 

    while True:
        ret, frame = video.read()
        frame = cv2.flip(frame, 1)
        hands, img = detector.findHands(frame)

        if hands:
            fingerUp = detector.fingersUp(hands[0])[:num_servos]  

            finger_count_str = ''.join(map(str, fingerUp))
            ser.write(finger_count_str.encode())

            angles = [0, 0] 
            for i, finger in enumerate(fingerUp, start=1):
                angles[i - 1] = int(np.interp(finger, [0, 1], [0, 180]))

            print("Detected Angles:", angles) 
            
         
            command = f"{angles[0]}:{angles[1]}\n" 
            ser.write(command.encode()) 

        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == ord("k"):
            break

    ser.close()
    video.release()
    cv2.destroyAllWindows()