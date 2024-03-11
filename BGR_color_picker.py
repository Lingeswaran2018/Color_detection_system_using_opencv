import cv2
import numpy as np

def Linga_Trackbar(x):   #This function is defined but left empty. This function will be called whenever a trackbar's value changes. Since it's empty (pass), it doesn't do anything.
    pass

# Trackbar
cv2.namedWindow("frame")      #This line creates a window with the title "frame". This is the window where the trackbars will be displayed.
cv2.createTrackbar("B", "frame", 0, 255, Linga_Trackbar)     #This line creates a trackbar named "B" inside the window "frame". The trackbar has a range from 0 to 255, and it calls the function Linga_Trackbar whenever its value changes.
cv2.createTrackbar("G", "frame", 0, 255, Linga_Trackbar)
cv2.createTrackbar("R", "frame", 0, 255, Linga_Trackbar)

img_bgr = np.zeros((250, 650, 3), np.uint8)  #It creates a black image (img_bgr) of size 250x650 pixels with 3 channels (BGR) using NumPy. This image will be updated dynamically based on the values of the trackbars.

while True: #the code continuously updates the values of the BGR channels based on the positions of the trackbars.
    b = cv2.getTrackbarPos("B", "frame")  #This line gets the current position of the trackbar named "B" inside the window "frame".
    g = cv2.getTrackbarPos("G", "frame")
    r = cv2.getTrackbarPos("R", "frame")

    img_bgr[:] = (b, g, r)

    cv2.imshow("frame", img_bgr)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

