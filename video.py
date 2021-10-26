# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

#!/usr/bin/python3

# Persistence-of-vision (POV) example for Adafruit DotStar RGB LED strip.
# Loads image, displays column-at-a-time on LEDs at very high speed,
# suitable for naked-eye illusions.
# See dotstar_simpletest.py for a much simpler example script.
# See dotstar_image_paint.py for a slightly simpler light painting example.
# This code accesses some elements of the dotstar object directly rather
# than through function calls or setters/getters...this is poor form as it
# could break easily with future library changes, but is the only way right
# now to do the POV as quickly as possible.
# May require installing separate libraries.

import math
import time
from PIL import Image
import cv2 
import os 

video = cv2.VideoCapture('rotate.mp4') 
try:  
	if not os.path.exists('frames'): 
		os.makedirs('frames') 
except OSError: 
	print ('Error') 
currentframe = 0
while(True): 
	ret,frame = video.read() 

	if ret: 
		name = './frames/frame' + str(currentframe) + '.png'
		print ('Captured...' + name) 
		cv2.imwrite(name, frame) 
		currentframe += 1
	else: 
		break
video.release() 
cv2.destroyAllWindows()
with open('vid.txt', 'w') as f:
  f.truncate()
	f.write(str(currentframe*360*72))
	f.write(',')
	
for v in range(currentframe):
  
  FILENAME = "frame" + str(l)+".png"  # Image file to load


  # Load image in RGB format and get dimensions:
  print("Loading...")
  #time.sleep(20000)
  IMG = Image.open(FILENAME).convert("RGB")
  PIXELS = IMG.load()
  WIDTH = IMG.size[0]
  HEIGHT = IMG.size[1]
  print("%dx%d pixels" % IMG.size)
  print(WIDTH)
  print(HEIGHT)
  offset = 0
  if (HEIGHT!=WIDTH):
    offset = (WIDTH-HEIGHT)/2
    

  # Calculate gamma correction table, makes mid-range colors look 'right':
  GAMMA = bytearray(HEIGHT)
  brightness = 0.25
  for i in range(HEIGHT):
    GAMMA[i] = int(pow(float(i) / 255.0, 2.7) * brightness * 255.0 + 0.5)

  # Allocate list of lists, one for each column of image.
  print("Allocating...")
  COLUMN = [0 for x in range(HEIGHT)]
  for x in range(WIDTH):
    COLUMN[x] = [[0, 0, 0, 0] for _ in range(HEIGHT)]
  
  # Convert entire RGB image into columnxrow 2D list.
  print("Converting...")
  for x in range(HEIGHT):  # For each column of image
    for y in range(HEIGHT):  # For each pixel in column
      value = PIXELS[x+offset, y]  # Read RGB pixel in image
      COLUMN[x][y][0] = GAMMA[value[0]]  # Gamma-corrected R
      COLUMN[x][y][1] = GAMMA[value[1]]  # Gamma-corrected G
      COLUMN[x][y][2] = GAMMA[value[2]]  # Gamma-corrected B
      COLUMN[x][y][3] = 0.5  # Brightness

  print("Displaying...")

  FINAL = [0 for x in range(360)]
  for x in range(360):
    FINAL[x] = [[0,0] for _ in range(72)]
  ratio = HEIGHT/36
  distance = 0.0
  offset2=(HEIGHT/2)-1
  for x in range(360):  # For each column of image
    for y in range(72):  # For each pixel in column
      distance = ratio * (y-36)
      fx = round((distance * math.cos(math.radians(x)))+offset2)
      fy = round((-1 * distance * math.sin(math.radians(x))) + offset2)
      #print("x point is", x, " and y point is ", y)
      #print("x is", fx, " and y is ", fy)
      r = COLUMN[fx][fy][0] << 16 # Gamma-corrected R
      g = COLUMN[fx][fy][1] << 8 # Gamma-corrected G
      b = COLUMN[fx][fy][2]  # Gamma-corrected B
      #FINAL[x][y][0] = fx
      #FINAL[x][y][1] = fy
      FINAL[x][y] = r+g+b

  print(FINAL[0])

  with open('readme.txt', 'w') as f:
    for n in range(360):
      for m in range(72):
        f.write(str(FINAL[n][m]))
        f.write(',')

