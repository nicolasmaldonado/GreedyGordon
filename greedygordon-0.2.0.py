from PIL import ImageGrab
import numpy as np
import cv2
import pywinauto
import time

tmplt =  cv2.imread('zenyellow.jpg',1)
w, h = tmplt.shape[1], tmplt.shape[0]

x0,y0,x1,y1 = 0,20,640,480 ### FOR RESOLUTION
ban = True

while(True):

    img = ImageGrab.grab(bbox=(x0,y0,x1,y1)) #x, y, w, h
    imagen = np.array(img)
    res = cv2.matchTemplate(imagen, tmplt, cv2.TM_CCOEFF_NORMED)

    threshold = 0.66
    loc = np.where(res >= threshold)

    
    
    if len(loc[0]) > 0:
        cv2.waitKey(340)

        """ ultima modificacion TEST
        cv2.waitKey(300)
        """
        ####  Repite lo mismo del principio pero una vez que encontro zen
        img = ImageGrab.grab(bbox=(x0, y0, x1, y1))  # x, y, w, h
        imagen = np.array(img)
        res = cv2.matchTemplate(imagen, tmplt, cv2.TM_CCOEFF_NORMED)

        threshold = 0.66
        loc = np.where(res >= threshold)
        ####

        closer = (1000,1000)
        for pt in zip(*loc[::-1]):
            if ( (pt[0]-x1//2)**2 + (pt[0]-y1//2)**2 ) < ( (closer[0]-x1//2)**2 + (closer[0]-y1//2)**2):
                closer = pt
            
        if len(loc[0]) > 0:
            pywinauto.mouse.press(button="left", coords=(x0+closer[0]+19,y0+closer[1]+22))
            cv2.waitKey(120)
            pywinauto.mouse.release(button="left", coords=(x1 // 2, y1 // 2))
        #for pt in zip(*loc[::-1]):
        #   cv2.rectangle(imagen,pt,(pt[0]+20,pt[1]+15),(0,0,255),2)
        

    #cv2.imshow('frame',imagen)
    k = cv2.waitKey(1)
    if k == 27:
        break
        
