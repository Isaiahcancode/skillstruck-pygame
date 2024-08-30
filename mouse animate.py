import pygame
pygame.init()
X = 500
Y = 500
yellow = (240,255,15)
navyblue = (30, 0, 180)
display = pygame.display.set_mode([X, Y])

running = True
clock = pygame.time.Clock()

pygame.mouse.set_visible(0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = false

            
    pos = pygame.mouse.get_pos( )
    x = pos[0]
    y = pos[1]
    display.fill(yellow)
    pygame.draw.rect(display, navyblue,[ 150, 200, 200, 100])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()