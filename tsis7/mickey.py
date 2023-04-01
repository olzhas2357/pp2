import pygame
from datetime import datetime
import math
pygame.init()

width, height = 829, 836

clock = pygame.time.Clock()
font = pygame.font.SysFont("Mickey Watch", 60)
bg_sound = pygame.mixer.Sound('../../my_own_codes/pygame_3/sound/sound.mp3')
bg_sound.play()

h_width, h_height = width//2, height//2
radius = h_height - 50

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("MICKEY WATCH")
picture = pygame.image.load("mickey_watch/watch.jpg").convert_alpha()
picture_rect = picture.get_rect()
left_hand = pygame.image.load("mickey_watch/second.png")
right_hand = pygame.image.load("mickey_watch/minute.png")
left_rect = left_hand.get_rect(bottomleft=(415, 565))
right_rect = right_hand.get_rect(bottomright=(825, 600))
clock60 = dict(zip(range(60), range(0, 360, 6)))

def get_clock_pos(clock_dict, clock_hand):
    x = h_width + radius * math.cos(math.radians(clock_dict[clock_hand]) - math.pi/2)
    y = h_height + radius * math.sin(math.radians(clock_dict[clock_hand]) - math.pi/2)
    return x, y


while True:
    screen.blit(picture, picture_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pygame.quit()

    t = datetime.now()
    minute, second = t.minute, t.second

    position_minute = get_clock_pos(clock60, minute)
    a = math.atan2(position_minute[1] - (left_rect[1] + 32), position_minute[0] - (left_rect[0] + 26))
    right_hand_rot = pygame.transform.rotate(right_hand, 720 - a*57.29)
    right_rect1 = (right_rect[0] - right_hand_rot.get_rect().width / 2, right_rect[1] - right_hand_rot.get_rect().height /2)
    screen.blit(right_hand_rot, right_rect1)

    position_second = get_clock_pos(clock60, second)
    angle = math.atan2(position_second[1] - (left_rect[1] + 32), position_second[0] - (left_rect[0] + 26))
    left_hand_rot = pygame.transform.rotate(left_hand, 360 - angle * 57.29)
    left_rect1 = (left_rect[0] - left_hand_rot.get_rect().width / 2, left_rect[1] - left_hand_rot.get_rect().height / 2)
    screen.blit(left_hand_rot, left_rect1)

    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
    screen.blit(time_render, (0, 0))
    pygame.display.flip()
    clock.tick(20)

