import sys, pygame
from PIL import Image
img = Image.open('maze.png')
background = [img]
size = width, height = 180, 180
screen = pygame.display.set_mode([180,180])

# Plan coordinate system
# Starting coordinates: (15-19, 0-4)
# Ending coordinates: (45-49, 180-184)
# Marker: 5px
# Each coordinate: 5px by 5px


# Recognizing black/white
print(img.size)
size = [img.size]
print(size[0])
colors = img.getcolors()
print(colors)
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)
print(list[2])

# Print the starting coordinate
print(list[2],",",177)

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)
print(list[2])

# Locate the ending coordinate
print (list[2],",",3)                                                                