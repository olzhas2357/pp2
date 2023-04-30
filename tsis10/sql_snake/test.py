import pygame

pygame.init()

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the font
font = pygame.font.Font(None, 30)

# Set up the textbox
textbox_rect = pygame.Rect(screen_width/2-100, screen_height/2-25, 200, 50)
textbox_surface = pygame.Surface((200, 50))
textbox_surface.fill(WHITE)

# Set up the interval
interval_rect = pygame.Rect(screen_width/2-50, screen_height/2-100, 100, 50)
interval_surface = pygame.Surface((100, 50))
interval_surface.fill(WHITE)
interval_color = WHITE
interval_flash_interval = 500  # in milliseconds
interval_last_flash_time = 0

# Set up the clock
clock = pygame.time.Clock()

# Start the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Set the focus to the textbox when the user presses enter
                pygame.key.set_mods(pygame.KMOD_NONE)  # reset key modifiers
                pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_TAB, 'mod': 0}))

    # Check if the textbox is focused and flash the interval if it is
    if pygame.key.get_focused() and textbox_rect.collidepoint(pygame.mouse.get_pos()):
        current_time = pygame.time.get_ticks()
        if current_time - interval_last_flash_time >= interval_flash_interval:
            interval_last_flash_time = current_time
            if interval_color == WHITE:
                interval_color = BLACK
            else:
                interval_color = WHITE
    else:
        interval_color = WHITE

    # Draw the elements on the screen
    screen.fill(BLACK)
    screen.blit(textbox_surface, textbox_rect)
    interval_surface.fill(interval_color)
    screen.blit(interval_surface, interval_rect)

    # Update the display and wait for the next frame
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()