#!/usr/bin/env python
# coding: utf-8

# In[36]:


import cv2
import os
from os.path import isfile, join
import numpy as np
import argparse


# In[ ]:


parser=argparse.ArgumentParser()
parser.add_argument("-i","--i_dir",help="Enter the Input directory",type=str,required=True)
parser.add_argument("-o","--o_dir",help="Enter the Output directory",type=str,required=True)
args=parser.parse_args()


# In[31]:


global image
global cache
global width
global xi,yi
width = 362

dir=args.i_dir
files = [f for f in os.listdir(dir) if os.path.isfile(join(dir, f))]
files.sort()


# In[32]:



op_dir=args.o_dir

try:
    os.mkdir(op_dir)
except OSError as error:
    print(error)


# In[33]:


def res(i):
    if i<0:
        i=99
    elif i>99:
        i=0
    else:
        i=i
    return i 


# In[34]:


# Mouse callback function. Gets called when mouse events happen.
def drawRect(event,x,y,flags,param):
    global image
    global width
    global xi,yi

#This if statement is enabled when the leftmouse is double clicked.
#if and elif statements are used to restrict the values of x and y so that the selected rectangle does not go out of bounds and give an error while saving the crop.
    if event==cv2.EVENT_LBUTTONDBLCLK:
        xy=(image.shape[1],image.shape[0])
        if x-width<0 and y-width<0:                                    
            x=x+abs(x-width)                                           
            y=y+abs(y-width)
        elif y-width<0 and x+width>xy[0]:
            y=y+abs(y-width)
            x=x=x-(x+width-xy[0])
        elif x-width<0 and y+width>xy[1]:
            x=x+abs(x-width)
            y=y-(y+width-xy[1])
        elif x+width>xy[0] and y+width>xy[1]:
            x=x-(x+width-xy[0])
            y=y-(y+width-xy[1])
        elif x-width<0:
            x=x+abs(x-width)
        elif y-width<0:
            y=y+abs(y-width)
        elif x+width>xy[0]:
            x=x-(x+width-xy[0])
        elif y+width>xy[1]:
            y=y-(y+width-xy[1])
        
        cv2.rectangle(image,(x-width,y-width),(x+width,y+width),(255,0,255),2)
        xi=x
        yi=y
        cv2.imshow("Image",image)
        
#If statement is activated when the middle mouse is pressed down.
#Used to reset the image if any mistake happens.
    if event==cv2.EVENT_MBUTTONDOWN:
        image=cv2.imread(dir+fname)
        cv2.putText(image,fname,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv2.imshow("Image",image)


# In[35]:


i=0
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Image",drawRect)

fname=files[i]
image=cv2.imread(dir+fname)
cv2.putText(image,fname,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
cv2.imshow("Image",image)

while True:
    key=cv2.waitKey(0)
    if key==ord('q'):
        break

    elif key==ord('m'):
        i+=1
        i=res(i)
        fname=files[i]
        image=cv2.imread(dir+fname)
        cv2.putText(image,fname,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv2.imshow("Image",image)

    elif key==ord('n'):
        i=i-1
        i=res(i)
        fname=files[i]
        image=cv2.imread(dir+fname) 
        cv2.putText(image,fname,(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
        cv2.imshow("Image",image)

    elif key==ord('g'):
        crop=image[yi-width+2:yi+width-2,xi-width+2:xi+width-2]
        #cv2.imshow('crop_img',crop)
        filename=op_dir+fname
        cv2.imwrite(filename, crop)

    elif key==ord('r'):
        i=res(i)
        fname=files[i]
        image=cv2.imread(dir+fname) 
        cv2.imshow("Image",image)

    elif key==ord('1'):
        width=362
    elif key==ord('2'):
        width=422
    elif key==ord('3'):
        width=482
    elif key==ord('4'):
        width=542
    elif key==ord('5'):
        width=602


cv2.destroyAllWindows()


# In[ ]:




