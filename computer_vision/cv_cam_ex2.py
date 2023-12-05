import cv2 
import numpy as np

video = cv2.VideoCapture(0)

while True:
    status, frame = video.read()
    if not status: break

    # cv2.rectangle(frame, (50, 50), (200, 300), (255, 255, 255), 5)
    cv2.rectangle(frame, (50, 50), (200, 300), (255, 255, 255), 5, -1)  # -1 means fills color
    cv2.circle(frame, (125, 175), 100, (0, 0, 255), -1)  
    cv2.putText(frame, "One",(100, 175), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1)

    cv2.imshow("Video output", frame)
    if cv2.waitKey(1) == 27:        # escape key
        break
video.release()     # release memory 
cv2.destroyAllWindows()     # close all windows
