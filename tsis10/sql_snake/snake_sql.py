import time
import psycopg2
import pygame, random, sys
from config import config
from sql_query import *


pygame.init()
class Map:
    def __init__(self, ref, screen):
        self.screen = screen
        self.ref = ref
        self.size = 10
        self.coords = self.rect_coords()

    def rect_coords(self):
        with open(self.ref, 'r') as file:
            rects = []
            for row_index, row in enumerate(file):
                for col_index, col in enumerate(row):
                    if col == '#':
                        rects += [pygame.Rect(col_index * self.size, row_index * self.size + 100, 10, 10)]
            return rects
    def draw(self):
        try:
            for rect in self.coords:
                pygame.draw.rect(self.screen, 'black', rect, 4)
        except:
            pass
# Чтобы сделать возможность начала игры заново я сделал из игры функцию,
# которую игрок вызывает, если после смерти он решить сыграть заново
def game():
    # Здесь я добавил константные значения, как размер экрана,
    # цвет и разметка для header-а(поле где показывается набранные очки игрока и уровень)
    class Apple:
        global screen
        def __init__(self):
            self.weight = random.randint(1, 5)
            self.lifetime = 10
            self.pos = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
            self.spawn = True
        def updates(self):
            self.pos = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
            self.weight = random.randint(1, 5)
            self.lifetime = 10
    screen = pygame.display.set_mode((400, 500))
    SNAKE_COLOR = 'black'
    BG_COLOR = (37, 19, 102)
    APPLE_COLOR = 'black'
    HEADER_LINE_START = (0, 100)
    HEADER_LINE_END = (400, 100)
    level = 0
    a1 = Apple()
    time_before_d = 0
    clock = pygame.time.Clock()
    running = True
    main_menu = True
    esc = False
    score = 0
    score_font = pygame.font.SysFont('lunchtime Doubly So', 32)
    levels = [Map('level/level0.txt', screen),Map('level/level1.txt', screen),Map('level/level2.txt', screen),Map('level/level3.txt', screen),Map('level/level4.txt', screen)]

    # Здесь я прописал начальную позицию змей и добавил элемент который определять куда должен повернутся и движется змея
    change = 'left' # указывает куда должен повернутся
    direction = 'left' # показывает куда двигалась до этого змея и из-за change меняет направление
    # это сделанно чтобы змея не меняло свое направление на противоположное



    # Cпециальный ивент для уменьшения время жизни яблока,
    # у меня в игре яблоко имеет "жизни" и этот ивент убирает одну единицу жизни
    # Чтобы яблоко исчезла
    minuslife = pygame.USEREVENT + 1
    pygame.time.set_timer(minuslife, 1000)

    level_change = False
    time_now = 0
    time_before = 0

    flash = pygame.USEREVENT + 2
    pygame.time.set_timer(flash, 1000)
    input_rect = pygame.Rect(100, 200, 158, 30)
    base_font = pygame.font.SysFont(None, 32)
    user_text = ''
    active = True
    enter = pygame.image.load('icon_sql_snake.png')
    interval_flash_interval = 300  # in milliseconds
    interval_last_flash_time = 0
    interval_color = 'black'

    while main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[0: -1]
                    elif event.key == pygame.K_RETURN:
                        if len(user_text) > 3:
                            main_menu = False
                        else:
                            continue
                    elif event.key != pygame.K_SPACE:
                        if len(user_text) < 10:
                            user_text += event.unicode
        if active:
            current_time = pygame.time.get_ticks()
            if current_time - interval_last_flash_time >= interval_flash_interval:
                interval_last_flash_time = current_time
                if interval_color == 'black':
                    interval_color = BG_COLOR
                else:
                    interval_color = 'black'
        else:
            interval_color = 'black'

        screen.fill(BG_COLOR)


        text_surface = base_font.render(user_text, True, 'black')
        pygame.draw.rect(screen, interval_color, input_rect, 2)
        screen.blit(enter, pygame.Rect(260, 192, 32, 32))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))


        pygame.display.update()
        clock.tick(60)
    conn = None
    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()


    player_pos = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]] # вся змея



    cur.execute(sql_check_of_exist, (user_text,))
    count = cur.fetchone()[0]
    cur.execute("SELECT score, x, y FROM score WHERE nickname = %s", (user_text,))

    pause = False
    if count != 0:
        SCORE, x, y = cur.fetchone()
        player_pos = [x, y]
        snake = [[x, y], [x+10, y], [x + 20, y]]
        pause = True
        while True:
            screen.fill(BG_COLOR)
            screen.blit(score_font.render(f'YOUR SCORE: {SCORE}', True, 'black'), (100, 200))
            pygame.display.update()
            time.sleep(1)
            break

        score = SCORE

    level = score // 4
    while running:
        '''
        Игрок только меняет направление движения змей, а змея уже сама движется без остановки по направлению
        За счет такого способа, мы избегаем того что змея может направиться в противоположную сторону
        Из-за этого он просто бы бился бы об себя
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_KP_8:
                    change = 'up'
                if event.key == pygame.K_s or event.key == pygame.K_KP_2:
                    change = 'down'
                if event.key == pygame.K_a or event.key == pygame.K_KP_4:
                    change = 'left'
                if event.key == pygame.K_d or event.key == pygame.K_KP_6:
                    change = 'right'
                if event.key == pygame.K_ESCAPE:
                    esc = True
                    running = False
            if event.type == minuslife:
                print(1)
                a1.lifetime -= 1
                if a1.lifetime == 0:
                    a1.updates()

        if direction != 'up' and change == 'down':
            direction = 'down'
        if direction != 'down' and change == 'up':
            direction = 'up'
        if direction != 'left' and change == 'right':
            direction = 'right'
        if direction != 'right' and change == 'left':
            direction = 'left'

        if direction == 'up':
            player_pos[1] -= 10
        if direction == 'down':
            player_pos[1] += 10
        if direction == 'left':
            player_pos[0] -= 10
        if direction == 'right':
            player_pos[0] += 10

        # Логика по которой яблоко респавниться после поедания
        while a1.spawn:
            a1.updates()
            if a1.pos not in snake:
                a1.spawn = False

        # Змея растёт постоянно, но только когда она съедает яблоко, она сохраняет свой размер
        # Съедания значить то что координаты головы змей и яблока совпали
        snake.insert(0, list(player_pos))

        if player_pos[0] == a1.pos[0] and player_pos[1] == a1.pos[1]:
            score += a1.weight
            a1.spawn = True
            old_level = level
            level = score // 4
            if level > len(levels) - 1:
                level = len(levels) - 1
            if level > old_level:
                print(1)
                level_change = True
                time_before = pygame.time.get_ticks()
        else:
            snake.pop()
        if (a1.pos[0], a1.pos[1], 10, 10) in levels[level].coords:
            a1.spawn = True
        time_now = pygame.time.get_ticks()
        screen.fill(BG_COLOR)




        pygame.draw.line(screen, 'black', HEADER_LINE_START, HEADER_LINE_END, 1)

        # Условия при которых игрок проигрывает. Прерывается сама игра, и сразу же начинается следующий цикл
        if ((player_pos[0] < -5 or player_pos[0] > screen.get_width() - 5) or (
                player_pos[1] < 100 or player_pos[1] > screen.get_height() - 5)):
            break
        if level_change:
            if time_now - time_before > 2000:
                level_change = False
                if (player_pos[0], player_pos[1], 10, 10) in levels[level].coords:
                    pause = False
                    break
        else:
            if (player_pos[0], player_pos[1], 10, 10) in levels[level].coords:
                if pause:
                    time_before_d = pygame.time.get_ticks()
                pause = False
                if time_now - time_before_d > 1000:
                    print(time_before_d)
                    break
        if player_pos in snake[1:]:
            break

        # Отрисовка элементов игры(змея, яблоко, показатели, четра для отделения игрового поля и показателей)
        for pos in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(a1.pos[0], a1.pos[1], 10, 10))
        screen.blit(score_font.render(f'Score: {score}', True, 'black'), (20, 38))
        levels[level].draw()
        pygame.display.update()

        clock.tick(15) # Изменение скорости змей

    if esc:
        cur.execute(sql_check_of_exist, (user_text,))
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute(sql_insert, (user_text, int(score), player_pos[0], player_pos[1]))
        else:
            cur.execute(sql_update, (user_text, int(score), player_pos[0], player_pos[1]))
    else:
        cur.execute(sql_clear, (user_text, ))


    conn.commit()
    conn.close()
    cur.close()



    # Цикл для меню выбора после проигрыша игрока
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game()
                if event.key == pygame.K_q:
                    running = False
        screen.fill(BG_COLOR)

        screen.blit(score_font.render('Press R for restart or Q for quit', True, 'black'), (35, 200))
        pygame.display.update()


game()

pygame.quit()