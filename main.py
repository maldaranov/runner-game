import pygame
from sys import exit

# initial setup and variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner-game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# general surfaces
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/Ground.png').convert_alpha()
text_surface = test_font.render('Look, it\'s a snail!', False, 'Black')

# entity surfaces
player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

# entity rectangles
player_rect = player_surface.get_rect(midbottom = (80, 300))
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    screen.blit(snail_surface, snail_rect)
    snail_rect.left = (snail_rect.left - 5) % 800
    screen.blit(player_surface, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)