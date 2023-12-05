import cv2 
import numpy as np

video = cv2.VideoCapture(r"C:\Users\HP\Downloads\WhatsApp video.mp4")

while True:
    status, frame = video.read()
    if not status: break

    # changes can be done here
    small_frame = cv2.resize(frame, (0, 0), fx = 0.9, fy = 0.9)

    gray_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
    inv_frame = rgb_frame * 255

    cv2.imshow("Video output", small_frame)
    cv2.imshow("Video output2", gray_frame)
    cv2.imshow("Video output3", rgb_frame)
    cv2.imshow("Video output4", inv_frame)

    if cv2.waitKey(1) == 27:        # escape key
        break
video.release()     # release memory 
cv2.destroyAllWindows()     # close all windows