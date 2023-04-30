import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = (255, 0,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (196, 35, 159)
list_1 = [WHITE, RED, GREEN, BLUE, PINK]


class GameObject:
    def draw(self):
        raise NotImplementedError

    def handle(self, mouse_pos):
        raise NotImplementedError

class Button:
    def __init__(self):
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 - 20, 20, 40, 40),
            width = 5
        )

    def draw(self):
        self.rect = pygame.draw.rect(
            SCREEN,
            WHITE,
            (WIDTH // 2 - 20, 20, 40, 40),
            width = 5
        )

class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points = []  # [(x1, y1), (x2, y2)]

    def draw(self):
        for idx, value in enumerate(self.points[:-1]):
            pygame.draw.line(
                SCREEN,
                WHITE,
                start_pos=value,  # self.points[idx]
                end_pos=self.points[idx + 1],
            )

    def handle(self, mouse_pos):
        self.points.append(mouse_pos)


class Circle(GameObject):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.start_pos = None
        self.end_pos = None

    def draw(self):
        pygame.draw.circle(
            SCREEN,
            list_1[0],
            self.center,
            self.radius,
            width=5
        )

    def handle(self, mouse_pos):
        self.radius = max(abs(mouse_pos[0] - self.center[0]),
                          abs(mouse_pos[1] - self.center[1]))

class Rectangle(GameObject):
    def __init__(self, start_pos):
        self.start_pos = start_pos  # (x1, y1)
        self.end_pos = start_pos  # (x2, y2)

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])
        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])
        pygame.draw.rect(
            SCREEN,
            list_1[0],
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

def main():
    running = True
    clock = pygame.time.Clock()
    active_obj = None
    button = Button()
    objects = [button, ]
    current_shape = Pen

    while running:
        SCREEN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                else:
                    active_obj = current_shape(start_pos=event.pos)

            if event.type == pygame.MOUSEMOTION and active_obj is not None:
                active_obj.handle(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
                objects.append(active_obj)
                active_obj = None

        for obj in objects:
            obj.draw()
        clock.tick(30)
        pygame.display.flip()


if __name__ == '__main__':
    main()