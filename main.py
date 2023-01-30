import numpy as np
import cv2
import random

LOOP = 1
POLYGON_POINTS = []
DRAWN = False

def draw_pixel(x,y):
    cv2.circle(img,(x,y),0,255,-1)

def click_event(event, x, y, flags, params):
    #Clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        POLYGON_POINTS.append((x,y))
        draw_pixel(x,y)
        cv2.imshow('image',img)
    
    #Fractal
    if len(POLYGON_POINTS) == 4:
        triangle = POLYGON_POINTS[:3]

        lastPoint = POLYGON_POINTS[-1]
        for i in range(LOOP):
            

        POLYGON_POINTS.clear()

img = np.zeros((512,512,1),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

