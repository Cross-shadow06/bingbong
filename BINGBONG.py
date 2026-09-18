from pygame import *
from random import randint

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('bingbong')
background = transform.scale(image.load('corn.jpg'), (win_width, win_height))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed


plauer1 = Player('slon.png', 50, 400, 80, 100, 15)
plauer2 = Player('bron.png', 50, 400, 80, 100, 15)

font.init()
font1 = font.SysFont('Arial', 60)
win = font1.render('YOUS WIN!!!', True, (255, 215, 0))
lose = font1.render('YOUS deid hahahaha', True, (177,22,22))

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))
        plauer1.update()
        plauer1.reset()
        plauer2.update()
        plauer2.reset()
'''
        if totol >= 10:
            window.blit(win, (200, 250))
            finish = True
        if lost >= 5 or life <= 0:
            window.blit(lose, (200, 250))
            finish = True
'''

    display.update()
    clock.tick(FPS)