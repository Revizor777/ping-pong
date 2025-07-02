import pygame
from random import randint, randrange
import math
pygame.init()

window=pygame.display.set_mode((500, 800))
background=pygame.transform.scale(pygame.image.load('table1.png'), (500, 800))
clock=pygame.time.Clock()
clock.tick(40)
key_pressed=[]

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, player_image, speed, height, width):
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load(player_image), (height, width))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.speed=speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Racket(GameSprite):
    def update(self):
        key_pressed1=pygame.key.get_pressed()
        if key_pressed1[pygame.K_RIGHT] and self.rect.x<420:
            self.rect.x+=self.speed
        if key_pressed1[pygame.K_LEFT] and self.rect.x>0:
            self.rect.x-=self.speed
class Ball(GameSprite):
    def __init__(self, x, y, player_image, speed, height, width, angle):
        super().__init__(x, y, player_image, speed, height, width)
        self.angle=angle
    def check(self):
        if self.rect.y>0 and self.rect.y<770:
            if (self.angle>=0 and self.angle<90):
                self.angle+=(90-self.angle)*2
            elif (self.angle>=180 and self.angle<270):
                self.angle+=(270-self.angle)*2
            elif (self.angle>=90 and self.angle<180):
                self.angle=(90-(self.angle-90))
            elif (self.angle>=270 and self.angle<360):
                self.angle=(270-(self.angle-270))
        if self.rect.y>=770:
            if (self.angle>=90 and self.angle<180):
                self.angle+=(180-self.angle)*2
            elif (self.angle>=0 and self.angle<90):
                self.angle=360-self.angle
        if self.rect.y<=0:
            if (self.angle>=180 and self.angle<270):
                self.angle=(180-(self.angle-180))
            elif (self.angle>=270 and self.angle<360):
                self.angle=0+(360-self.angle)
        print(self.angle)
    def update(self):
        while self.angle>360:
            self.angle-=360
        while self.angle<=0:
            self.angle+=100
        if self.rect.y<=0:
            self.check()
        if self.rect.y>=770:
            self.check()
        if self.rect.x<=0:
            self.check()
        if self.rect.x>=470:
            self.check()
        self.rect.x+=self.speed*math.cos(math.radians(self.angle))
        self.rect.y+=self.speed*math.sin(math.radians(self.angle))
class Oponent(GameSprite):
    def chasing(self, ball):
        if ball.rect.y<=400:
            if (ball.angle>=180 and ball.angle<270) and ball.rect.x>=self.rect.x:
                if not pygame.sprite.collide_rect(ball, self) and self.rect.x<=420:
                    self.rect.x+=self.speed
            if (ball.angle>=180 and ball.angle<270) and ball.rect.x<=self.rect.x:
                if not pygame.sprite.collide_rect(ball, self) and self.rect.x>=0:
                    self.rect.x-=self.speed
            if (ball.angle>=270 and ball.angle<360) and ball.rect.x<=self.rect.x:
                if not pygame.sprite.collide_rect(ball, self) and self.rect.x>=0:
                    self.rect.x-=self.speed
            if (ball.angle>=270 and ball.angle<360) and ball.rect.x>=self.rect.x:
                if not pygame.sprite.collide_rect(ball, self) and self.rect.x<=420:
                    self.rect.x+=self.speed










racket=Racket(410, 670, 'racket.png', 7, 80, 100)                               
ball=Ball(100, 100, 'ball.png', 10, 30, 30, 45)
robot=Oponent(410, 10, 'racket2.png', 7, 80, 100)




while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    if pygame.sprite.collide_rect(racket, ball):
        if (ball.angle>=90 and ball.angle<180):
            ball.angle+=((180-ball.angle)*2+randint(-50, 50))
        elif (ball.angle>=0 and ball.angle<90):
            ball.angle=(360-ball.angle-randrange(-50, 60, 10))
    if pygame.sprite.collide_rect(robot, ball):
        if (ball.angle>=180 and ball.angle<270):
            ball.angle=(180-(ball.angle-180)+randrange(-50, 60, 10))
        elif (ball.angle>=270 and ball.angle<360):
            ball.angle=(0+(360-ball.angle)+randrange(-50, 60, 10))
    window.blit(background, (0, 0)) 
    racket.update()
    racket.draw()
    robot.chasing(ball)
    robot.draw()
    ball.update()
    ball.draw()
    pygame.display.update()
    clock.tick(40)

