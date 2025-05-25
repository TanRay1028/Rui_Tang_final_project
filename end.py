import pygame,sys

def game_over1(screen):
    screen.fill((255, 255, 255))
    font1 = pygame.font.SysFont(None, 72)
    font2 = pygame.font.SysFont(None, 48)
    text1 = font1.render("Game Over!", True, (255, 0, 235))
    text2 = font2.render(f"Oh no, the cat stole all your oranges!", True, (50, 50, 50))
    text3 = font2.render("Press ENTER to play again", True, (50, 50, 50))

    rect1 = text1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
    rect2 = text2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.3))
    rect3 = text3.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.8))

    screen.blit(text1, rect1)
    screen.blit(text2, rect2)
    screen.blit(text3, rect3)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return


def game_over2(screen, score):
    screen.fill((255, 255, 255))
    font1 = pygame.font.SysFont(None, 72)
    font2 = pygame.font.SysFont(None, 48)
    text1 = font1.render("You win!", True, (255, 0, 235))
    text2 = font2.render(f"Doro got  {score}  oranges for you", True, (50, 50, 50))
    text3 = font2.render("Press ENTER to play again", True, (50, 50, 50))

    rect1 = text1.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
    rect2 = text2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2.3))
    rect3 = text3.get_rect(center=(screen.get_width() // 2, screen.get_height() // 1.8))

    screen.blit(text1, rect1)
    screen.blit(text2, rect2)
    screen.blit(text3, rect3)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
