import numpy as np
import cv2
import win32api

#This was for learning template matching


anvil = cv2.imread('assets/w1town.png', 0)
template = cv2.imread('assets/w1anvil.png', 0)
w, h = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = anvil.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + h, location[1] + w)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

anvilscreen = cv2.imread('assets/anvilscreen.png', 0)
template = cv2.imread('assets/anviltab2.png', 0)
w, h = template.shape

for method in methods:
    img2 = anvilscreen.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + h, location[1] + w)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

anvilbullet = cv2.imread('assets/anviltabbullet.png', 0)
template = cv2.imread('assets/bullet1.png', 0)
w, h = template.shape

for method in methods:
    img2 = anvilbullet.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + h, location[1] + w)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bulletcrafting = cv2.imread('assets/bulletcrafting.png', 0)
template = cv2.imread('assets/craft.png', 0)
w, h = template.shape

for method in methods:
    img2 = bulletcrafting.copy()
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + h, location[1] + w)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()