# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#Edited by Ross Lakey

import math
import time
from PIL import Image
#NOTE: Images must be 256X256 pixels
FILENAME = "soul.png"  # Image file to load


print("Loading image")

IMG = Image.open(FILENAME).convert("RGB")
PIXELS = IMG.load()
WIDTH = IMG.size[0]
HEIGHT = IMG.size[1]
print("%dx%d pixels" % IMG.size) # print image dimensions 
print(WIDTH)
print(HEIGHT)

# Create gamma correction table
GAMMA = bytearray(256)
brightness = 0.25
for i in range(256):
    GAMMA[i] = int(pow(float(i) / 255.0, 2.7) * brightness * 255.0 + 0.5)

# Allocate list of lists, one for each column of image.
print("Allocating...")
COLUMN = [0 for x in range(WIDTH)]
for x in range(WIDTH):
    COLUMN[x] = [[0, 0, 0, 0] for _ in range(HEIGHT)]
    
print("Converting to gamma colours")
for x in range(WIDTH):  # For each column of image
    for y in range(HEIGHT):  # For each pixel in column
        value = PIXELS[x, y]  # Read RGB pixel in image
        
        COLUMN[x][y][0] = GAMMA[value[0]]  # Gamma-corrected R
        COLUMN[x][y][1] = GAMMA[value[1]]  # Gamma-corrected G
        COLUMN[x][y][2] = GAMMA[value[2]]  # Gamma-corrected B
        COLUMN[x][y][3] = 0.5  # Brightness

print("Printing to textfile")
#create array for final rgb value outputs
FINAL = [0 for x in range(361)]
for x in range(361):
    FINAL[x] = [[0,0] for _ in range(72)]
ratio = 128/36
distance = 0.0
for x in range(361):  # 360 degrees 
    for y in range(72):  # For each LED in the strip
        distance = ratio * (y-36) #Find distance from from center at which the LED is placed
        fx = round((distance * math.cos(math.radians(x)))+127) #find x co-ordinate
        fy = round((-1 * distance * math.sin(math.radians(x))) + 127) #find y co-ordinate
        
        r = COLUMN[fx][fy][0] << 16 # R value converted to bit shifted hex value
        g = COLUMN[fx][fy][1] << 8 # G value converted to bit shifted hex value
        b = COLUMN[fx][fy][2]  # B value converted to hex value
        FINAL[x][y] = r+g+b #combined hex value

with open('readme.txt', 'w') as f: #write to textfile
    f.truncate() # delete previously stored image
    for n in range(361):
        for m in range(72):
            f.write(str(FINAL[n][m]))
            f.write(',')
