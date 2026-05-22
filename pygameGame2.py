import pygame as p
import random
from variables import *
import itertools
import time

p.init()
p.mixer.init()

#--------classes------------------------------------------------------------
class Head(): # code for the head of the snake (actual player)
    forbiddenPath = 2
    def __init__(self, sprite, positionX, positionY, rotation, hitbox):
        self.sprite = sprite
        self.positionX = positionX
        self.positionY = positionY
        self.rotation = rotation
        self.position = (positionX, positionY)
        self.hitbox = hitbox

    def Move(self, frame_counter):

        if key[p.K_w] and self.forbiddenPath != 0: #problematic shit
            self.rotation = 0
            self.sprite = playerSprite
        elif key[p.K_s] and self.forbiddenPath != 2:
            self.rotation = 180
            self.sprite = p.transform.rotate(playerSprite, 180)
        elif key[p.K_a] and self.forbiddenPath != 1:
            self.rotation = 90
            self.sprite = p.transform.rotate(playerSprite, 90)
        elif key[p.K_d] and self.forbiddenPath != 3:
            self.rotation = -90
            self.sprite = p.transform.rotate(playerSprite, -90)
        
        if frame_counter == GAME_SPEED:
            if self.rotation == 0:
                self.positionY = self.positionY - 32
                self.forbiddenPath = 2
            elif self.rotation == 180:
                self.positionY = self.positionY + 32
                self.forbiddenPath = 0
            elif self.rotation == 90:
                self.positionX = self.positionX - 32
                self.forbiddenPath = 3
            elif self.rotation == -90:
                self.positionX = self.positionX + 32
                self.forbiddenPath = 1

        self.position = (self.positionX, self.positionY)
        self.hitbox.topleft = self.position


class Segment(): # code for segments to follow eachother and stuff

    def __init__(self, sprite, position, rotation, hitbox):
        self.sprite = sprite
        self.position = position
        self.rotation = rotation
        self.tempPos = self.position
        self.tempRot = self.rotation
        self.tempSprite = self.sprite
        self.hitbox = hitbox

    def Follow(self, former, frame_counter):
        
        if frame_counter == GAME_SPEED:
            self.position = self.tempPos
            self.tempPos = former.position

            self.rotation = self.tempRot
            self.tempRot = former.rotation

            if self.tempRot == 0:
                self.sprite = self.tempSprite
            elif self.tempRot == 90:
                self.sprite = p.transform.rotate(self.tempSprite, 90)
            elif self.tempRot == 180:
                self.sprite = p.transform.rotate(self.tempSprite, 180)
            elif self.tempRot == -90:
                self.sprite = p.transform.rotate(self.tempSprite, -90)
        
        self.hitbox.topleft = self.position


class Apple(): #food. for score. to grow.

    def __init__(self, sprite1, sprite2, position, value, hitbox):
        self.sprite1 = sprite1
        self.sprite2 = sprite2
        self.position = position
        self.value = value
        self.hitbox = hitbox


class Button():

    def __init__(self, sprite, hitbox):
        self.sprite = p.transform.scale(sprite, (250, 80))
        self.hitbox = hitbox
        

class Number():
    i = 0
    def __init__(self,numbers,active):
        self.numbers = numbers
        self.active = active

    def GoUp(self, points):
        if self.i < 9:
            self.i += 1
            self.active = self.numbers[self.i]
        else:
            self.i = 0
            self.active = self.numbers[self.i]
        return self.i
#--------classes------------------------------------------------------------

# I can't put them in a different file help
player = Head(playerSprite, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, playerHitbox)
segment1 = Segment(segment1Sprite, (800,800), 0, tailHitbox1)
segment2 = Segment(segment1Sprite, (800,800), 0, tailHitbox2)
segment3 = Segment(segment1Sprite, (800,800), 0, tailHitbox3)
segment4 = Segment(segment1Sprite, (800,800), 0, tailHitbox4)
segment5 = Segment(segment1Sprite, (800,800), 0, tailHitbox5)
segment6 = Segment(segment1Sprite, (800,800), 0, tailHitbox6)
segment7 = Segment(segment1Sprite, (800,800), 0, tailHitbox7)
segment8 = Segment(segment1Sprite, (800,800), 0, tailHitbox8)
segment9 = Segment(segment1Sprite, (800,800), 0, tailHitbox9)
segment10 = Segment(segment1Sprite, (800,800), 0, tailHitbox10)
segment11 = Segment(segment1Sprite, (800,800), 0, tailHitbox11)
segment12 = Segment(segment1Sprite, (800,800), 0, tailHitbox12)
segment13 = Segment(segment1Sprite, (800,800), 0, tailHitbox13)
segment14 = Segment(segment1Sprite, (800,800), 0, tailHitbox14)
segment15 = Segment(segment1Sprite, (800,800), 0, tailHitbox15)
segment16 = Segment(segment1Sprite, (800,800), 0, tailHitbox16)
segment17 = Segment(segment1Sprite, (800,800), 0, tailHitbox17)
segment18 = Segment(segment1Sprite, (800,800), 0, tailHitbox18)
segment19 = Segment(segment1Sprite, (800,800), 0, tailHitbox19)
segment20 = Segment(segment1Sprite, (800,800), 0, tailHitbox20)
tail1 = Segment(tail1Sprite, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 32), 0, tailHitbox0)

apple = Apple(apple1Sprite, apple2Sprite, applePos, 10, appleHitbox)

playButton = Button(playSprite, playBHitbox)
quitButton = Button(quitSprite, quitBHitbox)

score1 = Number(numList,numList[0])
score2 = Number(numList,numList[0])

foods = [apple]
snake = [tail1]
segments = [segment1, segment2, segment3, segment4, segment5, segment6, segment7, segment8, segment9,
segment10, segment11, segment12, segment13, segment14, segment15, segment16, segment17, segment18,
segment19, segment20]

#----------gameplay-------------------------------------------------------------
p.mixer.music.play(-1)
while running:

    key = p.key.get_pressed()

    clock.tick(FPS)
    screen.fill(darkerBlue) 

    if points == 50: # snake gets faster when it gets FAT
        GAME_SPEED = 10
    elif points == 100:
        GAME_SPEED = 8
    elif points == 150:
        GAME_SPEED = 6

    if frame_counter > GAME_SPEED: # The GOAT
            frame_counter = 0
            animState += 1
    frame_counter += 1

    if playing == False and winScreen == False:
        screen.blit(playButton.sprite, (240,384))
        screen.blit(quitButton.sprite, (240,454))

        if menuPos == "play":
            if animState <= 2:
                screen.blit(arrowPointer, arrowPos[0])
            elif animState < 5:
                screen.blit(arrowPointer, arrowPos[1])
            elif animState >= 5:
                screen.blit(arrowPointer, arrowPos[1])
                animState = 0    
        elif menuPos == "quit":
            if animState <= 2:
                screen.blit(arrowPointer, arrowPos[2])
            elif animState < 5:
                screen.blit(arrowPointer, arrowPos[3])
            elif animState >= 5:
                screen.blit(arrowPointer, arrowPos[3])
                animState = 0

        if menuPos == "play":
            if key[p.K_s]:
                menuPos = "quit"
            if key[p.K_SPACE]:
                playing = True
        elif menuPos == "quit":
            if key[p.K_w]:
                menuPos = "play"
            if key[p.K_SPACE]:
                running = False

        playBHitbox.topleft = (255, 384)
        quitBHitbox.topleft = (255, 465)
    else:
        playBHitbox.topleft = (1000,0)
        quitBHitbox.topleft = (1000,0)

    if winScreen == True:
        screen.blit(wonSprite, (230,350))
        if key[p.K_SPACE]:
            winScreen = False
            time.sleep(1)

    #-------gameplay--------------
    if playing:

        gridX = gridXdef
        gridY = gridYdef
        grid = list(itertools.product(gridX,gridY))

        for i in lvl2Walls:
            if i.topleft in grid:
                grid.remove(i.topleft)
        for i in lvl3Walls:
            if i.topleft in grid:
                grid.remove(i.topleft)

        food_counter += 1
        if food_counter >= 200 and appleEaten == True:
            apple.position = (random.choice(grid))
            food_counter = 0
            appleEaten = False

        if currentLvl == 1:
            p.draw.rect(screen, green, wallHitbox1)
            p.draw.rect(screen, green, wallHitbox3)
            p.draw.rect(screen, green, wallHitbox2)
            p.draw.rect(screen, green, wallHitbox4)
        elif currentLvl == 2:
            p.draw.rect(screen, purple, wallHitbox1)
            p.draw.rect(screen, purple, wallHitbox3)
            p.draw.rect(screen, purple, wallHitbox2)
            p.draw.rect(screen, purple, wallHitbox4)
        elif currentLvl == 3:
            p.draw.rect(screen, red, wallHitbox1)
            p.draw.rect(screen, red, wallHitbox3)
            p.draw.rect(screen, red, wallHitbox2)
            p.draw.rect(screen, red, wallHitbox4)

        for i in lvl2Walls:
            p.draw.rect(screen, purple, i)

        for i in lvl3Walls:
            p.draw.rect(screen, red, i)

        screen.blit(numList[0], (665,20))
        screen.blit(score1.active, (630,20))
        screen.blit(score2.active, (595,20))

        screen.blit(player.sprite, (player.positionX, player.positionY))
        for s in snake:
            screen.blit(s.sprite, s.position)
        screen.blit(tail1.sprite, tail1.position)

        screen.blit(apple1Sprite, apple.position)
        appleHitbox.topleft = apple.position


        player.Move(frame_counter)
        former = player
        for s in snake:
            s.Follow(former, frame_counter)
            former = s

        for food in foods:
            if player.hitbox.colliderect(food.hitbox):
                food.position = (-50, -50)
                appleEaten = True
                points += food.value
                powerUp.play()
                i = score1.GoUp(points)
                if i == 0:
                    score2.GoUp(points)
                snake.insert(0, segments.pop(0))
                print(points)

        if points == 200:
            if currentLvl == 1:
                lvlChange = True
                lvl2()
                animState = 0
                currentLvl = 2
            elif currentLvl == 2:
                lvlChange = True
                lvl3()
                animState = 0
                currentLvl = 3
            elif currentLvl == 3:
                winScreen = True
                playing = False
                lvl1()
                score1.active = numList[0]
                score2.active = numList[0]
                score1.i = 0 
                score2.i = 0
                animState = 0
                currentLvl = 1

        for wall in walls:
            if player.hitbox.colliderect(wall):
                hitSomething.play()
                playing = False
                lvl1()
                score1.active = numList[0]
                score2.active = numList[0]
                score1.i = 0 
                score2.i = 0
                animState = 0
                currentLvl = 1
                print("u ded")

        for seg in snake:
            if player.hitbox.colliderect(seg.hitbox):
                hitSomething.play()
                playing = False
                lvl1()
                score1.active = numList[0]
                score2.active = numList[0]
                score1.i = 0 
                score2.i = 0
                animState = 0
                currentLvl = 1
                print("u bit yourself")    
    #-------gameplay---------------

    #reset the game
    if playing == False or lvlChange == True:
        snake = [tail1]
        segments = [segment1, segment2, segment3, segment4, segment5, segment6, segment7, segment8, segment9,
        segment10, segment11, segment12, segment13, segment14, segment15, segment16, segment17, segment18,
        segment19, segment20]
        player.positionX = SCREEN_WIDTH/2 
        player.positionY = SCREEN_HEIGHT/2
        for s in segments:
            s.position = (800,800)
            s.tempPos = (800,800)
            s.hitbox.topleft = s.position
        tail1.position = (800, 800)
        tail1.tempPos = (800, 800)
        apple.position = (-50,-50)
        player.rotation = 0
        player.sprite = playerSprite
        points = 0
        GAME_SPEED = 12
        lvlChange = False
        appleEaten = True

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        if event.type == p.MOUSEBUTTONDOWN:
            if playButton.hitbox.collidepoint(event.pos):
                playing = True
            elif quitButton.hitbox.collidepoint(event.pos):
                running = False

    if key[p.K_ESCAPE]:
        running = False

    p.display.update()
#----------gameplay-------------------------------------------------------------
p.quit()

print("game ended")