import pygame
pygame.init()


X = 500
Y = 500
white = (255,255,255)
black = (0, 0, 0)
blue = (90,90,250)

display = pygame.display.set_mode([X, Y])
pygame.display.set_caption('My Awesome Game')
running = True

while running:

    display.fill(black)
    pygame.draw.line(display, white,  [100, 100], [200, 200], 5)
    pygame.display.flip()