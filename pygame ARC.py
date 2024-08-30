import pygame
pygame.init()


X = 500
Y = 500
WHITE = (255,255,255)
BLACK = (0, 0, 0)
blue = (90,90,250)
YELLOW = (255, 220, 15)
pi = 3.14

DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption('My Awesome Game')
running = True

while running:

    DISPLAY.fill(blue)
    pygame.draw.arc(DISPLAY, BLACK, [50, 150, 400, 150], pi, 2*pi, 5)
    pygame.draw.circle(DISPLAY, BLACK, (175, 150), 24)
    pygame.draw.circle(DISPLAY, BLACK, (325, 150), 25)
    pygame.draw.polygon(DISPLAY, WHITE, [[225, 250], [250, 150], [275, 250]])
    pygame.draw.arc(DISPLAY, YELLOW, [15, 10, 450, 400], pi, 3*pi, 5) 
    pygame.display.flip()
