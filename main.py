import pygame
from sys import exit

# initial setup and variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner-game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/Ground.png').convert_alpha()
text_surface = test_font.render('Look, it\'s a snail!', False, 'Black')
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()

# rectangles
player_rect = player_surface.get_rect(midbottom = (80, 300))

# entities
snail_surface = pygame.image.load('graphics/snail/snail1.png')

# coordinates
snail_x_pos = 600

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, (snail_x_pos, 250))
    screen.blit(player_surface, player_rect)
    snail_x_pos = (snail_x_pos - 4) % 800

    pygame.display.update()
    clock.tick(60)