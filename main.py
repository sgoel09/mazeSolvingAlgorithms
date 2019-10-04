# Import modules
import sys, pygame, time, math
from time import sleep
from pygame.locals import *
from PIL import Image

# Initialize
img = Image.open('maze.png')
change = 3
width = img.width * change
height = img.height * change
screen = pygame.display.set_mode((width,height))
background = pygame.image.load('maze.png').convert()
newscreen = pygame.transform.scale(background, (width, height))


#Colors
color = (0, 188, 0)
white = (255, 255, 255)
black = (255, 255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 188, 0)

# Recognizing black/white
print(width, height)
size = [img.size]
print(size[0])
colors = img.getcolors()
print(colors)
pix = img.load()
list = []

# Locate the starting coordinate
for x in range(0,180):
    if pix[x,179] == (255, 255, 255, 255):
        list.append(x)

xvalueOfStart = list[0] * change
print(xvalueOfStart)

blockSize = len(list) * change

yvalueOfStart = height - blockSize

list = []

# Locate the ending coordinate
for x in range(0,180):
    if pix[x,0] == (255, 255, 255, 255):
        list.append(x)

xvalueOfEnd = list[0] * change
print(xvalueOfEnd)

pygame.draw.rect(newscreen, color, pygame.Rect(xvalueOfStart, yvalueOfStart, blockSize, blockSize))
screen.blit(newscreen, (0,0))
pygame.display.update()
time.sleep(0.1)

# Function to move forward
def moveUp(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y - blocksize, blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX
    currentY = y - blocksize
    currentX = x

# Function to move left
def moveDown(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x, y + blocksize, blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentY
    global currentX    
    currentY = y + blocksize
    currentX = x   
    
# Function to move left  
def moveLeft(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x - blocksize, y, blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x - blocksize
    currentY = y

# Function to move right
def moveRight(x, y, blocksize, newcolor):
    pygame.draw.rect(newscreen, newcolor, pygame.Rect(x, y, blockSize, blockSize))
    pygame.draw.rect(newscreen, color, pygame.Rect(x + blocksize, y, blockSize, blockSize))
    screen.blit(newscreen, (0,0))
    pygame.display.update()
    global currentX
    global currentY        
    currentX = x + blocksize
    currentY = y

#Initialization of currentX and currentY
def varsInit(x, y):
    global currentX
    global currentY
    global direction
    currentX = x
    currentY = y
    direction = 1

#Algorithm to determine direction to move if facing up
def up(replace):
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("up-Move up called")
        time.sleep(0.1)
        direction = 1
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("up-Move right called")
        time.sleep(0.1)
        direction = 2
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("up-Move left called")
        time.sleep(0.1)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("up-Move down called")
        time.sleep(0.1)
        direction = 4
    
#Algorithm to determine direction to move if facing right
def right(replace):
    global direction
    if newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("right-Move right called")
        time.sleep(0.1)
        direction = 2
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("right-Move down called")
        time.sleep(0.1)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("right-Move up called")
        time.sleep(0.1)
        direction = 1
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("right-Move left called")
        time.sleep(0.1)
        direction = 3
    
#Algorithm to determine direction to move if facing left
def left(replace):
    global direction
    if newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("left-Move left called")
        time.sleep(0.1)
        direction = 3
    elif newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("left-Move down called")
        time.sleep(0.1)
        direction = 4
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("left-Move up called")
        time.sleep(0.1)
        direction = 1
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("left-Move right called")
        time.sleep(0.1)
        direction = 2

#Algorithm to determine direction to move if facing down
def down(replace):
    global direction
    if newscreen.get_at((currentX, currentY + blockSize)) == white:#down
        moveDown(currentX, currentY, blockSize, replace)
        print("down-Move down called")
        time.sleep(0.1)
        direction = 4
    elif newscreen.get_at((currentX - blockSize, currentY)) == white:#left
        moveLeft(currentX, currentY, blockSize, replace)
        print("down-Move left called")
        time.sleep(0.1)
        direction = 3
    elif newscreen.get_at((currentX + blockSize, currentY)) == white:#right
        moveRight(currentX, currentY, blockSize, replace)
        print("down-Move right called")
        time.sleep(0.1)
        direction = 2
    elif newscreen.get_at((currentX, currentY - blockSize)) == white:#up        
        moveUp(currentX, currentY, blockSize, replace)
        print("down-Move up called")
        time.sleep(0.1)
        direction = 1

#returns boolean if current tile is intersection
def isIntersection():
    global direction
    paths = 0
    print("Called")
    if newscreen.get_at((currentX, currentY - blockSize)) == white:
        paths = paths + 1
        print("returnUp")
    if newscreen.get_at((currentX - blockSize, currentY)) == white:
        paths = paths + 1
        print("returnLeft")
    if newscreen.get_at((currentX + blockSize, currentY)) == white:
        paths = paths + 1
        print("returnRight")
    if  newscreen.get_at((currentX, currentY + blockSize)) == white:
        paths = paths + 1
        print("returnDown")
    if direction == 1 and newscreen.get_at((currentX, currentY - blockSize)) == blue:
        moveUp(currentX, currentY, blockSize, white)
        print ("up")
    if direction == 3 and newscreen.get_at((currentX - blockSize, currentY)) == blue:
        moveLeft(currentX, currentY, blockSize, white)
        print ("left")
    if direction == 2 and newscreen.get_at((currentX + blockSize, currentY)) == blue:
        moveRight(currentX, currentY, blockSize, white)
        print ("right")
    if direction == 4 and newscreen.get_at((currentX, currentY + blockSize)) == blue:
        moveDown(currentX, currentY, blockSize, white)
        print ("down")
    if paths > 2:
        print(paths)
        return True
    else:
        print(paths)
        if direction == 1
            moveUp(currentX, currentY, blockSize, white)
        if direction == 3
            moveLeft(currentX, currentY, blockSize, white)
        if direction == 2
            moveRight(currentX, currentY, blockSize, white)
        if direction == 4
            moveDown(currentX, currentY, blockSize, white)
        return False

varsInit(xvalueOfStart, yvalueOfStart)

moveUp(currentX, currentY, blockSize, white)

#time.sleep(0.1)

#moveLeft(currentX, currentY, blockSize)
#time.sleep(1)

#moveDown(currentX, currentY, blockSize)
#time.sleep(1)

#moveRight(currentX, currentY, blockSize)
#time.sleep(1)

'''
1 is up
2 is right
3 is left
4 is down
'''

direction = 1

def checkRed():
    global direction
    if newscreen.get_at((currentX, currentY - blockSize)) == red:
        direction = 1
        moveUp(currentX, currentY, blockSize, blue)
    elif newscreen.get_at((currentX + blockSize, currentY)) == red:
        direction = 2
        moveRight(currentX, currentY, blockSize, blue)
    elif newscreen.get_at((currentX - blockSize, currentY)) == red:
        direction = 3
        moveLeft(currentX, currentY, blockSize, blue)
    else:
        direction = 4
        moveDown(currentX, currentY, blockSize, blue)

# Check if all paths of an intersection have been travelled. If so, go back on red
def intersection():
    if newscreen.get_at((currentX, currentY + blockSize)) != white and newscreen.get_at((currentX, currentY - blockSize)) != white and newscreen.get_at((currentX - blockSize, currentY)) != white and newscreen.get_at((currentX + blockSize, currentY)) != white:
        checkRed()
            
          

# ------------- OUR ALGORITHM -------------

while 0 != currentY:
    getCur = newscreen.get_at((currentX, currentY))
    if direction == 1:#up
        if isIntersection():
            if getCur == blue:#blue=intersection tile
                moveDown(currentX, currentY, blockSize, white)
                moveUp(currentX, currentY, blockSize, red)#red=path into intersection
                intersection()
            else:
                up(blue)
        else:
            up(white)
    elif direction == 2:#right
        if isIntersection():
            if getCur == blue:#blue=intersection tile
                moveLeft(currentX, currentY, blockSize, white)
                moveRight(currentX, currentY, blockSize, red)#red=path into intersection
                intersection()
            else:
                right(blue)
        else:
            right(white)
    elif direction == 3:#left
        if isIntersection():
            if getCur == blue:#blue=intersection tile
                moveRight(currentX, currentY, blockSize, white)
                moveLeft(currentX, currentY, blockSize, red)#red=path into intersection                
                intersection()                    
            else:
                left(blue)
        else:
            left(white)
    elif direction == 4:#down
        if isIntersection():
            if getCur == blue:#blue=intersection tile
                moveUp(currentX, currentY, blockSize, white)
                moveDown(currentX, currentY, blockSize, red)#red=path into intersection                
                intersection()                   
            else:
                down(blue)
        else:
            down(white)
            

time.sleep(5)










'''
#original
while 0 != currentY:
    if direction == 1:#up
        up()
    elif direction == 2:
        right()
    elif direction == 3:
        left()
    elif direction == 4:
        down()

time.sleep(5)
'''