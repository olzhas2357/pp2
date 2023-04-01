import pygame


# Making canvas
screen = pygame.display.set_mode((900, 700))

# Setting Title
pygame.display.set_caption('GFG Paint')

draw_on = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (196, 35, 159)
list_1 = [WHITE, RED, GREEN, BLUE, PINK]


def circle():
    pygame.draw.circle(screen, WHITE, center=(450, 350), radius=42, width=5)
def rect():
    x, y = 50, 50
    pygame.draw.rect(screen, WHITE, rect=(100, 400, x, y), width = 5)
def draw():
    x = 15
    w = 85
    for i in range(5):
        pygame.draw.rect(screen, list_1[i], (x + 100*i, x, w, w))
    pygame.draw.circle(screen, WHITE, center = (657, 57), radius = 42, width = 5)
draw()

def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

# def roundRect(canvas, color, start, end, radius=1) :
#     Xaxis = end[0] - start[0]
#     Yaxis = end[1] - start[1]
#     dist = max(abs(Xaxis), abs(Yaxis))
#     for i in range(dist) :
#         x = int(start[0] + float(i) / dist * Xaxis)
#         y = int(start[1] + float(i) / dist * Yaxis)
#         pygame.draw.rect(canvas, color, pygame.Rect(start[0], start[1], x, y), width = radius)

mouse = pygame.mouse.get_pos()
color = list_1[0]
try:
    while True :
        for e in pygame.event.get():

            if e.type == pygame.QUIT :
                raise StopIteration
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    color = list_1[0]
                elif e.key == pygame.K_2:
                    color = list_1[1]
                elif e.key == pygame.K_3:
                    color = list_1[2]
                elif e.key == pygame.K_4:
                    color = list_1[3]
                elif e.key == pygame.K_5:
                    color = list_1[4]
                elif e.key == pygame.K_6:
                    color = BLACK
                elif e.key == pygame.K_UP:
                    radius +=2
                elif e.key == pygame.K_DOWN:
                    radius-=2
                elif e.key == pygame.K_o:
                    circle()
                elif e.key == pygame.K_s:
                    rect()

            if e.type == pygame.MOUSEBUTTONDOWN :
                # Draw a single circle when even mouse is clicked down.
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True
            # When mouse button released it will stop drawing
            if e.type == pygame.MOUSEBUTTONUP :
                draw_on = False
            # It will draw a continuous circle with the help of roundline function.
            if e.type == pygame.MOUSEMOTION :
                if draw_on :
                    pygame.draw.circle(screen, color, e.pos, radius)
                    roundline(screen, color, e.pos, last_pos, radius)
                last_pos = e.pos
            pygame.display.flip()

except StopIteration:
    pass

# Quit
pygame.quit()