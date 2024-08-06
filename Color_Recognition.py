import cv2
import numpy as np

# Global variables to store HSV and BGR values
h, s, v = 0, 0, 0
b, g, r = 0, 0, 0

def mouse_callback(event, x, y, flags, param):
    global hsv_frame, frame, h, s, v, b, g, r
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_value = hsv_frame[y, x]
        h, s, v = int(hsv_value[0]), int(hsv_value[1]), int(hsv_value[2])
        
        bgr_value = frame[y, x]
        b, g, r = int(bgr_value[0]), int(bgr_value[1]), int(bgr_value[2])

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_callback)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Display the selected HSV and BGR values
    cv2.rectangle(frame, (10, 10), (400, 120), (255, 255, 255), -1)
    cv2.putText(frame, f"H: {h}, S: {s}, V: {v}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(frame, f"B: {b}, G: {g}, R: {r}", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    
    # Display the selected color in the top right corner
    selected_color = np.zeros((100, 100, 3), np.uint8)
    selected_color[:] = [b, g, r]
    frame[10:110, frame.shape[1]-110:frame.shape[1]-10] = selected_color
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()

