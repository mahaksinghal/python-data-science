# # https://github.com/google/mediapipe/blob/master/docs/solutions/hands.md

# # https://developers.google.com/mediapipe/solutions/guide

# # pyautogui

# import cv2
# import mediapipe as mp
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_hands = mp.solutions.hands

# circle_center = (300, 300)
# # For webcam input:
# cap = cv2.VideoCapture(0)
# with mp_hands.Hands(
#     model_complexity=0,
#     min_detection_confidence=0.5,
#     min_tracking_confidence=0.5) as hands:
#   while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#       print("Ignoring empty camera frame.")
#       # If loading a video, use 'break' instead of 'continue'.
#       continue

#     # To improve performance, optionally mark the image as not writeable to
#     # pass by reference.
#     image.flags.writeable = False
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(image)

#     # Draw the hand annotations on the image.
#     image.flags.writeable = True
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
#     h, w , _ = image.shape
#     if results.multi_hand_landmarks:
#       for hand_landmarks in results.multi_hand_landmarks:

#         thumb = hand_landmarks.landmark[4]
#         index = hand_landmarks.landmark[8]

#         # denormalize the cordinates
#         thumb = int(thumb.x *w), int(thumb.y * h)
#         index = int(index.x *w), int(index.y * h)

#         # draw a circle
#         cv2.circle(image, thumb, 10, (0, 255, 0), 5)
#         cv2.circle(image, index, 10, (0, 255, 0), 5)
#         cv2.line(image, thumb, index, (255, 255, 0), 2)

#         # calculate the distance
#         dist = ((thumb[0] - index[0])**2 + (thumb[1] - index[1])**2) ** 0.5

#         # adjust circle size based on distance
#         circle_radius= int(50 - dist*200)

#         # draw the circle
#         cv2.circle(image, circle_center, circle_radius, (0, 255, 255), 4)
#         # cv2.putText(image, f'{dist:.2f} pixels', (50, 50),
#                     # cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

#     # Flip the image horizontally for a selfie-view display.
#     cv2.imshow('MediaPipe Hands', image)
#     if cv2.waitKey(5) & 0xFF == 27:
#       break
# cap.release()
# cv2.destroyAllWindows()

# -------------------------------------------------------------------------------------------------------
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# For static images:
IMAGE_FILES = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
 for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Process the grayscale image
    results = hands.process(gray_image)

    # Print handedness and draw hand landmarks on the image
    if not results.multi_hand_landmarks:
      continue
    for hand_landmarks in results.multi_hand_landmarks:
      mp_drawing.draw_landmarks(
          image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing.DrawingSpec(color=mp_drawing.BLUE_color, thickness=2, circle_radius=4),
          mp_drawing.DrawingSpec(color=mp_drawing.RED_color, thickness=2, circle_radius=2)
      )
      for i in range(21):
        x, y = int(hand_landmarks.landmark[i].x * 640), int(hand_landmarks.landmark[i].y * 480)
        if i == 4 or i == 20: # Tip of index finger and thumb
          cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

      # Draw circle based on distance between index finger tip and thumb tip
      cv2.circle(image, (int((hand_landmarks.landmark[4].x + hand_landmarks.landmark[20].x) / 2 * 640),
                         int((hand_landmarks.landmark[4].y + hand_landmarks.landmark[20].y) / 2 * 480)),
                 int(((hand_landmarks.landmark[4].x - hand_landmarks.landmark[20].x) ** 2 +
                       (hand_landmarks.landmark[4].y - hand_landmarks.landmark[20].y) ** 2) ** 0.5 * 640),
                 (255, 0, 0), 2)

    cv2.imwrite(f'output/hand_landmarks_{idx}.png', image)

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
 while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      continue

    image = cv2.flip(image, 1)
    image.flags.writeable = False
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing.DrawingSpec(color=mp_drawing.BLUE_color, thickness=2, circle_radius=4),
            mp_drawing.DrawingSpec(color=mp_drawing.RED_color, thickness=2, circle_radius=2)
        )
        for i in range(21):
          x, y = int(hand_landmarks.landmark[i].x * 640), int(hand_landmarks.landmark[i].y * 480)
          if i == 4 or i == 20: # Tip of index finger and thumb
            cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

        # Draw circle based on distance between index finger tip and thumb tip
        cv2.circle(image, (int((hand_landmarks.landmark[4].x + hand_landmarks.landmark[20].x) / 2 * 640),
                           int((hand_landmarks.landmark[4].y + hand_landmarks.landmark[20].y) / 2 * 480)),
                   int(((hand_landmarks.landmark[4].x - hand_landmarks.landmark[20].x) ** 2 +
                         (hand_landmarks.landmark[4].y - hand_landmarks.landmark[20].y) ** 2) ** 0.5 * 640),
                   (255, 0, 0), 2)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()

cv2.destroyAllWindows()