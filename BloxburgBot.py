import cv2
import numpy as np
import os
import pyautogui

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

def findSmallImage(small_image, large_image):
    method = cv2.TM_SQDIFF_NORMED

    result = cv2.matchTemplate(small_image, large_image, method)

    mn,_,mnLoc,_ = cv2.minMaxLoc(result)
    MPx,MPy = mnLoc

    trows,tcols = small_image.shape[:2]

    boundingRect = cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

    return large_image

def getPizzaType(Screen):
    if checkIfImageExists(cv2.imread("HamImg.png"), Screen):
        return "Ham"
    elif checkIfImageExists(cv2.imread("VeggieImg.png"), Screen):
        return "Veggie"
    elif checkIfImageExists(cv2.imread("PeperoniImg.png"), Screen):
        return "Peperoni"

print(getPizzaType(cv2.imread("FullVeggieIm.jpg")))