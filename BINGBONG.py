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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


plauer1 = Player('slon.png', 50, 400, 90, 110, 15)
plauer2 = Player('bron.png', 550, 400, 90, 110, 15)
bill = GameSprite('oler.png', 200, 200, 40, 40, 10)

font.init()
font1 = font.SysFont('Arial', 60)
win_l = font1.render('YOUSl WIN!!!', True, (255, 215, 0))
win_r = font1.render('YOUSr WIN!!!', True, (155, 115, 0))
lose_l = font1.render('YOUSl deid hahahaha', True, (77,222,22))
lose_r = font1.render('YOUSr deid hahahaha', True, (177,22,22))

speed_x = 3
speed_y = 3

run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))
        bill.rect.x += speed_x
        bill.rect.y += speed_y
        if bill.rect.y > win_height-50 or bill.rect.y <0:
            speed_y *= -1
        if sprite.collide_rect(plauer1, bill) or sprite.collide_rect(plauer2, bill):
            speed_x *= -1
        if bill.rect.x < 0:
            finish = True
            window.blit(lose_l, (202, 202))
        if bill.rect.x > win_width:
            finish = True
            window.blit(lose_r, (202, 202))
        plauer1.update_l()
        plauer1.reset()
        plauer2.update_r()
        plauer2.reset()
        bill.reset()


    display.update()
    clock.tick(FPS)