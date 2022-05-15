from pygame import *
import time as t

mixer.init()
font.init()
#import time
from random import randint
#создай окно игры
font2 = font.SysFont("Arial", 25)
font3 = font.SysFont("Arial", 50)
window = display.set_mode((700, 500))
display.set_caption("Пин-понг")
win_width = 700
win_hight = 500
backrround = transform.scale(image.load("fon.jpg"), (700, 500))


clock = time.Clock()
FPS = 60
game = True
score = 0
lost = 0
finish = True
c = True
q = 1
e = 1
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
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
        
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

player1 = Player("player.png", 0, 0, 2, 50, 100)
player2 = Player("player.png", 650, 0, 2, 50, 100)
while game:
    window.blit(backrround, (700, 500))
    player1.reset()
    player1.update_r()
    player2.reset()
    player2.update_l()


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)



