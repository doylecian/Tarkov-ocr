import pyautogui
import cv2 as cv
import numpy as np
import os
import glob
from matplotlib import pyplot as plt

font = cv.FONT_HERSHEY_SIMPLEX

template_data = []
temp_list = glob.glob('C:\\Users\\Cian\\Desktop\\template_images\\*.png')

for temp in temp_list:
    image = cv.imread(temp, 0)
    template_data.append(image)


img_rgb = cv.imread('C:\\Users\\Cian\\Desktop\\stash.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

for tmp in template_data:
    cv.waitKey(500)
    cv.destroyAllWindows()
    try:
        w, h = tmp.shape[::-1]
        res = cv.matchTemplate(img_gray, tmp, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        cv.imshow("Item to find", tmp)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

        cv.imshow('Result', img_rgb)
    except AttributeError:
        print("Skipped image")


cv.imshow('Result', img_rgb)
cv.waitKey(0)



