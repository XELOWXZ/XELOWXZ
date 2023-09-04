import pygame

#ประกาศใช้งาน pygame
pygame.init()
#หัวข้อ
pygame.display.set_caption("เกมอะไรว่ะเนี่ยย???")
#ตั่งค่าสี
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
#ขนาดหน้าจอ 
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอเกม 
screen.fill(WHITE)
running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()