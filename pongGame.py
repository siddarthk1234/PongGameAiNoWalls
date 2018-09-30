import pygame

import random

import sys




count3 = 0
p1Score = 0
AiScore = 0


game_over = True

class Paddle(pygame.sprite.Sprite):

 def __init__(self, image, pongPaddlex,pongPaddley):

  pygame.sprite.Sprite.__init__(self)


  self.rect = image.get_rect()

  self.rect.x =  pongPaddlex
  self.rect.y = pongPaddley










 def is_collided_with(self, sprite):
     return self.rect.colliderect(sprite.rect)


class Ball(pygame.sprite.Sprite):
    def __init__(self,image,ballxPosition1,ballyPosition1):
        pygame.sprite.Sprite.__init__(self)

        self.rect = image.get_rect()

        self.rect.x = ballxPosition1
        self.rect.y = ballyPosition1



















pygame.init()


size = (width,height) = (720,600)
background_color = (255,255,255)
screen = pygame.display.set_mode(size)
screen.fill(background_color)
pygame.display.flip()
dest = (0,300)
hitBottomWall = False
hitTopWall = False
notleftWall = False
hitLeftWall = False
hitRightWall = False
xPositionForPaddle1 = 175
xPositionForPaddle2 = 175
randomNumber13 = 5
ballGoingDiagonallyLeftUp = False
ballGoingDiagonallyLeftDown = False
count7 = 0
gameMode = "None"




RecoverAi1Left = False
RecoverAi1Right = False

RecoverAiUp = False
RecoverAiDown = False




randomNumber = 5

xForTopRightCornerOfRect = 110
yForTopRightCornerOfRect = 360

xForLowRightCornerOfRect = 110
yForLowRightCornerOfRect = 560

xyForTopRightCornerOfRect = (xForTopRightCornerOfRect, yForTopRightCornerOfRect)
xyForLowRightCornerOfRect = (xForLowRightCornerOfRect, yForLowRightCornerOfRect)

keydownHeld = True

yPosition = dest[1]
xyPosition = (60,yPosition)



xPositionForUpperLeftOfAi2Paddle = 545
xPositionForUpperRightOfAi2Paddle = 585
xPositionForLowerRightOfAi2Paddle = 585
xPositionForLowerLeftOfAi2Paddle = 545


xyPositionForUpperLeftOfAi2Paddle = (xPositionForUpperLeftOfAi2Paddle, 560)
xyPositionForUpperRightOfAi2Paddle = (xPositionForUpperRightOfAi2Paddle, 560)
xyPositionForLowerRightOfAi2Paddle = (xPositionForLowerRightOfAi2Paddle, 590)
xyPositionForLowerLeftOfAi2Paddle = (xPositionForLowerLeftOfAi2Paddle,590)


paddles = pygame.sprite.Group()


yPositionForUpperLeftCornerOfAiPaddle = 300
yPositionForUpperRightCornerOfAiPaddle = 300
yPositionForLowerLeftCornerOfAiPaddle = 350
yPositionForLowerRightCornerOfAiPaddle = 350
xyPositionForUpperLeftCornerOfAiPaddle = (700,yPositionForUpperLeftCornerOfAiPaddle)
xyPositionForUpperRightCornerOfAiPaddle = (720,yPositionForUpperRightCornerOfAiPaddle)
xyPositionForLowerLeftCornerOfAiPaddle = (700,yPositionForLowerLeftCornerOfAiPaddle)
xyPositionForLowerRightCornerOfAiPaddle = (720,yPositionForLowerRightCornerOfAiPaddle)











movingUp = False

hitBall = False




net = pygame.image.load("images/net.gif")
net = pygame.transform.scale(net,(60,600))
pongPaddle = pygame.image.load("images/download.png")
AiPongPaddle = pygame.image.load("images/download.png")
pongPaddle1 = pygame.image.load("images/pongPaddle.png")

pongPaddle2 = pygame.image.load("images/pongPaddle.png")

AiPongPaddle1 = pygame.image.load("images/pongPaddle.png")
AiPongPaddle2 = pygame.image.load("images/pongPaddle.png")





paddles.add_internal(pongPaddle)
paddles.add_internal(pongPaddle1)
paddles.add_internal(pongPaddle2)

xPositionForAiPongPaddle1 = 540
xPositionForAIPongPaddle2 = 540


pongPaddle1 = pygame.transform.scale(pongPaddle1 , (50,60))
pongPaddle2 = pygame.transform.scale(pongPaddle2, (50, 60)).convert()

AiPongPaddle = pygame.transform.scale(AiPongPaddle,(20,50))

ball = pygame.image.load("images/ball.png")


pongPaddle = pygame.transform.scale(pongPaddle, (20,50))
ball = pygame.transform.scale(ball,(50,50))



yForAiPongPaddleLocation = 300

AiPongPaddleLocation = (700,300)



AiPongPaddle1 = pygame.transform.scale(AiPongPaddle1,(50,60))
AiPongPaddle2 = pygame.transform.scale(AiPongPaddle2,(50,60))
screen.blit(AiPongPaddle1,(xPositionForAiPongPaddle1, -15))
screen.blit(AiPongPaddle2,(xPositionForAIPongPaddle2, 550))
screen.blit(pongPaddle1,(175,-15))
screen.blit(pongPaddle2, (175,550))
screen.blit(net,(350,0))

screen.blit(AiPongPaddle,AiPongPaddleLocation)
screen.blit(pongPaddle,dest)
screen.blit(ball,(360, 300))
count1 = 0
count2 = 0
count4 = 0
count5 = 0
randomNumber2 = 5
randomNumbe3 = 5
count6 = 0
randomNumber4 = 5
randomNumber5 = 5


count3 = 0
ballxPosition = 360
ballyPosition = 300
randomNumber1 = 5
leftPaddle = False
leftPaddle1 = False
AiXPaddleLocation = 660
AiYPaddleLocation = 360

reachedTop = False
yPositionForAiDot1 = 360
yPositionForAiDot2 = 560
yPositionForAiDot3 = 400
yPositionForAiDot4 = 500
xyForAiDot1 = (670,360)
xyForAiDot2 = (670,560)
xyForAiDot3 = (670,400)
xyForAiDot4 = (670,500)
hitTopRegionOfAiPaddle = False
hitMiddleREgionOfAiPaddle = False
hitBottomRegionOfAiPaddle = False
bouncedOffTopDiagonallyP1 = False
bouncedOffBottomDiagonallyP1 = False
bouncedOffTopDiagonallyAI = False
bouncedOffBottomDiagonallyAI = False
bouncedDirectlyTowardsLeftWallDiagonallyDown = False
bouncedDirectlyTowardsLeftWAllDiagonallyUp = False
xCoordinateForLeftBoundaryOfPaddle1 = 175
xCoordinateForRightBoundaryOfPAddle1 = 222
xyForLeftBoundaryPongPaddle1 = (xCoordinateForLeftBoundaryOfPaddle1,30)
xyForRightBoundaryPongPaddle1 = (xCoordinateForRightBoundaryOfPAddle1, 30)

yCoordinateForTopBoundaryOfPaddle = 300
yCoordinateForBottomBoundaryOfPaddle = 350
xyForTopBoundaryOfPaddle = (20,yCoordinateForTopBoundaryOfPaddle)
xyForBottomBoundaryOfPaddle = (20,yCoordinateForBottomBoundaryOfPaddle)
xPositionForBottomLeftBoundaryOfPaddle1 = 175
xPositionForBottomRightBoundaryOfPaddle1 = 225
xyPositionForBottomRightBoundaryOfPaddle1 = (xPositionForBottomRightBoundaryOfPaddle1,5)
xyPositionForBottomLeftBoundaryOfPaddle1 = (xPositionForBottomLeftBoundaryOfPaddle1,5)
yPositionForBottomTopOfPaddle = 300
yPositionForBottomBottomOfPaddle = 350
xyPositionForBottomTopOfPaddle = (0,yPositionForBottomTopOfPaddle)
xyPositionForBottomBottomOfPaddle = (0,yPositionForBottomBottomOfPaddle)

xPositionForTopLeftOfPaddle2 = 175
xPositionForBottomLeftOfPaddle2 = 175
xPositionForTopRightOfPaddle2 = 225
xPositionForBottomRightOfPaddle2 = 225
xyTopLeftBoundaryForPaddle2 = (xPositionForTopLeftOfPaddle2, 570)
xyBottomLeftBoundaryForPaddle2 = (xPositionForBottomLeftOfPaddle2, 595)
xyTopRightBoundaryForPaddle2 = (xPositionForTopRightOfPaddle2, 570)
xyBottomRightBoundaryForPaddle2 = (xPositionForBottomRightOfPaddle2,595)

pongPaddle1Rect = pongPaddle1.get_rect()
ballRect = ball.get_rect()
collided = pongPaddle1Rect.colliderect(ballRect)
PongPaddleRect = pongPaddle.get_rect()
count1 = 0


















count = 0
randomNumber12 = 5
ballGoingDiagonallyUp = False
ballGoingDiagonallyDown = False
DeflectBallLeftDiagonallyDown = False
DeflectBallLeftDiagonallyUp = False
DeflectBallRightDiagonallyUp = False
DeflectBallRightDiagonallyDown = False
PongPaddleHitBall = False
AiPaddle2HitBall = False
startRecoveryToMiddle = False
AiPaddleHitBall = False
ballGoingDiagonallyRightDown = False
ballGoingDiagonallyRightUp = False
collidedWithPaddle = False
collidedWithPaddle1 = False
collidedWithPaddle2 = False
collideWithAiPaddle = False
collideWithAiPaddle1 = False
collideWithAiPaddle2 = False
playingUpTo = 0




def GameOver():
  global playingUpTo
  global count1
  global game_over
  global gameMode
  while game_over:



    print("In here of game over")

    if(count1 == 0):

       screen.fill((255,255,255))
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface = myfont.render('Pong-game AI no walls', False, (0,0,0))


    textsurface1 = myfont.render('Level:', False, (0,0,0))

    textsurface2 = myfont.render('Easy', False, (0, 0, 0))

    textsurface3 = myfont.render('Medium', False, (0, 0, 0))

    textsurface4 = myfont.render('Hard', False, (0, 0, 0))
    textsurface5 = myfont.render('Play Up to:', False, (0, 0, 0))
    textsurface6 = myfont.render('10', False, (0, 0, 0))
    textsurface7 = myfont.render('15', False, (0,0,0))
    textsurface8 = myfont.render('20', False, (0, 0, 0))
    textsurface9 = myfont.render("Play Now!", False, (0,0,0))
    spRect9 = textsurface9.get_rect()
    spRect2 = textsurface2.get_rect()
    spRect2.centerx = 150
    spRect2.centery = 50
    spRect3 = textsurface3.get_rect()
    spRect3.centerx = 300
    spRect3.centery = 50
    spRect4 = textsurface4.get_rect()
    spRect4.centerx = 450
    spRect4.centery = 50
    spRect6 = textsurface6.get_rect()
    spRect6.centerx = 200
    spRect6.centery = 80
    spRect7 = textsurface7.get_rect()
    spRect7.centerx = 300
    spRect7.centery = 80
    spRect8 = textsurface8.get_rect()
    spRect8.centerx = 400
    spRect8.centery = 80
    spRect9.centerx = 400
    spRect9.centery = 200






    if(count1 == 0):






     
     screen.blit(textsurface9,spRect9)

     screen.blit(textsurface5, (0, 60))
     screen.blit(textsurface6,spRect6)
     screen.blit(textsurface7,(spRect7))
     screen.blit(textsurface8,spRect8)
     screen.blit(textsurface, (0, 0))


    mousPos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if spRect9.collidepoint(mousPos):
                    if playingUpTo != 0:
                        screen.fill((255,255,255))
                        game_over = False



                if spRect6.collidepoint(mousPos):
                    print("In here")

                    playingUpTo = 10


                    textsurface6 = myfont.render('10', False, (0, 0, 255))
                    textsurface7 = myfont.render('15', False, (0, 0, 0))
                    textsurface8 = myfont.render('20', False, (0, 0, 0))


                    screen.blit(textsurface5, (0, 60))
                    screen.blit(textsurface6, spRect6)
                    screen.blit(textsurface7, spRect7)
                    screen.blit(textsurface8, spRect8)
                    screen.blit(textsurface, (0, 0))

                    screen.blit(textsurface9, spRect9)
                    pygame.display.update()

                if spRect7.collidepoint(mousPos):
                    print("In here")

                    playingUpTo = 15





                    textsurface6 = myfont.render('10', False, (0, 0, 0))
                    textsurface7 = myfont.render('15', False, (0, 0, 255))
                    textsurface8 = myfont.render('20', False, (0, 0, 0))

                    screen.blit(textsurface5, (0, 60))
                    screen.blit(textsurface6, spRect6)
                    screen.blit(textsurface7, spRect7)
                    screen.blit(textsurface8, spRect8)
                    screen.blit(textsurface, (0, 0))

                    screen.blit(textsurface9, spRect9)
                    pygame.display.update()

                if spRect8.collidepoint(mousPos):


                    playingUpTo = 20






                    textsurface6 = myfont.render('10', False, (0, 0, 0))
                    textsurface7 = myfont.render('15', False, (0, 0, 0))
                    textsurface8 = myfont.render('20', False, (0, 0, 255))


                    screen.blit(textsurface5, (0, 60))
                    screen.blit(textsurface6, spRect6)
                    screen.blit(textsurface7, spRect7)
                    screen.blit(textsurface8, spRect8)
                    screen.blit(textsurface9, spRect9)
                    screen.blit(textsurface, (0, 0))

                    pygame.display.update()

    if count1 == 0 :
     pygame.display.update()
     pygame.display.flip()


    count1 = count1 + 1



GameOver()





while True:








 while game_over != True:
    pygame.font.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound("Sounds/hitPongBall.wav")




    myfont = pygame.font.SysFont('Comic Sans MS', 50)
    textsurface19 = myfont.render(str(p1Score), False, (0, 0, 0))
    textsurface20 = myfont.render(str(AiScore), False, (0,0,0))
    tpRect19 = textsurface19.get_rect()
    tpRect20 = textsurface20.get_rect()




    tpRect19.centerx = 30
    tpRect19.centery = 540


    tpRect20.centerx = 540
    tpRect20.centery = 540


    screen.blit(textsurface19,tpRect19)
    screen.blit(textsurface20,tpRect20)



    pygame.display.update()








    print("xPsotiionForTopLEftOfPaddle2")
    print(xPositionForTopLeftOfPaddle2)
    print("xPositionForTopRightOfPaddle2")
    print(xPositionForTopRightOfPaddle2)
    print("xcoordfortpbndryofPaddle")
    print(yCoordinateForTopBoundaryOfPaddle)
    print("yCoordforbtmboundaryofPaddle")
    print(yCoordinateForBottomBoundaryOfPaddle)

    print("ballxPosition")
    print(ballxPosition)
    print("xpositionForUpperLEftOfAi2Paddle")
    print(xPositionForUpperLeftOfAi2Paddle)
    print("xPositionForUpperRightOfAi2Paddle")
    print(xPositionForUpperRightOfAi2Paddle)
    print("ballyPosition")
    print(ballyPosition)


    print("yPostiion for lowerr left corner of ai paddle")
    print(yPositionForLowerLeftCornerOfAiPaddle)
    print("YPosition for upper left corner of ai paddle")
    print(yPositionForUpperLeftCornerOfAiPaddle)

    paddle12 = Paddle(pongPaddle, 0, yPosition)
    paddle13 = Paddle(pongPaddle1, xPositionForPaddle1,-15)
    paddle14 = Paddle(pongPaddle2,xPositionForPaddle2,550)
    AiPaddle = Paddle(AiPongPaddle,700,yForAiPongPaddleLocation)
    AiPaddle1 = Paddle(AiPongPaddle1,xPositionForAiPongPaddle1,-15)
    AiPaddle2= Paddle(AiPongPaddle2,xPositionForAIPongPaddle2,550)


    ball12 = Ball(ball, ballxPosition, ballyPosition)


    if paddle13.is_collided_with(ball12) and ballGoingDiagonallyLeftUp:
        ballGoingDiagonallyLeftDown = True
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = False
        ballGoingDiagonallyRightUp = False
        collidedWithPaddle = False
        collidedWithPaddle1 = True
        collidedWithPaddle2 = False
        collideWithAiPaddle = False;
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()

    if paddle13.is_collided_with(ball12) and ballGoingDiagonallyRightUp:
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = True
        ballGoingDiagonallyRightUp = False
        collidedWithPaddle = False
        collidedWithPaddle1 = True
        collidedWithPaddle2 = False
        collideWithAiPaddle = False;
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()

    print("paddle13 collided with ball 12")
    print(paddle14.is_collided_with(ball12))


    if paddle14.is_collided_with(ball12) and  ballGoingDiagonallyRightDown:
        ballGoingDiagonallyRightUp = True
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = False
        collidedWithPaddle = False
        collidedWithPaddle1 = False
        collidedWithPaddle2 = True
        collideWithAiPaddle = False;
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()

    if paddle14.is_collided_with(ball12) and ballGoingDiagonallyLeftDown:
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = True
        ballGoingDiagonallyRightDown = False
        collidedWithPaddle = False
        collidedWithPaddle1 = False
        collidedWithPaddle2 = True
        collideWithAiPaddle = False;
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()

    if paddle12.is_collided_with(ball12) and ballGoingDiagonallyLeftUp:
        ballGoingDiagonallyRightUp = True
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = False
        collidedWithPaddle = True
        collidedWithPaddle1 = False
        collidedWithPaddle2 = False
        collideWithAiPaddle = False;
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()

    if paddle12.is_collided_with(ball12) and ballGoingDiagonallyLeftDown:
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = True
        collidedWithPaddle = True
        collidedWithPaddle1 = False
        collidedWithPaddle2 = False
        collideWithAiPaddle = False

        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()



    if AiPaddle.is_collided_with(ball12) and ballGoingDiagonallyRightDown:
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyLeftDown = True
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = False
        collidedWithPaddle = False
        collidedWithPaddle1 = False
        collidedWithPaddle2 = False
        collideWithAiPaddle = True
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        sounda.play()

    if AiPaddle.is_collided_with(ball12) and ballGoingDiagonallyRightUp:
            ballGoingDiagonallyRightUp = False
            ballGoingDiagonallyLeftDown = False
            ballGoingDiagonallyLeftUp = True
            ballGoingDiagonallyRightDown = False
            collidedWithPaddle = False
            collidedWithPaddle1 = False
            collidedWithPaddle2 = False
            collideWithAiPaddle = True
            collideWithAiPaddle1 = False
            collideWithAiPaddle2 = False
            sounda.play()


    if AiPaddle1.is_collided_with(ball12) and ballGoingDiagonallyRightUp:
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = True
        collidedWithPaddle = False
        collidedWithPaddle1 = False
        collidedWithPaddle2 = False
        collideWithAiPaddle = False
        collideWithAiPaddle1 = True
        collideWithAiPaddle2 = False
        sounda.play()









    if AiPaddle1.is_collided_with(ball12) and ballGoingDiagonallyLeftUp:
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyLeftDown = True
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = False
        collidedWithPaddle = False
        collidedWithPaddle1 = False
        collidedWithPaddle2 = False
        collideWithAiPaddle = False
        collideWithAiPaddle1 = True
        collideWithAiPaddle2 = False
        sounda.play()

    if AiPaddle2.is_collided_with(ball12) and ballGoingDiagonallyRightDown:
            ballGoingDiagonallyRightUp = False
            ballGoingDiagonallyLeftDown = False
            ballGoingDiagonallyLeftUp = True
            ballGoingDiagonallyRightDown = False
            collidedWithPaddle = False
            collidedWithPaddle1 = False
            collidedWithPaddle2 = False
            collideWithAiPaddle = False
            collideWithAiPaddle1 = False
            collideWithAiPaddle2 = True
            sounda.play()


    if AiPaddle2.is_collided_with(ball12) and ballGoingDiagonallyLeftDown:
            ballGoingDiagonallyRightUp = True
            ballGoingDiagonallyLeftDown = False
            ballGoingDiagonallyLeftUp = False
            ballGoingDiagonallyRightDown = False
            collidedWithPaddle = False
            collidedWithPaddle1 = False
            collidedWithPaddle2 = False
            collideWithAiPaddle = False
            collideWithAiPaddle1 = False
            collideWithAiPaddle2 = True
            sounda.play()





    if(p1Score == playingUpTo or AiScore == playingUpTo):
        playingUpTo = 0
        gameMode = "None"
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightDown = False
        collidedWithPaddle = False
        collidedWithPaddle1 = False
        collidedWithPaddle2 = False
        collideWithAiPaddle = False
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        screen.fill((255,255,255))
        game_over = True
        count = 0
        count1 = 0
        p1Score = 0
        AiScore = 0
        GameOver()





    print("ballgonigdiagonallyrightdown")
    print(ballGoingDiagonallyRightDown)
    print("ai paddle 1")
    print(collideWithAiPaddle1)



    if(((collidedWithPaddle and ballGoingDiagonallyRightUp) or  (collidedWithPaddle2 and ballGoingDiagonallyRightUp) or (collideWithAiPaddle2 and ballGoingDiagonallyRightUp) or ballGoingDiagonallyRightDown or ballGoingDiagonallyRightUp)and yForAiPongPaddleLocation != ballyPosition):



        if (ballyPosition > yForAiPongPaddleLocation and yForAiPongPaddleLocation !=  540):
            yForAiPongPaddleLocation = yForAiPongPaddleLocation + 1

        if (ballyPosition < yForAiPongPaddleLocation and yForAiPongPaddleLocation != 60):
            yForAiPongPaddleLocation = yForAiPongPaddleLocation - 1





    if((collidedWithPaddle and ballGoingDiagonallyRightDown) or (collidedWithPaddle1 and ballGoingDiagonallyRightDown) or (collideWithAiPaddle1 and ballGoingDiagonallyRightDown)) and yForAiPongPaddleLocation != ballyPosition:
        print("Here i am in the zone")
        if (ballyPosition > yForAiPongPaddleLocation and yForAiPongPaddleLocation != 540):
            yForAiPongPaddleLocation = yForAiPongPaddleLocation + 1

        if (ballyPosition < yForAiPongPaddleLocation and yForAiPongPaddleLocation != 60):
            yForAiPongPaddleLocation = yForAiPongPaddleLocation - 1



    if((collidedWithPaddle and ballGoingDiagonallyRightUp) or (collidedWithPaddle and ballGoingDiagonallyRightDown) or (collidedWithPaddle1 and ballGoingDiagonallyRightDown) or (collidedWithPaddle2 and ballGoingDiagonallyRightUp) or (collideWithAiPaddle and ballGoingDiagonallyLeftUp ) or (collideWithAiPaddle2 and ballGoingDiagonallyRightUp) or (collideWithAiPaddle2 and ballGoingDiagonallyLeftUp)) and ballxPosition != xPositionForAiPongPaddle1:
        print(" In ai paddle 1 movement")

        if ballxPosition > xPositionForAiPongPaddle1 and xPositionForAiPongPaddle1 != 720:
            xPositionForAiPongPaddle1 = xPositionForAiPongPaddle1 + 1;

        if ballxPosition < xPositionForAiPongPaddle1 and xPositionForAiPongPaddle1 != 380:
            xPositionForAiPongPaddle1 = xPositionForAiPongPaddle1 -1;



    if((collidedWithPaddle and ballGoingDiagonallyRightDown) or (collidedWithPaddle1 and ballGoingDiagonallyRightDown) or (collideWithAiPaddle and ballGoingDiagonallyLeftDown) or (collideWithAiPaddle1 and ballGoingDiagonallyLeftDown) or (collideWithAiPaddle1 and ballGoingDiagonallyRightDown) or (collideWithAiPaddle and ballGoingDiagonallyLeftDown) ):

        if ballxPosition > xPositionForAIPongPaddle2 and xPositionForAIPongPaddle2 != 720:
            xPositionForAIPongPaddle2 = xPositionForAIPongPaddle2 + 1

        if ballxPosition < xPositionForAIPongPaddle2 and xPositionForAIPongPaddle2 != 380:
            xPositionForAIPongPaddle2= xPositionForAIPongPaddle2 -1




















    if paddle12.is_collided_with(ball12):
        print("hit the ball")



    if(count7 == 0):
        randomNumber13 = random.randrange(0,4)
        count7 = count7 + 1


        if(randomNumber13 == 0):
          ballGoingDiagonallyLeftUp = True


        if(randomNumber13 == 1):
          ballGoingDiagonallyLeftDown = True

        if(randomNumber13 == 2):
          ballGoingDiagonallyRightUp = True

        if(randomNumber13 == 3):
            ballGoingDiagonallyRightDown = True









    if ballGoingDiagonallyRightDown:
        ballxPosition = ballxPosition +1
        ballxPosition = ballxPosition +1


    if ballGoingDiagonallyLeftUp == True:

        ballxPosition = ballxPosition -1
        ballyPosition = ballyPosition -1


    if ballGoingDiagonallyLeftDown == True:

        ballxPosition = ballxPosition -1
        ballyPosition = ballyPosition + 1


    if ballGoingDiagonallyRightUp == True:
        ballxPosition = ballxPosition +1
        ballyPosition = ballyPosition -1

    if ballGoingDiagonallyRightDown == True:
        ballxPosition = ballxPosition +1
        ballyPosition = ballyPosition + 1




















































    if((collidedWithPaddle2 == False and (ballyPosition == 586 and ballxPosition < 350)) or (collidedWithPaddle1 == False and (ballyPosition ==-35 and ballxPosition < 350 )) or (collidedWithPaddle == False and ballxPosition == -24)  ):
        AiScore = AiScore + 1
        ballxPosition = 360
        ballyPosition = 300
        collideWithAiPaddle = False
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyRightDown = False
        count7 = 0

    if ((collideWithAiPaddle2 == False and (ballxPosition > 350 and ballyPosition == 586)) or (
            collideWithAiPaddle1 == False and (ballyPosition == -35 and ballxPosition > 350)) or (
            collideWithAiPaddle == False and ballxPosition > 720)):
        p1Score = p1Score + 1
        ballxPosition = 360
        ballyPosition = 300
        collideWithAiPaddle = False
        collideWithAiPaddle1 = False
        collideWithAiPaddle2 = False
        ballGoingDiagonallyLeftDown = False
        ballGoingDiagonallyLeftUp = False
        ballGoingDiagonallyRightUp = False
        ballGoingDiagonallyRightDown = False
        count7 = 0









    screen.fill((255, 255, 255))
    screen.blit(pongPaddle1, (xPositionForPaddle1, -15))



    screen.blit(pongPaddle, dest)
    screen.blit(net, (350, 0))
    screen.blit(AiPongPaddle, (700,yForAiPongPaddleLocation))
    screen.blit(ball, (ballxPosition, ballyPosition))
    screen.blit(pongPaddle2, (xPositionForPaddle2, 550))
    screen.blit(AiPongPaddle1, (xPositionForAiPongPaddle1, -15))
    screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))
    keys = pygame.key.get_pressed()


    if keys[pygame.K_q] and xPositionForPaddle1 > 0:
        xPositionForPaddle1 = xPositionForPaddle1 -1
        xCoordinateForRightBoundaryOfPAddle1 = xCoordinateForRightBoundaryOfPAddle1 -1
        xCoordinateForLeftBoundaryOfPaddle1 = xCoordinateForLeftBoundaryOfPaddle1 -1
        xyForLeftBoundaryPongPaddle1 = (xCoordinateForLeftBoundaryOfPaddle1,30)
        xyForRightBoundaryPongPaddle1 = (xCoordinateForRightBoundaryOfPAddle1,30)
        xPositionForBottomLeftBoundaryOfPaddle1 = xPositionForBottomLeftBoundaryOfPaddle1 -1
        xPositionForBottomRightBoundaryOfPaddle1 = xPositionForBottomRightBoundaryOfPaddle1-1
        xyPositionForBottomRightBoundaryOfPaddle1 = (xPositionForBottomRightBoundaryOfPaddle1, 5)
        xyPositionForBottomLeftBoundaryOfPaddle1 = (xPositionForBottomLeftBoundaryOfPaddle1, 5)


        screen.fill((255,255,255))

        screen.blit(pongPaddle1,(xPositionForPaddle1,-15))

        screen.blit(pongPaddle, dest)
        screen.blit(net, (350, 0))
        screen.blit(AiPongPaddle, (700, yForAiPongPaddleLocation))
        screen.blit(ball, (ballxPosition, ballyPosition))
        screen.blit(pongPaddle2,(xPositionForPaddle2,550))
        screen.blit(AiPongPaddle1,(xPositionForAiPongPaddle1,-15))
        screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))



    if keys[pygame.K_w] and xPositionForPaddle1 < 320:
            print("In herez")
            xPositionForPaddle1 = xPositionForPaddle1 + 1
            xCoordinateForLeftBoundaryOfPaddle1 = xCoordinateForLeftBoundaryOfPaddle1 +1
            xCoordinateForRightBoundaryOfPAddle1 = xCoordinateForRightBoundaryOfPAddle1 + 1
            xyForLeftBoundaryPongPaddle1 = (xCoordinateForLeftBoundaryOfPaddle1, 30)
            xyForRightBoundaryPongPaddle1 = (xCoordinateForRightBoundaryOfPAddle1, 30)
            xPositionForBottomLeftBoundaryOfPaddle1 = xPositionForBottomLeftBoundaryOfPaddle1 +1
            xPositionForBottomRightBoundaryOfPaddle1 = xPositionForBottomRightBoundaryOfPaddle1 + 1
            xyPositionForBottomRightBoundaryOfPaddle1 = (xPositionForBottomRightBoundaryOfPaddle1, 5)
            xyPositionForBottomLeftBoundaryOfPaddle1 = (xPositionForBottomLeftBoundaryOfPaddle1, 5)

            screen.fill((255, 255, 255))

            screen.blit(pongPaddle1, (xPositionForPaddle1, -15))

            screen.blit(pongPaddle, dest)
            screen.blit(net, (350, 0))
            screen.blit(AiPongPaddle, (700, yForAiPongPaddleLocation))
            screen.blit(ball, (ballxPosition, ballyPosition))
            screen.blit(AiPongPaddle1, (xPositionForAiPongPaddle1, -15))
            screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))
            screen.blit(pongPaddle2, (xPositionForPaddle2, 550))




    if keys[pygame.K_z] and xPositionForPaddle2 > 0:
            xPositionForPaddle2 = xPositionForPaddle2 - 1
            xPositionForTopRightOfPaddle2 = xPositionForTopRightOfPaddle2 -1
            xPositionForBottomRightOfPaddle2 = xPositionForBottomRightOfPaddle2-1
            xPositionForTopLeftOfPaddle2 = xPositionForTopLeftOfPaddle2 -1
            xPositionForBottomLeftOfPaddle2 = xPositionForBottomLeftOfPaddle2-1


            xyTopLeftBoundaryForPaddle2 = (xPositionForTopLeftOfPaddle2 , 570)
            xyBottomLeftBoundaryForPaddle2 =( xPositionForBottomLeftOfPaddle2, 595)
            xyTopRightBoundaryForPaddle2 = (xPositionForTopRightOfPaddle2, 570)
            xyBottomRightBoundaryForPaddle2 = (xPositionForBottomRightOfPaddle2, 595)


            screen.fill((255, 255, 255))

            screen.blit(pongPaddle2, (xPositionForPaddle2, 550))

            screen.blit(pongPaddle, dest)
            screen.blit(net, (350, 0))
            screen.blit(AiPongPaddle, (700, yForAiPongPaddleLocation))
            screen.blit(AiPongPaddle1, (xPositionForAiPongPaddle1, -15))
            screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))
            screen.blit(ball, (ballxPosition, ballyPosition))
            screen.blit(pongPaddle1, (xPositionForPaddle1, -15))



    if keys[pygame.K_x] and xPositionForPaddle2  < 320:
                xPositionForPaddle2 = xPositionForPaddle2 + 1

                screen.fill((255, 255, 255))

                screen.blit(pongPaddle2, (xPositionForPaddle2, 550))

                screen.blit(pongPaddle, dest)
                screen.blit(net, (350, 0))
                screen.blit(AiPongPaddle, (700, yForAiPongPaddleLocation))
                screen.blit(ball, (ballxPosition, ballyPosition))
                screen.blit(pongPaddle1, (xPositionForPaddle1, -15))
                screen.blit(AiPongPaddle1, (xPositionForAiPongPaddle1, -15))
                screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))

                xPositionForTopRightOfPaddle2 = xPositionForTopRightOfPaddle2 +1
                xPositionForBottomRightOfPaddle2 = xPositionForBottomRightOfPaddle2 +1
                xPositionForTopLeftOfPaddle2 = xPositionForTopLeftOfPaddle2 + 1
                xPositionForBottomLeftOfPaddle2 = xPositionForBottomLeftOfPaddle2 + 1

                xyTopLeftBoundaryForPaddle2 = (xPositionForTopLeftOfPaddle2, 570)
                xyBottomLeftBoundaryForPaddle2 = (xPositionForBottomLeftOfPaddle2, 595)
                xyTopRightBoundaryForPaddle2 = (xPositionForTopRightOfPaddle2, 570)
                xyBottomRightBoundaryForPaddle2 = (xPositionForBottomRightOfPaddle2, 595)



    if keys[pygame.K_UP] and yPosition > 60:







        yPosition = yPosition - 1
        yCoordinateForTopBoundaryOfPaddle = yCoordinateForTopBoundaryOfPaddle -1
        yCoordinateForBottomBoundaryOfPaddle = yCoordinateForBottomBoundaryOfPaddle-1
        xyForTopBoundaryOfPaddle = (20,yCoordinateForTopBoundaryOfPaddle)
        xyForBottomBoundaryOfPaddle = (20, yCoordinateForBottomBoundaryOfPaddle)
        print("yPosition")
        print(yPosition)
        yPositionForBottomTopOfPaddle = yPositionForBottomTopOfPaddle - 1
        yPositionForBottomBottomOfPaddle = yPositionForBottomBottomOfPaddle - 1
        xyPositionForBottomTopOfPaddle = (0, yPositionForBottomTopOfPaddle)
        xyPositionForBottomBottomOfPaddle = (0, yPositionForBottomBottomOfPaddle)

        yForTopRightCornerOfRect = yForTopRightCornerOfRect -1
        yForLowRightCornerOfRect = yForLowRightCornerOfRect -1
        xyForTopRightCornerOfRect = (xForTopRightCornerOfRect,yForTopRightCornerOfRect)
        xyForLowRightCornerOfRect = (xForLowRightCornerOfRect,yForLowRightCornerOfRect)
        dest = (0, yPosition)

        screen.fill((255, 255, 255))

        print(yPosition)
        screen.blit(pongPaddle, dest)
        screen.blit(net,(350,0))
        screen.blit(AiPongPaddle, (700, yForAiPongPaddleLocation))
        screen.blit(ball,(ballxPosition,ballyPosition))
        screen.blit(pongPaddle1,(xPositionForPaddle1,-15))
        screen.blit(pongPaddle2,(xPositionForPaddle2, 550))
        screen.blit(AiPongPaddle1, (xPositionForAiPongPaddle1, -15))
        screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))





    if keys[pygame.K_DOWN] and yPosition < 500 :
        print("ball y Position")
        print(ballyPosition)
        print("yForTopRightCornerOfRect")
        print(yForTopRightCornerOfRect)
        print("ball x Position")
        print(ballxPosition)
        print("xForLowRightCornerOfRect")
        print(yForLowRightCornerOfRect)
        print("ball y Position")
        print(ballyPosition)



        yPosition = yPosition + 1
        yCoordinateForTopBoundaryOfPaddle = yCoordinateForTopBoundaryOfPaddle + 1
        yCoordinateForBottomBoundaryOfPaddle = yCoordinateForBottomBoundaryOfPaddle + 1
        xyForTopBoundaryOfPaddle = (20, yCoordinateForTopBoundaryOfPaddle)
        xyForBottomBoundaryOfPaddle = (20, yCoordinateForBottomBoundaryOfPaddle)
        print("this is the yz position")
        print(yPosition)
        yForTopRightCornerOfRect = yForTopRightCornerOfRect + 1
        yForLowRightCornerOfRect = yForLowRightCornerOfRect + 1
        xyForTopRightCornerOfRect = (xForTopRightCornerOfRect, yForTopRightCornerOfRect)
        xyForLowRightCornerOfRect = (xForLowRightCornerOfRect, yForLowRightCornerOfRect)
        yPositionForBottomTopOfPaddle = yPositionForBottomTopOfPaddle + 1
        yPositionForBottomBottomOfPaddle = yPositionForBottomBottomOfPaddle + 1
        xyPositionForBottomTopOfPaddle = (0, yPositionForBottomTopOfPaddle)
        xyPositionForBottomBottomOfPaddle = (0, yPositionForBottomBottomOfPaddle)

        dest = (0,yPosition)
        screen.fill((255,255,255))
        screen.blit(net,(350,0))
        screen.blit(pongPaddle,dest)
        screen.blit(pongPaddle1, (xPositionForPaddle1, -15))
        screen.blit(pongPaddle2, (xPositionForPaddle2, 550))
        screen.blit(AiPongPaddle, (700, yForAiPongPaddleLocation))
        screen.blit(ball,(ballxPosition,ballyPosition))
        screen.blit(AiPongPaddle1, (xPositionForAiPongPaddle1, -15))
        screen.blit(AiPongPaddle2, (xPositionForAIPongPaddle2, 550))


    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.circle(screen, (0, 0, 255), xyForLeftBoundaryPongPaddle1, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyForRightBoundaryPongPaddle1, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForBottomLeftBoundaryOfPaddle1, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForBottomRightBoundaryOfPaddle1, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForBottomBottomOfPaddle, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForBottomTopOfPaddle, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyTopLeftBoundaryForPaddle2, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyBottomLeftBoundaryForPaddle2, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyTopRightBoundaryForPaddle2, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyBottomRightBoundaryForPaddle2, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255),xyPositionForUpperLeftOfAi2Paddle, 2, 2)# circle 1
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForUpperRightOfAi2Paddle, 2, 2)#circle 2
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForLowerRightOfAi2Paddle, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), xyPositionForLowerLeftOfAi2Paddle, 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), (700,300), 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), (720, 300), 2, 2)
    pygame.draw.circle(screen,(0,0,255),(700,350),2,2)
    pygame.draw.circle(screen, (0, 0, 255), (720, 350), 2, 2)
    pygame.draw.circle(screen, (0, 0, 255), (360, 300), 2, 2)



    pygame.display.update()


    pygame.display.flip()




























