import cv2
import numpy as np

# Load the image
image = cv2.imread('F:/Mine.jpg')

# Convert to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of the background color (e.g., green)
lower_color = np.array([35, 100, 100])  # Lower bound of green
upper_color = np.array([85, 255, 255])  # Upper bound of green

# Create a mask
mask = cv2.inRange(hsv, lower_color, upper_color)

# Invert the mask to get the foreground
mask_inv = cv2.bitwise_not(mask)

# Use the mask to extract the foreground
foreground = cv2.bitwise_and(image, image, mask=mask_inv)

# Save the result
cv2.imwrite('output_image.png', foreground)

