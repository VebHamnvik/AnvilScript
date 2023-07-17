import time
import cv2
import mss
import numpy

#This was for learning and testing mss

# template and dimensions
template = cv2.imread("assets/w1town.png", 0)
w, h = template.shape

with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
    output = "test.png"

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)
    testBilde = cv2.imread('test.png', 0)
    cv2.imshow('Test', testBilde)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




    # Press "q" to quit
    #if cv2.waitKey(25) & 0xFF == ord("q"):
    #    cv2.destroyAllWindows()
    #    break





