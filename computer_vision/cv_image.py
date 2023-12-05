import cv2

# load an image
img1 = cv2.imread("computer_vision\python.png")

print(img1.shape)           # weight, height, layers of colors
print(img1.ndim)

# print(img1)

# img1 = img1 * 255           # max value is 255

# img1 = img1[0:100, 0:200]        # width, height

# img1 = img1[0:1000:2]
img1 = img1[0:100, 1]

# to print the image
cv2.imshow("image 1", img1)
cv2.waitKey(0)