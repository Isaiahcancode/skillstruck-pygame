import pygame

pygame.init()

X = 500
Y = 500
BLUE = (90, 90, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

cir_x = 150
cir_y = 150

DISPLAY = pygame.display.set_mode([X, Y])
running = True
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cir_x = rect_x - 20
            elif event.key == pygame.K_RIGHT:
                cir_x = rect_x + 20
            elif event.key == pygame.K_UP:
                cir_y = rect_y - 20
            elif event.key == pygame.K_DOWN:
                cir_y = rect_y + 20
          

    DISPLAY.fill(BLUE)
    pygame.draw.circle(DISPLAY, WHITE, (cir_x, cir_y), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()