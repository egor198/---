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
dy = 3
dx = 3
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
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
        
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

player1 = Player("player.png", 0, 0, 3, 50, 100)
player2 = Player("player.png", 650, 0, 3, 50, 100)
ball = GameSprite("ball.png", 450, 300, 4, 50, 50)

while game:
    window.fill(back)
    player1.reset()
    player1.update_r()
    player2.reset()
    player2.update_l()
    ball.reset()
    ball.rect.y += dy
    ball.rect.x += dx
    if ball.rect.y >= 400:
        dy *= -1
    if ball.rect.y <= 0:
        dy *= -1
    if sprite.collide_rect(player1, ball) :
        dx *= -1
        dx += 0.4
        dy += 0.4
    if sprite.collide_rect(player2, ball) :
        dx *= -1
        dx += 0.4
        dy += 0.4

    if ball.rect.x >= 650:
        score += 1
        #sleep(2)
        dy = randint(1, 3)
        dx = randint(-3, 3)
        ball.rect.x = 300
        ball.rect.y = 100
    if ball.rect.x <= 0:
        score1 += 1
        #sleep(2)
        dy = randint(1, 3)
        dx = randint(-3, 3)
        ball.rect.x = 300
        ball.rect.y = 100

    text = font2.render("Счет:" + str(score), 1, (0, 255, 0))
    text2 = font2.render("Счет:" + str(score1), 1, (0, 255, 0))   
    window.blit(text, (10, 20))
    window.blit(text2, (620, 20))



    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
    print(dx, dy)