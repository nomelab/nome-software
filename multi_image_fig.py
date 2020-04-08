# -*- coding: utf-8 -*-
"""
Create figures with multiple images.
Created 2020/02/21 by Gabriella Bruno.
Useful revisions for future:
    1. input option to place subfigure labels below or outside of image
"""
def multi_image_fig(pic_list,col,spacing,save_name,label=None):
    from PIL import Image, ImageDraw, ImageFont
    import math as m
    #list of alphabet
    sub=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
    #font of label
    ft=ImageFont.truetype('C:\WINDOWS\FONTS\BASKVILL.TTF', 100)
    #load images from list
    im=[Image.open(i,'r') for i in pic_list]
    #get size of image in columns,rows
    c,r=im[0].size
    #get width of new image
    width=c*col+spacing*(col-1)
    #get height of new image
    height=m.ceil(len(pic_list)/col)*(r+spacing-1)
    #create new image
    txt = Image.new('RGB',(width,height),'white')
    #draw existing images on images
    for i in list(range(len(pic_list)-(len(pic_list)%col))):
        #column
        xpos=m.floor(i/col)
        #row
        ypos=i%col
        #actual x location
        y=xpos*(c+spacing)
        #actual y location
        x=ypos*(r+spacing)
        txt.paste(im[i],(x,y))
        if label==None:
            ImageDraw.Draw(txt).text((x,y),'('+sub[i]+')',fill='white',font=ft)
    if len(pic_list)%col != 0:
        #center images on last row
        last=len(pic_list)%col
        for i in list(range(len(pic_list)-last,len(pic_list))):
            xpos=m.floor(i/col)
            ypos=i%col
            y=xpos*(c+spacing)
            x=int((width-(last*(r+spacing-1)))/2)+(ypos*r)
            txt.paste(im[i],(x,y))
            if label==None:
                ImageDraw.Draw(txt).text((x,y),'('+sub[i]+')',fill='white',font=ft)
    #save image
    txt.save(save_name+'.png')
    return height

ris1433=['SI EDS-HAADF-DF4-DF2-BF 1433-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 1433-C-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-V-int.png']
c=multi_image_fig(ris1433,4,0,'ris1433',label='no')
ris1611=['SI EDS-HAADF-DF4-DF2-BF 1611-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 1611-C-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Si-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-V-int.png']
c=multi_image_fig(ris1611,3,0,'ris1611',label='no')
ris1058=['SI EDS-HAADF 1058 scale-HAADF.png','SI EDS-HAADF 1058 scale-C-int.png','SI EDS-HAADF 1058 scale-Cr-int.png','SI EDS-HAADF 1058 scale-Fe-int.png','SI EDS-HAADF 1058 scale-Mn-int.png','SI EDS-HAADF 1058 scale-Mo-int.png','SI EDS-HAADF 1058 scale-Ni-int.png','SI EDS-HAADF 1058 scale-Si-int.png','SI EDS-HAADF 1058 scale-V-int.png']
c=multi_image_fig(ris1058,3,0,'ris1058',label='no')
dis1433=['SI EDS-HAADF-DF4-DF2-BF 1433-BF.png']
c=multi_image_fig(dis1433,1,0,'dis1433',label='no')

#test and older versions
'''
pics=['SI_EDS-HAADF-DF4-DF2-BF_1433-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1433 no scale-Cr-int.png','test.png']
ris1433=['SI EDS-HAADF-DF4-DF2-BF 1433-BF.png','SI EDS-HAADF-DF4-DF2-BF 1433-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 1433-C-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-DF2.png','SI EDS-HAADF-DF4-DF2-BF 1433-DF4.png','SI EDS-HAADF-DF4-DF2-BF 1433-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 1433-V-int.png']
c=multi_image_fig(ris1433,4,0,'ris1433',label='no')
ris1611=['SI EDS-HAADF-DF4-DF2-BF 1611-BF.png','SI EDS-HAADF-DF4-DF2-BF 1611-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 1611-C-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-DF2.png','SI EDS-HAADF-DF4-DF2-BF 1611-DF4.png','SI EDS-HAADF-DF4-DF2-BF 1611-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-Si-int.png','SI EDS-HAADF-DF4-DF2-BF 1611-V-int.png']
c=multi_image_fig(ris1611,4,0,'ris1611',label='no')
ris0934=['SI EDS-HAADF-DF4-DF2-BF 0934-BF.png','SI EDS-HAADF-DF4-DF2-BF 0934-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 0934-C-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-DF2.png','SI EDS-HAADF-DF4-DF2-BF 0934-DF4.png','SI EDS-HAADF-DF4-DF2-BF 0934-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-Si-int.png','SI EDS-HAADF-DF4-DF2-BF 0934-V-int.png']
c=multi_image_fig(ris1611,4,0,'ris0934',label='no')
ris1008=['SI EDS-HAADF-DF4-DF2-BF 1008-BF.png','SI EDS-HAADF-DF4-DF2-BF 1008-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 1008-C-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-DF2.png','SI EDS-HAADF-DF4-DF2-BF 1008-DF4.png','SI EDS-HAADF-DF4-DF2-BF 1008-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-Si-int.png','SI EDS-HAADF-DF4-DF2-BF 1008-V-int.png']
c=multi_image_fig(ris1611,4,0,'ris1008',label='no')
ris1058=['SI EDS-HAADF-DF4-DF2-BF 1058-BF.png','SI EDS-HAADF-DF4-DF2-BF 1058-HAADF.png','SI EDS-HAADF-DF4-DF2-BF 1058-C-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-Cr-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-DF2.png','SI EDS-HAADF-DF4-DF2-BF 1058-DF4.png','SI EDS-HAADF-DF4-DF2-BF 1058-Fe-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-Mn-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-Mo-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-Ni-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-Si-int.png','SI EDS-HAADF-DF4-DF2-BF 1058-V-int.png']
c=multi_image_fig(ris1611,4,0,'ris1058',label='no')
'''