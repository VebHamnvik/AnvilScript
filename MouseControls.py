import pyautogui

#This was for learning how to control the mouse

for i in range(2):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)


#Etter å ha funnet koordinatene for punktet
    #pyautogui.moveTo(middleX, middleY, duration=0.5)
    #pyautogui.click(middleX, middleY, button='left')