import cv2
import keyboard
import pyautogui
import time
import mss
from pyscreenshot.plugins.msswrap import sct

#Removed the other methods as one is enough. Tested it multiple times and it worked fine
methods = [cv2.TM_CCOEFF]

def templateMatching(templateImg):

    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
        output = "assets/test.png"

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)

        baseImg = cv2.resize(cv2.imread('assets/test.png', 0), (0,0), fx = 0.7, fy = 0.7)
        template = cv2.resize(cv2.imread(templateImg, 0), (0,0), fx = 0.7, fy = 0.7)

        w, h = template.shape

        for method in methods:
            img2 = baseImg.copy()
            result = cv2.matchTemplate(img2, template, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            location = max_loc
            bottom_right = (location[0] + h, location[1] + w)

            middle = ((location[0] + bottom_right[0]) / 2, (location[1] + bottom_right[1]) / 2)

            middleX = int(middle[0])
            middleY = int(middle[1])

            #If you want to see the template matching in action you just uncomment these
            cv2.rectangle(img2, location, bottom_right, 255, 5)
            cv2.circle(img2, (middleX, middleY), 3, (0,0,255), -1)

            #and this
            cv2.imshow('Match', img2)

            #the +10 and +40 was after playing around. When I just used middleX and middleY,
            #the cursor missed the rectangle. Will probably need more refining once I try it with the game
            pyautogui.moveTo(middleX+10, middleY+40, duration=0.25)
            pyautogui.leftClick()
            time.sleep(1)

            #and this
            cv2.waitKey(0)
            cv2.destroyAllWindows()

#Made a seperate function for implementing scrolling the mousewheel when finding the bullet
def templateMatchingBullet(templateImg):
    keyboard.add_hotkey('esc', lambda: exit(0))

    baseImg = sct.shot(output='baseImg.png')

    img = cv2.imread(baseImg, 0)
    template = cv2.imread(templateImg, 0)
    w, h = template.shape

    for method in methods:
        #Lager en kopi av bilde i hver loop slik at ikke samme bilde blir tegnet over hver gang
        img2 = img.copy()
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        #location vil automatisk være et punkt øvert i venstre, så da må vi finne nederst til høyre
        location = max_loc
        bottom_right = (location[0] + h, location[1] + w)

        #Tegner rektangelet mellom de to punktene jeg har funnet
        cv2.rectangle(img2, location, bottom_right, 255, 5)

        #Finner midten i rektangelet
        middle = ((location[0] + bottom_right[0]) / 2, (location[1] + bottom_right[1]) / 2)

        #Lagrer koordinatene til senteret av rektangelet i to forskjellige variabler
        middleX = int(middle[0])
        middleY = int(middle[1])

        #Tegner en dot i midtpunktet
        cv2.circle(img2, (middleX, middleY), 3, (0,0,255), -1)

        #Lager popoppvinduer for hvert bilde
        #cv2.imshow('Match', img2)
        pyautogui.scroll(-7)
        pyautogui.moveTo(middleX+150, middleY+100, duration=0.25)
        pyautogui.leftClick

        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

#Tried adding a sleep timer so I had time to open Idleon after starting the script
time.sleep(3)


templateMatching('assets/w1anvil.png')
templateMatching('assets/anviltab2.png')
#templateMatchingBullet('assets/bullet1.png')
templateMatching('assets/craft.png')