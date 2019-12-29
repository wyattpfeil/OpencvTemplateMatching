import numpy as np
import cv2

method = cv2.TM_SQDIFF_NORMED

cap = cv2.VideoCapture(1)
small_image = cv2.imread('qrCode.png')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Read the images from the file
    large_image = frame

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
    #print(MPx + ", " + MPy)
    # Display the original image with the rectangle around the match.
    cv2.imshow('output',large_image)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()