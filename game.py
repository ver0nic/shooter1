from pygame import *
from random import randint

window = display.set_mode((900, 600))
display.set_caption('Shooter')

background = image.load('galaxy.jpg')
background = transform.scale (background, (900, 600))

clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
shoot = mixer.Sound('fire.ogg')

lost = 0
score = 0

class GameSprite(sprite.Sprite):
    def __init__(self, img, x_pos, y_pos, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = speed
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        pressed = key.get_pressed()
        if pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if pressed[K_d] and self.rect.x < 840:
            self.rect.x += self.speed

    def fire(self):
        pass

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed

        if self.rect.y >= 600:
            self.rect.x = randint(0, 900-80)
            self.rect.y = 0

player = Player('rocket.png', 400, 480, 10, 50, 100)
enemies = sprite.Group()
for i in range(7):
    enemy = Enemy('ufo.png', randint(0, 900-80), 0, randint(1,5), 80, 40)
    enemies.add(enemy)
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if not finish:
            window.blit(background, (0, 0))
            player.draw()
            player.update()

            enemies.draw(window)
            enemies.update()

    display.update()
    clock.tick(FPS)

