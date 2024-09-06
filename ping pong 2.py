import pygame

pygame.init()

X = 400
Y = 400
navy_BLUE = (0, 0, 128)
white = (255, 255, 255)
orange = (255, 165, 0)
BLACK = (0, 0, 0)


DISPLAY = pygame.display.set_mode([X, Y])
pygame.display.set_caption('My Ping Pong game')

paddel1 = 250
paddel2 = 250

x_pos = 100
y_pos = 100

x_movment = 5
y_movment = 2

running = True
clock = pygame.time.Clock()

while running:
    DISPLAY.fill(BLACK)

    pygame.draw.rect(DISPLAY, navy_BLUE, (0, 0, 400, 25))
    pygame.draw.rect(DISPLAY, navy_BLUE, (0, 375, 400, 25))

    pygame.draw.rect(DISPLAY, orange, (15, paddel1, 10, 25))
    pygame.draw.rect(DISPLAY, orange, (285, paddel2, 10, 25))

    pygame.draw.rect(DISPLAY, white, (x_pos, y_pos, 5, 5))

    x_pos = x_pos + x_movment
    y_pos = y_pos + y_movment

    if x_pos == 25 and paddel1 < y_pos + 2.5 < paddel1 +25:
        x_movment = x_movment * -1

    if y_pos < 25 or y_pos > 375:
        y_movment = y_movment * -1
    

    clock.tick(15)


    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and paddel1 > 25:
                paddel1 = paddel1 -20
            elif event.key == pygame.K_s and paddel1 < 350: 
                paddel1 = paddel1 + 20
            elif event.key == pygame.K_u and paddel2 > 25:
                paddel2 = paddel2 - 20
            elif event.key == pygame.K_j and paddel2 < 350:
                paddel2 = paddel2 + 20

          
    pygame.display.flip()

pygame.quit()