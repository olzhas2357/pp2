import pygame
from pygame.locals import *
import time
import random
pygame.init()

FramePerSec = pygame.time.Clock()
FPS = 60

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

width = 400
height = 600
speed = 5
score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CARS")
street = pygame.image.load("image/AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/car1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("image/car2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 500)

    def move(self):
        keys = pygame.key.get_pressed()
        # if keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if keys[K_DOWN]:
        #     self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

E1 = Enemy()
P1 = Player()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)


while True:

    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5

        if event.type == QUIT:
            exit()

    scores = font_small.render(f"SCORE: {str(score)}", True, BLACK)
    screen.blit(scores, (10, 10))

    screen.blit(street, (0, 0))
    screen.blit(scores, (10, 10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('image/crash2.mp3').play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:

            entity.kill()
        time.sleep(2)
        exit()

    # screen.blit()
    pygame.display.update()
    FramePerSec.tick(FPS)



