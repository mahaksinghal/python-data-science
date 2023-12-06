# https://github.com/google/mediapipe/blob/master/docs/solutions/hands.md

# https://developers.google.com/mediapipe/solutions/guide

# pyautogui

import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    h, w , _ = image.shape
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
            
        # print hand is left
        # if results.multi_handedness[0].classification[0].label == 'Left':
        #     print('left')
        # else:
        #     print('right')

        thumb = hand_landmarks.landmark[4]
        index = hand_landmarks.landmark[8]

        # denormalize the cordinates
        thumb = int(thumb.x *w), int(thumb.y * h)
        index = int(index.x *w), int(index.y * h)

        # draw a circle
        cv2.circle(image, thumb, 10, (0, 255, 0), 5)
        cv2.circle(image, index, 10, (0, 255, 0), 5)
        cv2.line(image, thumb, index, (255, 255, 0), 2)

        # calculate the distance
        dist = ((thumb[0] - index[0])**2 + (thumb[1] - index[1])**2) ** 0.5
        cv2.putText(image, f'{dist:.2f} pixels', (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
cv2.destroyAllWindows()