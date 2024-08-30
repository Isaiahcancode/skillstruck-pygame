import pygame
pygame.init()

X = 400
Y = 400
#colors

white = (255,255,255)
black = [0, 0, 0]
blue = (0,63,163)
red = (255,15,15)
backround = (0,52,92)
#setup screen
display = pygame.display.set_mode([X, Y])
pygame.display.set_caption('Timer counting up')
running = True

clock = pygame.time.Clock()

font = pygame.font.Font(None, 24)
total_seconds = 0

frame_count = 0
start_time = 80
while running:
    display.fill(blue)

    total_seconds = start_time - (frame_count // 60)



    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds - (minutes * 60)
    output_string = "Time Left: " + str(minutes) + ":" + str(seconds)

    Text = font.render(output_string, True, white)
    display.blit(Text, [100, 200])

    

    frame_count += 1

    clock.tick(60)

    
    pygame.display.flip()
