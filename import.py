import pygame
pygame.init()
X = 500
Y = 500
yellow = (240,255,15)
navyblue = (30, 0, 180)
display = pygame.display.set_mode([X, Y])

running = True

while running:

    display.fill(yellow)
    pygame.draw.circle(display, navyblue, (200, 200), 100)
    pygame.display.flip()