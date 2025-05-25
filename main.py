import sys
import pygame
from doro import Doro
from orange import Orange
from cat import  Cat
import begin, end

def game_lose():
    end.game_over1(screen)
    return True

def game_win():
    end.game_over2(screen, score)
    return True

def start_game():
    begin.start(screen)

pygame.init()
# create display screen
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
# set clock to control the frame rate
clock = pygame.time.Clock()

# load Doro and orange
doro = Doro(frame_folder='doro_element')
orange = Orange(img_path='orange.png', screen_width=width, screen_height=height)
cat = Cat(frame_folder='cat_element', screen_width=width, screen_height=height )

# set the game time
score = 0
game_time = 20 * 1000
start_time = pygame.time.get_ticks()

# show start page
start_game()

while True:
    cur_time = pygame.time.get_ticks()
    elapsed_time = cur_time - start_time
    remaining_time = max(0, game_time - elapsed_time)

    if remaining_time == 0:
        if game_win():
            score = 0
            start_time = pygame.time.get_ticks()
            doro = Doro(frame_folder='doro_element')
            orange = Orange(img_path='orange.png', screen_width=width, screen_height=height)
            cat = Cat(frame_folder='cat_element', screen_width=width, screen_height=height)

    # draw all elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # fill screen color
    screen.fill(pygame.Color(255, 255, 255))

    # receive gamer input to move doro
    doro.move(screen_width=width, screen_height=height)
    doro.update()
    # put doro on the screen
    doro.draw(screen)

    # put a cat to chase doro
    cat.chase(doro_x=doro.pos_x,doro_y=doro.pos_y)
    cat.update()
    cat.draw(screen)

    # put orange on the screen
    orange.draw(screen)

    # if doro get the orange then spawn a new
    if doro.get_rect().colliderect(orange.get_rect()):
        orange.orange_spawn()
        score += 1

    # if cat catch up doro
    if doro.get_rect().colliderect(cat.get_rect()):
        if game_lose():
            score = 0
            start_time = pygame.time.get_ticks()
            doro = Doro(frame_folder='doro_element')
            orange = Orange(img_path='orange.png', screen_width=width, screen_height=height)
            cat = Cat(frame_folder='cat_element', screen_width=width, screen_height=height)

    font = pygame.font.SysFont(None, 36)
    time_text = font.render(f"Time: {remaining_time // 1000}", True, (255, 0, 235))
    score_text = font.render(f"Score: {score}", True, (255, 0, 235))
    screen.blit(time_text, (10, 10))
    screen.blit(score_text, (10, 50))

    pygame.display.update()
    # set the FPS equals 60
    clock.tick(60)