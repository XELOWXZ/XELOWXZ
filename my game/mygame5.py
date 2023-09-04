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
custom_font = pygame.font.Font("Font/Coiny.ttf",20)
title_text = custom_font.render("HELLO MY GAME",True,BLACK)


running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    screen.blit(title_text,(80,100))

    pygame.display.update()
pygame.quit()