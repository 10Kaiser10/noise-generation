import numpy as np
import cv2
import random as rand
import time
import math

currT = time.time()
sizeX = 512
sizeY = 512

img = np.ndarray((sizeX,sizeY,3))

'''img[0,0] = [rand.random(), rand.random(), rand.random()]
img[0,sizeY-1] = [rand.random(), rand.random(), rand.random()]
img[sizeX-1,0] = [rand.random(), rand.random(), rand.random()]
img[sizeX-1,sizeY-1] = [rand.random(), rand.random(), rand.random()]'''

img[0,0] = [1,0,0]
img[0,sizeY-1] = [0,0,1]
img[sizeX-1,0] = [0,1,0]
img[sizeX-1,sizeY-1] = [1,1,0]


for y in range(0, sizeY):
    for i in range(0,3):
        a = (img[0,sizeY-1,i]*y/sizeY + (1-y/sizeY)*img[0,0,i])
        b = (img[sizeX-1,sizeY-1,i]*y/sizeY + (1-y/sizeY)*img[sizeX-1,0,i])
        a = 0.5 - (math.cos(a*math.pi))/2
        b = 0.5 - (math.cos(b*math.pi))/2
        for x in range(0, sizeX):
            val = (1-x/sizeX)*a + (x/sizeX)*b
            out = 0.5 - (math.cos(val*math.pi))/2
            img[x,y,i] = out


print(time.time() - currT)
cv2.imshow("ss" ,img)
cv2.waitKey(0)
