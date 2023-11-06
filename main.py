import cv2
import numpy as np

# Load the image
image = cv2.imread("new.png")

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper thresholds for the drought color (in HSV format)
lower_threshold = np.array([0, 25, 25])
upper_threshold = np.array([30, 200, 200])

# Create a mask based on the defined thresholds
mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the segmented image
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


