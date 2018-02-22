from cv2 import *
import numpy as np
from time import sleep
flag =0
global data
data = ""
temp = [0,0,0,0,0,0] #b,r,g
global blu,re,gre
blu,re,gre = 0,0,0
def nothing(x):
    pass


#480,640,3


def blue(a, b, c, d, resetb):
    c = a+(c/2)             #r = row || c = column
    r = b+(d/2)
    #print "-----------------",c,r
    if((c>200)and(c<441))and((r>150)and(r<331)):
        resetb = 1
    if((((c>=0)and(c<201))and((r>=0)and(r<151)))and (resetb == 1)):
        print "A"
        resetb = 0
    elif((((c>=441)and(c<640))and((r>=0)and(r<151)))and (resetb == 1)):
        print "B"
        resetb = 0
    elif((((c>=0)and(c<201))and((r>=331)and(r<480)))and (resetb == 1)):
        print "C"
        resetb = 0
    elif((((c>=441)and(c<640))and((r>=331)and(r<480)))and (resetb == 1)):
        print "D"
        resetb = 0
    return resetb
    

def red(a, b, c, d, resetb):
    c = a+(c/2)             #r = row || c = column
    r = b+(d/2)
    #print "-----------------",c,r
    if((c>200)and(c<441))and((r>150)and(r<331)):
        resetb = 1
    if((((c>=0)and(c<201))and((r>=0)and(r<151)))and (resetb == 1)):
        print "E"
        resetb = 0
    elif((((c>=441)and(c<640))and((r>=0)and(r<151)))and (resetb == 1)):
        print "F"
        resetb = 0
    elif((((c>=0)and(c<201))and((r>=331)and(r<480)))and (resetb == 1)):
        print "G"
        resetb = 0
    elif((((c>=441)and(c<640))and((r>=331)and(r<480)))and (resetb == 1)):
        print "H"
        resetb = 0
    return resetb
    

def green(a, b, c, d, resetb):
    c = a+(c/2)             #r = row || c = column
    r = b+(d/2)
    #print "-----------------",c,r
    if((c>200)and(c<441))and((r>150)and(r<331)):
        resetb = 1
    if((((c>=0)and(c<201))and((r>=0)and(r<151)))and (resetb == 1)):
        print "I"
        resetb = 0
    elif((((c>=441)and(c<640))and((r>=0)and(r<151)))and (resetb == 1)):
        print "J"
        resetb = 0
    elif((((c>=0)and(c<201))and((r>=331)and(r<480)))and (resetb == 1)):
        print "K"
        resetb = 0
    elif((((c>=441)and(c<640))and((r>=331)and(r<480)))and (resetb == 1)):
        print "L"
        resetb = 0
    return resetb




cam = VideoCapture(0)
sleep(0.5)
namedWindow('Track')
##createTrackbar('Blue','Track',50,255,nothing)






## 1.BLUE  2.RED
while True:
    
    #flag = 0    
    ##-------------------------------- BLUE
    _,img = cam.read()
    img = flip(img,1)
    imgb = img[:,:,0]
    gr = cvtColor(img, COLOR_BGR2GRAY)
    imgblue = subtract(imgb,gr)
    ##imshow('1',imgb)

    _,bw = threshold(imgblue,50,255,THRESH_BINARY)
    ##imshow('2',bw)

    contoursb,_ = findContours(bw.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for i in contoursb:
        x,y,w,h = boundingRect(i)
        if(w*h>4000):
            re,gre = 0,0
            if blu == 0:
                temp[0] = 0
                blu = 1
            #flag= 1
            temp[0] = blue(x,y,w,h,temp[0])
            rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    ##-------------------------------- BLUE
    
        
    ##-------------------------------- RED
    _,img = cam.read()
    img = flip(img,1)
    imgr = img[:,:,2]
    grr = cvtColor(img, COLOR_BGR2GRAY)
    imgred = subtract(imgr,grr)
    ##imshow('1',imgr)

    _,bwr = threshold(imgred,50,255,THRESH_BINARY)
    ##imshow('2',bwr)
    
    contoursr,_ = findContours(bwr.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for ir in contoursr:
        xr,yr,wr,hr = boundingRect(ir)
        if(wr*hr>4000):
            blu,gre = 0,0
            if re == 0:
                temp[1]=0
                re = 1
            #flag = 3
            just = temp[1]
            just2 = red(xr,yr,wr,hr,just)
            temp[1] = just2
            rectangle(img,(xr,yr),(xr+wr,yr+hr),(0,0,255),3)
    ##-------------------------------- RED

    ##-------------------------------- GREEN
    _,im = cam.read()
    im = flip(im,1)
    imgg = im[:,:,1]
    #imshow('green',imgg)
    gr = cvtColor(im, COLOR_BGR2GRAY)
    imggreen = subtract(imgg,gr)
    #imshow('1',imggreen)

    _,bwg = threshold(imggreen,50,255,THRESH_BINARY)
    imshow('2',bwg)
    
    contoursg,_ = findContours(bwg.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for ig in contoursg:
        xg,yg,wg,hg = boundingRect(ig)
        if(wg*hg>200):
            blu,red = 0,0
            if gre == 0:
                temp[2]=0
                gre = 1
            #flag = 2
            temp[2] = green(xg,yg,wg,hg,temp[2])
            rectangle(im,(xg,yg),(xg+wg,yg+hg),(0,255,0),3)
    ##-------------------------------- GREEN

    

    


    imshow('3',img)

#    if flag==2:
#        print "green"
#     elif flag==2:
#        print "red"

    
    if waitKey(10)==32:
        print data+"a"
        break
    if waitKey(1)==27:
        break
    elif flag==4:
        break

cam.release()
destroyAllWindows()

