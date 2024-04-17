import pygame

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Red ball moves")
clock = pygame.time.Clock()
FPS = 30
x = 400
y = 400
pos = (x , y)
done = False
color_red = (255,0,0)
while not done:
    screen.fill((255,255,255))
    pygame.draw.circle(screen, color_red , pos, 25)
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 25:
            x -= 20
    if keys[pygame.K_RIGHT] and x < 775:
            x += 20
    if keys[pygame.K_DOWN] and y < 775:
            y += 20
    if keys[pygame.K_UP] and y > 25:
            y -= 20
    pos = (x , y)
    clock.tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
        
    pygame.display.flip()
    

        

