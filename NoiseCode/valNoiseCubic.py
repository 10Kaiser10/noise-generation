import numpy as np
import cv2
import random
import time

size = 600
sampledPoints = 3

img = np.ndarray((size+1,size+1))

for i in range(0,sampledPoints+1):
    x = (i*size)//sampledPoints
    for j in range(0,sampledPoints+1):
        y = (j*size)//sampledPoints
        if(i == sampledPoints):
            img[x,y] = img[0,y]
        elif(j == sampledPoints):
            img[x,y] = img[x,0]
        else:
            img[x,y] = random.random()

for i in range(0,sampledPoints+1):
    for j in range(0,sampledPoints):
        if(j == 0):
            p = img[((i)*size)//sampledPoints, ((j)*size)//sampledPoints]
            s = img[((i)*size)//sampledPoints, ((j+2)*size)//sampledPoints]
        elif(j == sampledPoints-1):
            s = img[((i)*size)//sampledPoints, ((j+1)*size)//sampledPoints]
            p = img[((i)*size)//sampledPoints, ((j-1)*size)//sampledPoints]
        else:
            p = img[((i)*size)//sampledPoints, ((j-1)*size)//sampledPoints]
            s = img[((i)*size)//sampledPoints, ((j+2)*size)//sampledPoints]

        #p = img[((i)*size)//sampledPoints, ((j-1)*size)//sampledPoints]
        q = img[((i)*size)//sampledPoints, ((j)*size)//sampledPoints]
        r = img[((i)*size)//sampledPoints, ((j+1)*size)//sampledPoints]
        #s = img[((i)*size)//sampledPoints, ((j+2)*size)//sampledPoints]

        #print(str(p) + "," + str(q) + ","+str(r) + ","+str(s))

        a = -0.5*p + 1.5*q - 1.5*r + 0.5*s
        b = p - 2.5*q + 2*r - 0.5*s
        c = -0.5*p + 0.5*r
        d = q

        startY = (j*size)//sampledPoints
        endY = ((j+1)*size)//sampledPoints
        lengthY = endY-startY

        for y in range(startY+1,endY):
            f = (y-startY)/lengthY
            img[((i)*size)//sampledPoints,y] = a*f*f*f + b*f*f + c*f + d

for j in range(0,size+1):
    for i in range(0, sampledPoints):
        if(i == 0):
            p = img[((i)*size)//sampledPoints, j]
            s = img[((i+2)*size)//sampledPoints, j]
        elif(i == sampledPoints-1):
            s = img[((i-1)*size)//sampledPoints, j]
            p = img[((i+1)*size)//sampledPoints, j]
        else:
            p = img[((i-1)*size)//sampledPoints, j]
            s = img[((i+2)*size)//sampledPoints, j]

        q = img[((i)*size)//sampledPoints, j]
        r = img[((i+1)*size)//sampledPoints, j]

        #print(str(p) + "," + str(q) + ","+str(r) + ","+str(s))

        a = -0.5*p + 1.5*q - 1.5*r + 0.5*s
        b = p - 2.5*q + 2*r - 0.5*s
        c = -0.5*p + 0.5*r
        d = q

        startX = (i*size)//sampledPoints
        endX = ((i+1)*size)//sampledPoints
        lengthX = endX-startX

        for x in range(startX+1,endX):
            f = (x-startX)/lengthX
            img[x,j] = a*f*f*f + b*f*f + c*f + d
cv2.imwrite(r"C:\Users\shiva\Desktop\Noise Generation\noise3.jpg", 255*img)
cv2.imshow("cubic" ,img)
cv2.waitKey(0)

