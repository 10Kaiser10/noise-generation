import numpy as np
import cv2
import random
import time

sizeX = 512
sizeY = 512

img = np.ndarray((sizeX,sizeY))

for x in range(0,sizeX):
    for y in range(0,sizeY):
        img[x,y] = random.random()

cv2.imshow("img", img)
cv2.waitKey(0)