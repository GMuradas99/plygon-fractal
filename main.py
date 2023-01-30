import numpy as np
import cv2
import random

POLYGON = 3
LOOP = 100000
POLYGON_POINTS = []

def draw_pixel(x,y):
    cv2.circle(img,(x,y),0,255,-1)

def click_event(event, x, y, flags, params):
    #Clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        POLYGON_POINTS.append((x,y))
        draw_pixel(x,y)
    
    #Fractal
    if len(POLYGON_POINTS) == POLYGON+1:
        triangle = POLYGON_POINTS[:POLYGON]

        lastPoint = POLYGON_POINTS[-1]
        for i in range(LOOP):
            randPoint = random.choice(triangle)
            newPoint = (int((randPoint[0]+lastPoint[0])/2), int((randPoint[1]+lastPoint[1])/2))
            draw_pixel(newPoint[0],newPoint[1])
            lastPoint = newPoint

        POLYGON_POINTS.clear()

    cv2.imshow('image',img)

img = np.zeros((512,512,1),np.uint8)
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

