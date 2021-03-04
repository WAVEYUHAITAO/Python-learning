#! /usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os
im=Image.new('RGBA',(200,200),'white')
draw=ImageDraw.Draw(im)
draw.line([(0,0),(150,0),(150,150),(0,150),(0,0)],fill='black')
draw.rectangle((20,30,60,60),fill='blue')
draw.ellipse((120,30,160,60),fill='red',outline='purple')
draw.polygon(((57,87),(79,62),(94,85),(120,90),(103,113)),fill='brown')
for i in range(100,200,10):
    draw.line([(i,0),(200,i-100)],fill='green')
draw.text((20,150),'Hello',fill='purple')
fontsFolder='/Library/Fonts'
arialFont=ImageFont.truetype(os.path.join(fontsFolder,'Arial Unicode.ttf'),32)
draw.text((100,150),'Howdy',fill='gray',font=arialFont)
im.save('drawing.png')