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

movement_x = 2
movement_y = 2

while running:

    display.fill(white)
    pygame.draw.rect(display, black, [rect_x, rect_y, 100, 59])


    rect_x = rect_x + movement_x
    rect_y = rect_y + movement_y

    if rect_x > 400 or rect_x < 0:
        movement_x = movement_x * -1
    if rect_y > 400 or rect_y < 0:
        movement_y = movement_y * -1
    clock.tick(60)

    pygame.display.flip()

