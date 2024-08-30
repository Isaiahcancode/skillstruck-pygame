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
clock = pygame.time.Clock()

rect_x = 150
rect_y = 150

while running:

    display.fill(white)
    pygame.draw.rect(display, black, [rect_x, rect_y, 200, 20])
    rect_x = rect_x + 1
    rect_y = rect_y - 2


    
    clock.tick(60)

    pygame.display.flip()

