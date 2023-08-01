import cv2
import numpy as np

def on_trackbar_change(_):
    # Retrieve the current trackbar values
    hue_min = cv2.getTrackbarPos('Hue Min', 'Trackbars')
    hue_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
    sat_min = cv2.getTrackbarPos('Sat Min', 'Trackbars')
    sat_max = cv2.getTrackbarPos('Sat Max', 'Trackbars')
    val_min = cv2.getTrackbarPos('Val Min', 'Trackbars')
    val_max = cv2.getTrackbarPos('Val Max', 'Trackbars')

    # Create lower and upper bounds for HSV thresholding
    lower_bound = np.array([hue_min, sat_min, val_min])
    upper_bound = np.array([hue_max, sat_max, val_max])

    # Apply the HSV thresholding to the image
    image_filtered = cv2.inRange(image_hsv, lower_bound, upper_bound)

    # Concatenate the original image and the filtered image horizontally
    combined_image = np.hstack((image, cv2.cvtColor(image_filtered, cv2.COLOR_GRAY2BGR)))

    # Show the combined image
    cv2.imshow('Original and Filtered Image', combined_image)

# Load the image
image = cv2.imread("input.JPG")
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a window to display the trackbars
cv2.namedWindow('Trackbars')

# Create trackbars for each parameter
cv2.createTrackbar('Hue Min', 'Trackbars', 0, 179, on_trackbar_change)
cv2.createTrackbar('Hue Max', 'Trackbars', 179, 179, on_trackbar_change)
cv2.createTrackbar('Sat Min', 'Trackbars', 0, 255, on_trackbar_change)
cv2.createTrackbar('Sat Max', 'Trackbars', 255, 255, on_trackbar_change)
cv2.createTrackbar('Val Min', 'Trackbars', 0, 255, on_trackbar_change)
cv2.createTrackbar('Val Max', 'Trackbars', 255, 255, on_trackbar_change)

# Show the original image
cv2.imshow('Original and Filtered Image', image)

# Call the trackbar callback function to initialize the filtered image
on_trackbar_change(0)

# Wait for key press and close the window on 'q' press
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
