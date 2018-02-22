from cv2 import *
import numpy as np
from time import sleep

def nothing(x):
    pass

cam = VideoCapture(0)
sleep(0.5)
namedWindow('Track')
##createTrackbar('Blue','Track',50,255,nothing)

## 1.BLUE  2.RED
while True:
    
    
    ##-------------------------------- BLUE
    _,img=cam.read()
    img =flip(img,1)
    gr = cvtColor(img, COLOR_BGR2GRAY)
    imgb = img[:,:,0]
    imgbl = subtract(imgb,gr)
    ##imshow('1',imgb)

    _,bw = threshold(imgbl,50,255,THRESH_BINARY)
    ##imshow('2',bw)

    contoursb,_ = findContours(bw.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for i in contoursb:
        x,y,w,h = boundingRect(i)
        if(w*h>150):
            flag = 1
            rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    ##-------------------------------- BLUE
    
        
    ##-------------------------------- RED
    ##_,img = cam.read()
    imgr = img.copy()
    imgr =flip(imgr,1)
    imgr = imgr[:,:,2]
    grr = cvtColor(imgr, COLOR_BGR2GRAY)
    imgr = subtract(imgr,grr)
    ##imshow('1',imgr)

    _,bwr = threshold(imgr,50,255,THRESH_BINARY)
    ##imshow('2',bwr)

    contoursr,_ = findContours(bwr.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for ir in contoursr:
        xr,yr,wr,hr = boundingRect(i)
        if(wr*hr>150):
            flag = 2
            rectangle(img,(xr,yr),(xr+wr,yr+hr),(0,0,255),3)
    ##-------------------------------- RED


    imshow('3',img)

    if flag==1:
        print blue
    elif flag==2:
        print red


    if waitKey(1)==27:
        break

cam.release()
destroyAllWindows()

