import pygame
from sys import exit

# initial setup and variables
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('runner-game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# surfaces
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/Ground.png')
text_surface = test_font.render('Look, it\'s a snail!', False, 'Black')

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
    snail_x_pos = (snail_x_pos - 4) % 800

    pygame.display.update()
    clock.tick(60)