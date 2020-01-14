#import the necessary modules
import freenect
import cv2
import numpy as np
import time


#function to get RGB image from kinect
def get_video():
    array,_ = freenect.sync_get_video()
    array = cv2.cvtColor(array,cv2.COLOR_RGB2BGR)
    return array

if __name__ == "__main__":
    i = 0
    while 1:
        #get a frame from RGB camera
        frame = get_video()
 
        #display RGB image
        cv2.imshow('RGB image',frame)

        k = cv2.waitKey(5) & 0xFF
        if k == 32: 
            break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('img/frame'+str(i)+'.png',frame)
            i = i+1
    cv2.destroyAllWindows()
