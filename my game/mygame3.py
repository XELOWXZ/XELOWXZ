import pygame
pygame.init()
pygame.display.set_caption("เกมอะไรว่ะเนี่ยย???")
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
screen.fill(WHITE)
#วาดรูป
pygame.draw.line(screen, BLACK, (0,0),(100, 100),5)
pygame.draw.rect(screen,RED,(170,20,100,50))
pygame.draw.circle(screen,BLACK,(400,80),50,3)
running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()