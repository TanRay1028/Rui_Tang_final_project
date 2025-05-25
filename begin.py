import pygame,sys
def start(screen):
    screen.fill((255, 255, 255))
    title = 'Welcome to Doro Adventure!'
    subtitle = 'Press any arrows key to start'
    font_title = pygame.font.SysFont(None, 72)
    font_subtitle = pygame.font.SysFont(None, 48)
    text_title = font_title.render(title, True, (255, 0, 235))
    text_subtitle = font_subtitle.render(subtitle, True, (50, 50, 50))
    rect_title = text_title.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.5))
    rect_subtitle = text_subtitle.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_title, rect_title)
    screen.blit(text_subtitle, rect_subtitle)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False