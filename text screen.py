import pygame
pygame.init()

X = 400
Y = 400
#colors

white = [255,255,255]
black = [0, 0, 0]
blue = (90,90,250)
red = (255,15,15)
#setup screen
display = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Text on screen')
running = True

font = pygame.font.Font(None, 24)

while running:
    display.fill(black)
    
    Text = font.render("Awesome Game!", True, white)
    display.blit(Text, [100, 200])
    pygame.display.flip()
