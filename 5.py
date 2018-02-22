from cv2 import *
import numpy as np
from pykeyboard import PyKeyboard
from time import sleep

sleep(20)
keyboard = PyKeyboard()
def nothing(x):
    pass


cam = VideoCapture(0)
sleep(0.5)
namedWindow('red')
createTrackbar('thr','red',40,255,nothing)

ix,iy = -1,-1
t = 0
k = 0
flag = 0
while True: 
    _,img=cam.read()
    img = flip(img,1)
    gr = cvtColor(img,COLOR_BGR2GRAY)
    red = img[:,:,2]
    res = subtract(red, gr)
    thr = getTrackbarPos('thr','red')
    _,bw = threshold(res, thr, 255,THRESH_BINARY)
    contours,_ = findContours(bw.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h = boundingRect(cnt)
        iix,iiy = x+(w/2) ,y+(h/2)
        if  iy > iiy and iy - iiy > 30 and ((ix - iix < 7 and ix - iix >0)or (iix - ix < 7 and iix - ix>0)) :
            print 'up'
            keyboard.press_key('w')
            sleep(0.1)
            
        elif ix > iix and ix - iix > 30 and ((iy - iiy < 7 and iy - iiy > 0)or (iiy - iy < 7 and iiy - iy>0)) :
            print 'left'
            keyboard.press_key('a')
            sleep(0.1)
            keyboard.release_key('a')
            
        elif ix < iix and iix - ix > 30 and ((iy - iiy < 7 and iy - iiy > 0)or (iiy - iy < 7 and iiy - iy>0)):
            print 'right'
            keyboard.press_key('d')
            sleep(0.1)
            keyboard.release_key('d')            
        elif iy < iiy and iiy - iy > 30 and ((ix - iix < 7 and ix - iix >0)or (iix - ix < 7 and iix - ix>0)):
            print 'down'
            keyboard.release_key('w')
            keyboard.press_key('s')
            sleep(0.1)
            keyboard.release_key('s')            
        if w*h > 100:
            rectangle(img, (x,y), (x+w,y+h),(0,0,255),2)
            k = k+1
            if k == 20:
                ix,iy = x+(w/2) ,y+(h/2)
                k = 0
    

    imshow('img',img)
    if waitKey(1) == 27:
        break

    
cam.release()
destroyAllWindows()
