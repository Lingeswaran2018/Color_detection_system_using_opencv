import cv2
import numpy as np
from PIL import Image
from Get_limit import get_limits

def get_limits(color): # Function to determine the lower and upper limits of the color in HSV space
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Define a tolerance for hue adjustment
    hue_tolerance = 10

    # Calculate lower and upper hue values based on the tolerance
    lower_hue = max(0, hue - hue_tolerance)
    upper_hue = min(180, hue + hue_tolerance)

    # Set lower and upper limits for saturation and value
    lower_limit = np.array([lower_hue, 100, 100], dtype=np.uint8)
    upper_limit = np.array([upper_hue, 255, 255], dtype=np.uint8)

    return lower_limit, upper_limit

def Linga_Trackbar(x):   # Get trackbar positions
    global your_color
    b = cv2.getTrackbarPos("B", "trackbar_window")
    g = cv2.getTrackbarPos("G", "trackbar_window")
    r = cv2.getTrackbarPos("R", "trackbar_window")
    your_color = [b, g, r]
    # Update the color displayed in the image window
    img_bgr[:] = (b, g, r)


# Create trackbar window
cv2.namedWindow("trackbar_window")
cv2.createTrackbar("B", "trackbar_window", 0, 255, Linga_Trackbar)
cv2.createTrackbar("G", "trackbar_window", 0, 255, Linga_Trackbar)
cv2.createTrackbar("R", "trackbar_window", 0, 255, Linga_Trackbar)

# Create webcam window
cv2.namedWindow("webcam_window")
img_bgr = np.zeros((400, 650, 3), np.uint8)
your_color = [0, 0, 255]  # Initial color in BGR colorspace
cap = cv2.VideoCapture(0)
while True:
    # Update color from trackbars
    b, g, r = your_color

    # Update the color displayed in the trackbar window
    cv2.imshow("trackbar_window", img_bgr)

    ret, frame = cap.read()

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=your_color)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    # Show webcam feed in the webcam window
    cv2.imshow('webcam_window', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
