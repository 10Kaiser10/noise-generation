import numpy as np
import cv2
import random
import time

sizeX = 700
sizeY = 700

img = np.zeros((sizeX,sizeY),dtype=float)

InIsampledPoints = 35
val=1

for p in range(0,5):
    sampledPoints = InIsampledPoints*val
    val = val*2
    print(sampledPoints)

    sampVals = np.ndarray((sampledPoints+1, sampledPoints + 1))

    for x in range(0,sampledPoints+1):
        for y in range(0,sampledPoints+1):
            if(x == sampledPoints):
                sampVals[x,y] = sampVals[0,y]
            elif(y == sampledPoints):
                sampVals[x,y] = sampVals[x,0]
            else:
                sampVals[x,y] = random.random()


    for i in range(0,sampledPoints):
        for j in range(0,sampledPoints):
            startY = (j*sizeY)//sampledPoints
            endY = ((j+1)*sizeY)//sampledPoints
            lengthY = endY-startY
            for y in range(startY, endY):
                a = (sampVals[i,j+1]*(y-startY)/lengthY + (1-(y-startY)/lengthY)*sampVals[i,j])
                b = (sampVals[i+1,j+1]*(y-startY)/lengthY + (1-(y-startY)/lengthY)*sampVals[i+1,j])

                startX = (i*sizeX)//sampledPoints
                endX = ((i+1)*sizeX)//sampledPoints
                lengthX = endX-startX
                for x in range(startX, endX):
                    img[x,y] = img[x,y] + ((1-(x-startX)/lengthX)*a + ((x-startX)/lengthX)*b)/val
                    #print(img[x,y])


maxN=0
for x in range(0,sizeX):
    for y in range(0,sizeY):
        if (maxN<img[x,y]):
            maxN = img[x,y]

for x in range(0,sizeX):
    for y in range(0,sizeY):
        img[x,y] = img[x,y]/maxN

cv2.imshow("ss", img)
cv2.waitKey(0)