import pygame
pygame.init()
pygame.display.set_caption("เกมอะไรว่ะเนี่ยย???")
#ตั้งค่าสี
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
#ขนาดหน้าจอ
SCREEN_W = 800 
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
#แสดงหน้าจอ
screen.fill(WHITE)
screen_rect = screen.get_rect()
print(screen_rect.width)
print(screen_rect.height)
print(screen_rect.size)
print(screen_rect.centerx) # screen_w // 2 = 300
print(screen_rect.centery) # screen_h // 2 = 300
print(screen_rect.center)
running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    pygame.display.update()
pygame.quit()