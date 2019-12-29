import cv2
import numpy as np
import os
import pyautogui
def findSmallImage(small_image, large_image):
    method = cv2.TM_SQDIFF_NORMED

    # Read the images from the file
    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    # Step 3: Draw the rectangle on large_image
    boundingRect = cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)
    return large_image



while(True):
 try:
  img = pyautogui.screenshot()
  image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
  smallFoundImg = findSmallImage(cv2.imread('AddDough.png'), image)
  #cv2.imshow("SmallFoundImg", smallFoundImg)
  StopIteration(0.5)
 except KeyboardInterrupt:
  break

out.release()
cv2.destroyAllWindows()