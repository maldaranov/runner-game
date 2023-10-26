import pygame
from sys import exit

# init
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner-game')
clock = pygame.time.Clock()

# score-init
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
score_surf = score_font.render('Look, it\'s a snail!', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400,50))

# background-init
sky_surf = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('graphics/Ground.png').convert_alpha()

# player-init
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))
player_gravity = 0

# snail-init
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20
    
    # background-draw
    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))

    # score-draw
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    screen.blit(score_surf, score_rect)

    # snail-draw
    snail_rect.left = (snail_rect.left - 5) % 800
    screen.blit(snail_surface, snail_rect)

    # player-draw
    player_gravity += 1
    player_rect.y += player_gravity
    screen.blit(player_surface, player_rect)

    pygame.display.update()
    clock.tick(60)