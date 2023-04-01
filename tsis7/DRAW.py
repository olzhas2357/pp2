import pygame

pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BALL")
clock = pygame.time.Clock()
icon = pygame.image.load("image/ball.png")
pygame.display.set_icon(icon)

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.dx, self.dy = 0, 0
    def update(self, * args):
        self.rect.x += self.dx
        self.dx = 0
        self.rect.y += self.dy
        self.dy = 0

ball = Object(400, 400, "image/ball.png")
running = True
while running:

    screen.fill("black")
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball.dy = -20
    if keys[pygame.K_DOWN]:
        ball.dy = 20
    if keys[pygame.K_LEFT]:
        ball.dx = -20
    if keys[pygame.K_RIGHT]:
        ball.dx = 20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.blit(ball.image, ball.rect)
    ball.update()
    clock.tick(60)
    pygame.display.flip()

#import pygame
#import sys
# pygame.init()
# size = width, height = 1700, 1000
# speed = [2, 2]
# black = 0, 0, 0
#
# screen = pygame.display.set_mode(size)
#
# ball = pygame.image.load('image/ball.png')
# ballrect = ball.get_rect()
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
#             if event.key == pygame.K_w:
#                 sys.exit()
#
#     ballrect = ballrect.move(speed)
#
#     if ballrect.left < 0 or ballrect.right > width:
#         speed[0] = - speed[0]
#     elif ballrect.top < 0 or ballrect.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(black)
#     screen.blit(ball, ballrect)
#     pygame.display.flip()