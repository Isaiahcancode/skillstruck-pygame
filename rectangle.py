import pygame
pygame.init()

X = 550
Y = 550
white = (255,255,255)
black = (0, 0, 0)
blue = (90,90,250)

display = pygame.display.set_mode([X, Y])
pygame.display.set_caption('My Awesome Game')
running = True

while running:

    display.fill(white)
    pygame.draw.rect(display, black, [150, 150, 100, 20])
    pygame.display.flip()

