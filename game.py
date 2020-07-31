from sys import hexversion
import pygame
pygame.init()

win  = pygame.display.set_mode((500, 500))

pygame.display.set_caption("test game")


screen_width = 500
screen_height = 500
x = 50
y = 50
height = 60
width = 40
vel = 5 

isJump = False
jumpCount = 10

# main loop
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x == 0:
            pass
        else:
            x -= vel
    if keys[pygame.K_RIGHT]:
        if x == (500 - width):
            pass
        else:
            x += vel
    if not isJump:
        if keys[pygame.K_UP]:
            if y == 0:
                pass
            else:
                y -= vel
        if keys[pygame.K_DOWN]:
            if y == (500 - height):
                pass
            else:
                y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount > 0:
                y -= jumpCount * 5 * 0.5
            else:
                y -= jumpCount * 5 * 0.5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
