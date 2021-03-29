import numpy as np
import cv2
import random
import time
import math

size=800

plotTheta = np.zeros((900,900),dtype=float)
plotXY = np.zeros((900,900),dtype=float)

c = [0]*900
c2 = [0]*900

'''using X and Y value'''

for i in range(0,100000):
    x = random.randint(1,size-1)
    y = random.randint(1,size-1)
    #print(x,y)
    ang = int(1800*((math.atan(x/y))/math.pi))
    c[ang] += 1

for i in range(0,900):
    plotXY[c[i],i] = 1


'''using anfgular values'''
for i in range(0,100000):
    theta = random.randint(0,899)
    c2[theta] += 1

for i in range(0,900):
    plotTheta[c2[i],i] = 1


cv2.imshow("usingXY" ,plotXY)
cv2.imshow("usingTheta" ,plotTheta)
cv2.waitKey(0)