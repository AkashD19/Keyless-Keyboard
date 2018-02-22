from cv2 import *
import os
import numpy as np
from time import sleep
flag =0

#temp = [0,0,0,0,0,0] #b,r,g
temp1,temp2,temp0 = 0.0,0,0

global blu,re, gre
blu,re,gre = 0,0,0
def nothing(x):
    pass
def clear():
    os.system('CLS')

#def data(str):
#    data = data+str
#    print data
#480,640,3

def green(a,b,c,d,resetb):
    c = a+(c/2)             #r = row || c = column
    r = b+(d/2)
    #print "-----------------",c,r
    if((c>200)and(c<441))and((r>150)and(r<331)):
        resetb = 1
    if((((c>=0)and(c<201))and((r>=0)and(r<151)))and (resetb == 1)):
        #data("I")
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
    





cam = VideoCapture(0)
sleep(0.5)
namedWindow('Track')
##createTrackbar('Blue','Track',50,255,nothing)






## 1.BLUE  2.RED
while True:
    
    flag = 0    
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
                temp0 = 0
                blu = 1
            flag= 1
            temp0 = blue(x,y,w,h,temp0)
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
                temp1=0
                re = 1
            #flag = 3
            temp1 = red(xr,yr,wr,hr,temp1)
            rectangle(img,(xr,yr),(xr+wr,yr+hr),(0,0,255),3)
    ##-------------------------------- RED

    ##-------------------------------- GREEN
    _,img = cam.read()
    img = flip(img,1)
    imgg = img[:,:,1]
    grg = cvtColor(img, COLOR_BGR2GRAY)
    imggreen = subtract(imgg,grg)
    ##imshow('1',imgg)

    _,bwg = threshold(imggreen,50,255,THRESH_BINARY)
    imshow('2',bwg)
    
    contoursg,_ = findContours(bwg.copy(),RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    for ig in contoursg:
        xg,yg,wg,hg = boundingRect(ig)
        if(wg*hg>4000):
            blu,re = 0,0
            if gre == 0:
                temp2=0
                gre = 1
            #flag = 2
            temp2 = green(xg,yg,wg,hg,temp2)
            rectangle(img,(xg,yg),(xg+wg,yg+hg),(0,255,0),3)
    ##-------------------------------- GREEN


    imshow('3',img)

#    if flag==2:
#        print "green"
#     elif flag==2:
#        print "red"

    
    if waitKey(10)==32:
        print data+" "
        break
    if waitKey(1)==27:
        break
    elif flag==4:
        break

cam.release()
destroyAllWindows()

