from types import DynamicClassAttribute
from xml.dom import DOMException
from pygame import *
import time as t

mixer.init()
font.init()
#import time
from random import randint
#создай окно игры
font2 = font.SysFont("Arial", 25)
font3 = font.SysFont("Arial", 50)
window = display.set_mode((700, 450))
display.set_caption("Пин-понг")
back = 200, 255, 255
win_width = 700
win_hight = 500
window.fill(back)
list = [-3, -2, -1, 1, 2, 3]
dy = randint(-3, 3)
dx = randint(-3, 3)
dy1 = randint(-3, 3)
dx1 = randint(-3, 3)
dy2 = randint(-3, 3)
dx2 = randint(-3, 3)
dy3 = randint(-3, 3)
dx3 = randint(-3, 3)
dy4 = randint(-3, 3)
dx4 = randint(-3, 3)
score = 0
score1 = 0


clock = time.Clock()
FPS = 60
game = True
finish = True


#ВСЕ КЛАССЫ
class GameSprite(sprite.Sprite):
    def __init__(self, background, player_x, player_y, player_speed, sizex, sizey):
        super().__init__()
        self.image = transform.scale(image.load(background), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0 :
            self.rect.y -= self.speed 
        if keys_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 440:
            self.rect.y += self.speed

player1 = Player("player.png", 100, 100, 3, 50, 50)
ball = GameSprite("ball.png", randint(0, 600), randint(0, 400), 4, 50, 50)
ball1 = GameSprite("ball.png", randint(0, 600), randint(0, 400), 4, 50, 50)
ball2 = GameSprite("ball.png", randint(0, 600), randint(0, 400), 4, 50, 50)
ball3 = GameSprite("ball.png", 450, 300, 4, 50, 50)
ball4 = GameSprite("ball.png", 450, 300, 4, 50, 50)
while game:
    window.fill(back)
    player1.reset()
    player1.update_r()
    ball.reset()
    ball1.reset()
    ball2.reset()
    ball3.reset()
    ball4.reset()

    ball.rect.y += dy
    ball.rect.x += dx
    if ball.rect.y >= 400 or ball.rect.y <= 0:
        dy *= -1
    if ball.rect.x >= 650 or ball.rect.x <= 0:
        dx *= -1

    ball1.rect.y += dy1
    ball1.rect.x += dx1
    if ball1.rect.y >= 400 or ball1.rect.y <= 0:
        dy1 *= -1
    if ball1.rect.x >= 650 or ball1.rect.x <= 0:
        dx1 *= -1

    ball2.rect.y += dy2
    ball2.rect.x += dx2
    if ball2.rect.y >= 400 or ball2.rect.y <= 0:
        dy2 *= -1
    if ball2.rect.x >= 650 or ball2.rect.x <= 0:
        dx2 *= -1
        
    
    ball3.rect.y += dy3
    ball3.rect.x += dx3
    if ball3.rect.y >= 400 or ball3.rect.y <= 0:
        dy3 *= -1
    if ball3.rect.x >= 650 or ball3.rect.x <= 0:
        dx3 *= -1
    
    
    ball4.rect.y += dy4
    ball4.rect.x += dx4
    if ball4.rect.y >= 400 or ball4.rect.y <= 0:
        dy4 *= -1
    if ball4.rect.x >= 650 or ball4.rect.x <= 0:
        dx4 *= -1

    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player1, ball1) or sprite.collide_rect(player1, ball2) or sprite.collide_rect(player1, ball3) or sprite.collide_rect(player1, ball4):
        game = False

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
    print(dx, dy)