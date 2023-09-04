import pygame
import random

pygame.init()
pygame.display.set_caption("BALL OF KING")
#ตั้งค่าสี
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
YELLOW = (255,255,51)
#ความเร็วการเคลื่อนที่
SPEED = 8
BALL_SPEED=7
#FPS
FPS = 60 
clock = pygame.time.Clock()

#ขนาดหน้าจอ
SCREEN_W = 900
SCREEN_H = 1050
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
screen.fill(BLACK)

#โหลดภาพ
paddle=pygame.image.load("Image/paddle.png")
paddle=pygame.transform.scale(paddle,(120,30))

#paddle object
paddle_rect = paddle.get_rect()
paddle_rect.centerx = SCREEN_W // 1.1
paddle_rect.centery = SCREEN_H // 1.1

#ball object
ball=pygame.image.load("Image/ball.png")
ball = pygame.transform.scale(ball,(50,50))
ball_rect = ball.get_rect()
ball_rect.x = random.randint(0,SCREEN_W-32)
ball_rect.y = 0

#score system
score = 0
font = pygame.font.Font("Font/Coiny.ttf",30)
score_text = font.render("Score : "+str(score),True,YELLOW) 
score_rect = score_text.get_rect()
score_rect.topleft=(10,10)
running=True 
while running : 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    #การชน
    if paddle_rect.colliderect(ball_rect):
        score+=10  
        score_text = font.render("Score : "+str(score),True,YELLOW)  
        ball_rect.x = random.randint(0,SCREEN_W-32)
        ball_rect.y = 0

    #รับค่าจากผู้เล่น
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left>0: 
        paddle_rect.x-=SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.right<SCREEN_W: 
        paddle_rect.x+=SPEED
    #การเคลื่อนที่ลูกบอล
    if ball_rect.y < SCREEN_H:
        ball_rect.y+=BALL_SPEED
    else:
        #ทะลุหน้าจอเกม
        ball_rect.x = random.randint(0,SCREEN_W-32)
        ball_rect.y = 0
    #แสดงภาพ
    screen.fill(BLACK) 
    screen.blit(paddle,paddle_rect)
    screen.blit(ball,ball_rect)
    screen.blit(score_text,score_rect)
    #แสดงขอบเขตวัตถุ
    #pygame.draw.rect(screen,GREEN,paddle_rect,2)
    #pygame.draw.rect(screen,GREEN,ball_rect,2)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()