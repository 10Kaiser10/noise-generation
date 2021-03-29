import numpy as np
import cv2
import random
import time
from math import cos
from math import pi

sizeX = 600
sizeY = 600

sampledPoints = 60

sampVals = np.ndarray((sampledPoints+1, sampledPoints + 1))

for x in range(0,sampledPoints+1):
    for y in range(0,sampledPoints+1):
        if(x == sampledPoints):
            sampVals[x,y] = sampVals[0,y]
        elif(y == sampledPoints):
            sampVals[x,y] = sampVals[x,0]
        else:
            sampVals[x,y] = random.random()

img = np.ndarray((sizeX,sizeY))
#imgCubic = np.ndarray((sizeX,sizeY))

for i in range(0,sampledPoints):
    for j in range(0,sampledPoints):
        startY = (j*sizeY)//sampledPoints
        endY = ((j+1)*sizeY)//sampledPoints
        lengthY = endY-startY
        for y in range(startY, endY):
            a = (sampVals[i,j+1]*(y-startY)/lengthY + (1-(y-startY)/lengthY)*sampVals[i,j])
            b = (sampVals[i+1,j+1]*(y-startY)/lengthY + (1-(y-startY)/lengthY)*sampVals[i+1,j])
            #aC = 0.5 - (cos(a*pi))/2
            #bC = 0.5 - (cos(b*pi))/2

            startX = (i*sizeX)//sampledPoints
            endX = ((i+1)*sizeX)//sampledPoints
            lengthX = endX-startX
            for x in range(startX, endX):
                img[x,y] = (1-(x-startX)/lengthX)*a + ((x-startX)/lengthX)*b
                #imgCubic[x,y] = 0.5 - (cos(img[x,y]*pi))/2
                #print(img[x,y])

cv2.imshow("linear" ,img)
#cv2.imshow("cubic" ,imgCubic)
cv2.waitKey(0)