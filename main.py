import pygame
from sys import exit
from enum import Enum

# init
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
GAME_STATE = "active"
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("runner-game")
game_font = pygame.font.Font("font/Pixeltype.ttf", 50)
start_time = 0

# game state class
class State(Enum):
    PLAYING = 0
    GAME_OVER = 1
state = State.PLAYING

# score function
def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_surf = game_font.render(f"{current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (WINDOW_WIDTH/2, 50))
    screen.blit(score_surf, score_rect)

# background-init
sky_surf = pygame.image.load("graphics/Sky.png").convert_alpha()
ground_surf = pygame.image.load("graphics/Ground.png").convert_alpha()

# player-init
player_surf = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

# snail-init
snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # event loop if game is running
        if (state == State.PLAYING):
            # player jump by pressing on the character model
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity = -20

            # player jump by pressing "space" key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity = -20

        # event loop if game is over
        elif (state == State.GAME_OVER):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                state = State.PLAYING
                snail_rect.left = 600
                start_time = pygame.time.get_ticks()

    # draw loop if game is running
    if (state == State.PLAYING):
        # background-draw
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))

        # score-draw
        display_score()

        # snail-draw
        snail_rect.left = (snail_rect.left - 5) % WINDOW_WIDTH
        screen.blit(snail_surf, snail_rect)

        # player-draw
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # collisions
        if snail_rect.colliderect(player_rect):
            state = State.GAME_OVER
    
    # draw loop if game is over
    elif (state == State.GAME_OVER):
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)