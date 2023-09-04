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
#ตั้งค่าคุณสมบัติ paddle 
paddle_rect = paddle.get_rect()
paddle_rect.centerx = SCREEN_W // 2
paddle_rect.centery = SCREEN_H // 2

running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        print("Up Arrow")
    if keys[pygame.K_DOWN]:
        print("Down Arrow")
    if keys[pygame.K_LEFT]:
        print("Left Arrow")
    if keys[pygame.K_RIGHT]:
        print("Right Arrow")

    #แสดงภาพ
    screen.fill(WHITE)
    screen.blit(paddle,paddle_rect)
    pygame.display.update()
pygame.quit()