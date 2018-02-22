from cv2 import *
import numpy as np
from time import sleep
from pykeyboard import PyKeyboard

keyboard = PyKeyboard()

def nothing(x):
    pass

#480, 640
cam = VideoCapture(0)

sleep(0.5)
namedWindow('red')
namedWindow('Track')
createTrackbar('s2','Track',7,40,nothing)
createTrackbar('s1','Track',20,80,nothing)
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
    #imshow('red',red)
    res = subtract(red, gr)
    #imshow('res',res)
    s1 = getTrackbarPos('s1','Track')
    s2 = getTrackbarPos('s2','Track')
    thr = getTrackbarPos('thr','red')
    _,bw = threshold(res, thr, 255,THRESH_BINARY)
    imshow('bw',bw)
    contours,_ = findContours(bw.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x,y,w,h = boundingRect(cnt)
        if w*h > 300:
            rectangle(img, (x,y), (x+w,y+h),(0,0,255),2)
            k = k+1
            if k == 2:
                ix,iy = x+(w/2) ,y+(h/2)
                k = 0
                flag = 1
            if flag == 1:
                iix,iiy = x+(w/2) ,y+(h/2)
                if  iy > iiy and iy - iiy > s1 and ((ix - iix < s2 and ix - iix >0)or (iix - ix < s2 and iix - ix>0)) :
                    keyboard.press_key('w')
                    sleep(0.0001)
                    print 'up'
                elif iix < 360 and ix > iix and ix - iix > s1 and ((iy - iiy < s2 and iy - iiy > 0)or (iiy - iy < s2 and iiy - iy>0)) :
                    keyboard.release_key('d')
                    keyboard.press_key('a')
                    #keyboard.press_key('w')
                    sleep(0.0001)
                    print 'left'
                    
                elif iix > 280 and ix < iix and iix - ix > s1 and ((iy - iiy < s2 and iy - iiy > 0)or (iiy - iy < s2 and iiy - iy>0)):
                    keyboard.release_key('a')
                    keyboard.press_key('d')
                    #keyboard.press_key('w')
                    sleep(0.0001)
                    print 'right'
                    
                elif iiy > 380 and iy < iiy and iiy - iy > s1 and ((ix - iix < s2 and ix - iix >0)or (iix - ix < s2 and iix - ix>0)):
                    keyboard.release_key('w')
                    keyboard.press_key('s')
                    sleep(0.01)
                    print 'down'
                    keyboard.release_key('s')

    t = img[:,:,2]
    imshow('img',t)
    if waitKey(1) == 27:
        break

u = img.shape
print u    


cam.release()
destroyAllWindows()
