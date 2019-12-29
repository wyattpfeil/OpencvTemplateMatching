import cv2
import numpy as np

def checkIfImageExists(small_image, large_image):
    res = cv2.matchTemplate(small_image, large_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    threshold = 0.8
    flag = False
    if np.amax(res) > threshold:
        flag = True
    if flag == True: 
        return True
    else:
        return False

print(checkIfImageExists(cv2.imread('AddDough.png'), cv2.imread('large_image.png')))

