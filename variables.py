import pygame as p
import random

p.mixer.init()

SCREEN_WIDTH = 768
SCREEN_HEIGHT = 768
FPS = 60 # gonna use it as the game speed until i figure out deltatime (nvm frame counter exists)
frame_counter = 0
food_counter = 0 # counts the frames between foods
GAME_SPEED = 12 # when frame counter resets
points = 0
animState = 0
arrowPos11 = (475,410) # not eleven, 1-1
arrowPos12 = (480,410)
arrowPos21 = (475,480)
arrowPos22 = (480,480)
arrowPos = [arrowPos11,arrowPos12,arrowPos21,arrowPos22]
menuPos = "play"
appleEaten = True
currentLvl = 1
winScreen = False

screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), p.SCALED | p.FULLSCREEN)
clock = p.time.Clock()
gridXdef = [64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384,
 416, 448, 480, 512, 544, 576, 608, 640, 672] # possible apple positions
gridYdef = [64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384,
 416, 448, 480, 512, 544, 576, 608, 640, 672]
applePos = (-50, -50) # out of bounds till needed

darkerBlue = (13,15,36)
green = (37,111,100)
purple = (112,30,127)
red = (140,5,5)

playerSprite = p.image.load("assets\HeadBlue.png")
segment1Sprite = p.image.load("assets\segmentBlue.png")
tail1Sprite = p.image.load("assets\TailBlue.png")
apple1Sprite = p.image.load("assets\AppleLeft.png")
apple2Sprite = p.image.load("assets\AppleRight.png")
playSprite = p.image.load("assets\PlayBlue.png") # 50x16
quitSprite = p.image.load("assets\QuitBlue.png")
wonSprite = p.image.load("assets\YouWon.png")
wonSprite = p.transform.scale(wonSprite, (500,250))

oneSprite = p.image.load("assets\Say1.png") # Num doesn't work so we go turkish (Number = Sayı)
twoSprite = p.image.load("assets\Say2.png")
threeSprite = p.image.load("assets\Say3.png")
fourSprite = p.image.load("assets\Say4.png")
fiveSprite = p.image.load("assets\Say5.png")
sixSprite = p.image.load("assets\Say6.png")
sevenSprite = p.image.load("assets\Say7.png")
eightSprite = p.image.load("assets\Say8.png")
nineSprite = p.image.load("assets\Say9.png")
zeroSprite = p.image.load("assets\Say0.png")

arrowPointer = p.image.load("assets\Arrow.png")
arrowPointer = p.transform.scale(arrowPointer, (21,21))

numList0 = [zeroSprite,oneSprite,twoSprite,threeSprite,fourSprite,fiveSprite,sixSprite,sevenSprite,eightSprite,
nineSprite]
numList = []
for n in numList0:
    newSp = p.transform.scale(n, (35,35))
    numList.append(newSp)

running = True
playing = False
lvlChange = False

playerHitbox = p.Rect(400, 400, 32, 32)

tailHitbox0 = p.Rect(-150, -150, 32, 32) # hell
tailHitbox1 = p.Rect(-150, -150, 32, 32)
tailHitbox2 = p.Rect(-150, -150, 32, 32)
tailHitbox3 = p.Rect(-150, -150, 32, 32)
tailHitbox4 = p.Rect(-150, -150, 32, 32)
tailHitbox5 = p.Rect(-150, -150, 32, 32)
tailHitbox6 = p.Rect(-150, -150, 32, 32)
tailHitbox7 = p.Rect(-150, -150, 32, 32)
tailHitbox8 = p.Rect(-150, -150, 32, 32)
tailHitbox9 = p.Rect(-150, -150, 32, 32)
tailHitbox10 = p.Rect(-150, -150, 32, 32)
tailHitbox11 = p.Rect(-150, -150, 32, 32)
tailHitbox12 = p.Rect(-150, -150, 32, 32)
tailHitbox13 = p.Rect(-150, -150, 32, 32)
tailHitbox14 = p.Rect(-150, -150, 32, 32)
tailHitbox15 = p.Rect(-150, -150, 32, 32)
tailHitbox16 = p.Rect(-150, -150, 32, 32)
tailHitbox17 = p.Rect(-150, -150, 32, 32)
tailHitbox18 = p.Rect(-150, -150, 32, 32)
tailHitbox19 = p.Rect(-150, -150, 32, 32)
tailHitbox20 = p.Rect(-150, -150, 32, 32)

wallHitbox1 = p.Rect(0, 0, 768, 64) # this creates a cage for the snake (python)
wallHitbox2 = p.Rect(0, 0, 64, 768)
wallHitbox3 = p.Rect(0, 704, 768, 64)
wallHitbox4 = p.Rect(704, 0, 64, 768)

appleHitbox = p.Rect(-50, -50, 32, 32)
bananaHitbox = p.Rect(-50, -50, 32, 32)

playBHitbox = p.Rect(255, 384, 250, 70)
quitBHitbox = p.Rect(255, 465, 250, 65)

walls = [wallHitbox1, wallHitbox2, wallHitbox3, wallHitbox4]
tails = [tailHitbox0,tailHitbox1,tailHitbox2,tailHitbox3,tailHitbox4,tailHitbox5,tailHitbox6,tailHitbox7,
tailHitbox8,tailHitbox9,tailHitbox10,tailHitbox11,tailHitbox12,tailHitbox13,tailHitbox14,tailHitbox15,
tailHitbox16,tailHitbox17,tailHitbox18,tailHitbox19,tailHitbox20]

powerUp = p.mixer.Sound("assets\PowerUp.mp3")
powerUp.set_volume(0.1)
hitSomething = p.mixer.Sound("assets\ExplosionBy u_b32baquv5u.mp3")
hitSomething.set_volume(0.1)
mainTheme = p.mixer.music.load("assets\Insert Coin(loop ver).wav") #By KYTstudio
p.mixer.music.set_volume(0.1)

lvl2Walls = []
for i in range(30):
    lvl2Walls.append(p.Rect(1000,1000,32,32)) #This is much easier i wish i did it before

for i in lvl2Walls:
    walls.append(i)

lvl3Walls = []
for i in range(46):
    lvl3Walls.append(p.Rect(1000,1000,32,32))

for i in lvl3Walls:
    walls.append(i)

#levels are made out of a lot of rects, i am gonna specify their coordinates here.
#wish me luck

def lvl1():
    for i in lvl2Walls:
        i.topleft = (1000,1000)
    for i in lvl3Walls:
        i.topleft = (1000,1000)

def lvl2():
    lvl2Walls[0].topleft = (128,128)
    lvl2Walls[1].topleft = (160,128)
    lvl2Walls[2].topleft = (192,128)
    lvl2Walls[3].topleft = (224,128)
    lvl2Walls[4].topleft = (128,160)
    lvl2Walls[5].topleft = (128,192)
    lvl2Walls[6].topleft = (128,224)
    lvl2Walls[7].topleft = (480,64)
    lvl2Walls[8].topleft = (480,96)
    lvl2Walls[9].topleft = (480,128)
    lvl2Walls[10].topleft = (480,160)
    lvl2Walls[11].topleft = (480,192)
    lvl2Walls[12].topleft = (480,224)
    lvl2Walls[13].topleft = (480,256)
    lvl2Walls[14].topleft = (480,288)
    lvl2Walls[15].topleft = (256,448)
    lvl2Walls[16].topleft = (256,480)
    lvl2Walls[17].topleft = (256,512)
    lvl2Walls[18].topleft = (256,544)
    lvl2Walls[19].topleft = (256,576)
    lvl2Walls[20].topleft = (256,608)
    lvl2Walls[21].topleft = (256,640)
    lvl2Walls[22].topleft = (256,672)
    lvl2Walls[23].topleft = (608,512)#a
    lvl2Walls[24].topleft = (608,544)
    lvl2Walls[25].topleft = (608,576)
    lvl2Walls[26].topleft = (608,608)
    lvl2Walls[27].topleft = (576,608)
    lvl2Walls[28].topleft = (544,608)
    lvl2Walls[29].topleft = (512,608)

def lvl3():
    lvl3Walls[0].topleft = (64,224)
    lvl3Walls[1].topleft = (96,224)
    lvl3Walls[2].topleft = (128,224)
    lvl3Walls[3].topleft = (160,224)
    lvl3Walls[4].topleft = (192,224)
    lvl3Walls[5].topleft = (224,224)
    lvl3Walls[6].topleft = (256,224) #
    lvl3Walls[7].topleft = (480,224)
    lvl3Walls[8].topleft = (512,224)
    lvl3Walls[9].topleft = (544,224)
    lvl3Walls[10].topleft = (576,224)
    lvl3Walls[11].topleft = (608,224)
    lvl3Walls[12].topleft = (640,224)
    lvl3Walls[13].topleft = (672,224) #
    lvl3Walls[14].topleft = (288,96)
    lvl3Walls[15].topleft = (288,128)
    lvl3Walls[16].topleft = (320,128)
    lvl3Walls[17].topleft = (320,96) #
    lvl3Walls[18].topleft = (416,96)
    lvl3Walls[19].topleft = (416,128)
    lvl3Walls[20].topleft = (448,128)
    lvl3Walls[21].topleft = (448,96) #
    lvl3Walls[22].topleft = (160,352)
    lvl3Walls[23].topleft = (160,384) #
    lvl3Walls[24].topleft = (512,352)
    lvl3Walls[25].topleft = (512,384) #
    lvl3Walls[26].topleft = (192,512)
    lvl3Walls[27].topleft = (224,512)
    lvl3Walls[28].topleft = (256,512)
    lvl3Walls[29].topleft = (288,512)
    lvl3Walls[30].topleft = (320,512)
    lvl3Walls[31].topleft = (352,512)
    lvl3Walls[32].topleft = (384,512)
    lvl3Walls[33].topleft = (416,512)
    lvl3Walls[34].topleft = (448,512)
    lvl3Walls[35].topleft = (480,512)
    lvl3Walls[36].topleft = (512,512)
    lvl3Walls[37].topleft = (544,512) #
    lvl3Walls[38].topleft = (96,608)
    lvl3Walls[39].topleft = (96,640)
    lvl3Walls[40].topleft = (128,608)
    lvl3Walls[41].topleft = (128,640) #
    lvl3Walls[42].topleft = (608,608)
    lvl3Walls[43].topleft = (640,608)
    lvl3Walls[44].topleft = (608,640)
    lvl3Walls[45].topleft = (640,640)
    for i in lvl2Walls:
        i.topleft = (1000,1000)