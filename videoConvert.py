# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#Edited by Ross Lakey

import math
import time
from PIL import Image
import sys, os

currentframe = 44 #number of image frames in the frames file
with open('vid.txt', 'w') as f: 
  f.truncate()# delete previously stored video entries
  f.write(str(currentframe*360*72)) # print 
  f.write(',')

for v in range(1,currentframe): #loop through all image frames
  if (v<10):
    FILENAME = "frames/ezgif-frame-00" + str(v)+".jpg"  # Image file to load
  else:
    FILENAME = "frames/ezgif-frame-0" + str(v)+".jpg"  # Image file to load
    

  # Load image in RGB format and get dimensions:
  print("Loading...")
  IMG = Image.open(FILENAME).convert("RGB")
  PIXELS = IMG.load()
  WIDTH = IMG.size[0]
  HEIGHT = IMG.size[1]
  print("%dx%d pixels" % IMG.size) # print image dimensions
  print(WIDTH)
  print(HEIGHT)
  offset = 0
  if (HEIGHT!=WIDTH): #if image is not 1:1 dimensions, add in offset so as to cut circle out of the centre of the image
    offset = (WIDTH-HEIGHT)/2
    

# Create gamma correction table
  GAMMA = bytearray(256)
  brightness = 0.25
  for i in range(256):
     GAMMA[i] = int(pow(float(i) / 255.0, 2.7) * brightness * 255.0 + 0.5)

  # Allocate list of lists, one for each column of image.
  print("Allocating...")
  COLUMN = [0 for x in range(HEIGHT)]
  for x in range(HEIGHT):
    COLUMN[x] = [[0, 0, 0, 0] for _ in range(HEIGHT)]
  
print("Converting to gamma colours")
  for x in range(HEIGHT):  # For each column of image
    for y in range(HEIGHT):  # For each pixel in column
      value = PIXELS[x+offset, y]  # Read RGB pixel in image using Offset, offset is set to zero in the case of 1:1 image dimensions
      COLUMN[x][y][0] = GAMMA[value[0]]  # Gamma-corrected R
      COLUMN[x][y][1] = GAMMA[value[1]]  # Gamma-corrected G
      COLUMN[x][y][2] = GAMMA[value[2]]  # Gamma-corrected B
      COLUMN[x][y][3] = 0.5  # Brightness

print("Printing to textfile")
#create array for final rgb value outputs
  FINAL = [0 for x in range(361)]
  for x in range(361):
    FINAL[x] = [[0,0] for _ in range(72)]
  ratio = (HEIGHT/2)/36
  distance = 0.0
  offset2=(HEIGHT/2)-1 #offset to ensure pixels are cut from the center of the image
  for x in range(361):  # 360 degrees
    for y in range(72):  # For each LED in the strip
      distance = ratio * (y-36) #Find distance from from center at which the LED is placed
      fx = round((distance * math.cos(math.radians(x)))+offset2)  #find x co-ordinate
      fy = round((-1 * distance * math.sin(math.radians(x))) + offset2) #find y co-ordinate
      #print("x point is", x, " and y point is ", y)
      #print("x is", fx, " and y is ", fy)
      r = COLUMN[fx][fy][0] << 16 # Gamma-corrected R
      g = COLUMN[fx][fy][1] << 8 # Gamma-corrected G
      b = COLUMN[fx][fy][2]  # Gamma-corrected B
      #FINAL[x][y][0] = fx
      #FINAL[x][y][1] = fy
      FINAL[x][y] = r+g+b


  with open('vid.txt', 'a') as f: #print values to video file
    for n in range(361):
      for m in range(72):
        f.write(str(FINAL[n][m]))
        f.write(',')
