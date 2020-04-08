# -*- coding: utf-8 -*-
"""
This file imports an image and sets a scale bar.
Created 2020/02/21 by Gabriella Bruno.
Useful revisions for future:
    1. center scale bar value relative scale bar
    2. read scale bar value directly from image
"""
def scale_bar(image_with,image,bar_value,save_name,name=None):
    from PIL import Image, ImageDraw, ImageFont
    import math as m
    from collections import Counter
    #import picture with scale bar
    im=Image.open(image_with,'r')
    #get size of image in columns,rows
    c,r=im.size
    #get data from pixels going row to row
    pix_val=list(im.getdata(0))
    #get values equal to 0 which represent scale bar
    z=[i for i, r in enumerate(pix_val) if r == 0]
    #count zeros in each row
    z=[m.floor(i/c) for i in z]
    #get number of pixels
    n=Counter(z)
    n=n.most_common(1)
    n=n[0][1]
    #get a length to pixel ratio in nm/pixel
    ratio=bar_value/n
    #import picture without scale bar
    im=Image.open(image,'r')
    #redraw image
    new=ImageDraw.Draw(im)
    #draw scale bar
    new.rectangle([20,c-30,20+n,c-20],fill='white',outline='black')
    #change font size of scale bar value
    ft=ImageFont.truetype('C:\WINDOWS\FONTS\BASKVILL.TTF', 100)
    #draw scale bar value
    new.text((0,0.87*c),str(bar_value)+' nm',fill='white',font=ft)
    #insert name in top left corner (optional)
    if name!=None:
        new.text((0,0),str(name),fill='white',font=ft)
    #save image as something new
    im.save(save_name+'.png')
    return z,new

#test
x,y=scale_bar('SI_EDS-HAADF-DF4-DF2-BF_1433-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1433 no scale-Cr-int.png',50,'test','Cr')