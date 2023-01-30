from tqdm import tqdm

import numpy as np
import cv2
import random

### GLOBAL VARIABLES ###
#Number of vertices of the Polygon
POLYGON = 3
#Number of random points entered
LOOP = 100000
#Width and height of window
WIDTH = 1000
HEIGHT = 1000
#To store the selected points
POLYGON_POINTS = []

#Draws pixel on canvas
def draw_pixel(x,y):
    cv2.circle(img,(x,y),0,255,-1)

#Loop that detects clicks
def click_event(event, x, y, flags, params):
    #Left click
    if event == cv2.EVENT_LBUTTONDOWN:
        POLYGON_POINTS.append((x,y))
        draw_pixel(x,y)
    
    #Fractal
    if len(POLYGON_POINTS) == POLYGON+1:
        #Splicing the polygon
        triangle = POLYGON_POINTS[:POLYGON]
        #First point to start the fractal from
        lastPoint = POLYGON_POINTS[-1]
        #Fratal loop
        for i in tqdm(range(LOOP)):
            randPoint = random.choice(triangle)
            #New point = point in the middle between last point and a random polygon vertex
            newPoint = (int((randPoint[0]+lastPoint[0])/2), int((randPoint[1]+lastPoint[1])/2))
            draw_pixel(newPoint[0],newPoint[1])
            lastPoint = newPoint

        POLYGON_POINTS.clear()

    cv2.imshow('image',img)

if __name__ == "__main__":
    img = np.zeros((WIDTH,HEIGHT,1),np.uint8)
    cv2.imshow('image',img)
    cv2.setMouseCallback('image',click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

