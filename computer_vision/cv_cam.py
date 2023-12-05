import cv2 
import numpy as np

video = cv2.VideoCapture(0)

while True:
    status, frame = video.read()
    if not status: break
    cv2.imshow("Video output", frame)
    if cv2.waitKey(1) == 27:        # escape key
        break
video.release()     # release memory 
cv2.destroyAllWindows()     # close all windows
