import pygame

pygame.init()
width = 512
height = 512
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MUSIC")
music_files = ["sound/music.mp3", "sound/sound.mp3", "sound/sza.mp3"]
bg = pygame.image.load('image/surface.png')
bg_pausa = pygame.image.load('image/pausa.png')
bg_left = pygame.image.load('image/left.png')

font = pygame.font.Font(None, 20)
pygame.mixer.music.load(music_files[0])

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_music():
    global current_music
    current_music = (current_music + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music])
    pygame.mixer.music.play()

def prev_music():
    global current_music
    current_music = (current_music - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_music])
    pygame.mixer.music.play()

current_music = 0
play_music()

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    screen.blit(bg_pausa, (150, 10))
    screen.blit(bg_left, (250, 10))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if keys[pygame.K_SPACE]:
        if pygame.mixer.music.get_busy():
            stop_music()
        else:
            play_music()

    elif keys[pygame.K_LEFT]:
        next_music()
    elif keys[pygame.K_RIGHT]:
        prev_music()

    text = font.render("Press SPACE to play/pause, LEFT/RIGHT to change music", True, (0, 0, 0))
    text_rect = text.get_rect(center=(256, 500))
    screen.blit(text, text_rect)
    pygame.display.flip()