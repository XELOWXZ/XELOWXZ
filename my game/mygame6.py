import pygame
pygame.init()
pygame.display.set_caption("เกมอะไรว่ะเนี่ยย???")
#ตั้งค่าสี
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
#ขนาดหน้าจอ
SCREEN_W = 600  
SCREEN_H = 300
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
screen.fill(WHITE)
#โหลดภาพ
paddle=pygame.image.load("Image/paddle.png")
#ปรับขนาดภาพ
paddle=pygame.transform.scale(paddle,(120,30))

running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #แสดงภาพ
    screen.blit(paddle,(100,100))
    pygame.display.update()
pygame.quit()