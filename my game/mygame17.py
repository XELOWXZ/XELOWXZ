import pygame
import random
import winsound

pygame.init()
pygame.display.set_caption("BALL OF KING")
# ตั้งค่าสี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 51)
PURPLE = (9, 102, 102)
# ความเร็วการเคลื่อนที่
SPEED = 10
BALL_SPEED = 5
# FPS
FPS = 60
clock = pygame.time.Clock()

# ขนาดหน้าจอ
SCREEN_W = 576
SCREEN_H = 1024
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen.fill(BLACK)

# เพิ่มเสียง
pygame.mixer.init()
collision_sound = pygame.mixer.Sound('Sounds/เอฟเฟกต์.mp3')
collision_sound.set_volume(10000)
background_music = pygame.mixer.Sound('Sounds/Sound2.mp3')
background_music.set_volume(0.5)
background_music.play(-1)

# โหลดภาพ
paddle = pygame.image.load("Image/paddle.png")
paddle = pygame.transform.scale(paddle, (120, 30))

# paddle object
paddle_rect = paddle.get_rect()
paddle_rect.centerx = SCREEN_W // 1.1
paddle_rect.centery = SCREEN_H // 1.1

# ball object
ball = pygame.image.load("Image/ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ball_rect = ball.get_rect()
ball_rect.x = random.randint(0, SCREEN_W - 32)
ball_rect.y = 0

# Bg
bg = pygame.image.load("Image/BG.png")
bg = pygame.transform.scale(bg, (576, 1024))
bg_rect = bg.get_rect()
bg_rect.centerx = SCREEN_W // 2
bg_rect.centery = SCREEN_H // 2

# score system
score = 0
font = pygame.font.Font("Font/04B_30__.TTF", 20)
score_text = font.render("Score : " + str(score), True, PURPLE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # การชน
    if ball_rect.colliderect(paddle_rect):
        score += 10
        score_text = font.render("Score : " + str(score), True, YELLOW)
        ball_rect.x = random.randint(0, SCREEN_W - 32)
        ball_rect.y = 0
        BALL_SPEED += 0.5  # เพิ่มความเร็วของลูกบอลเมื่อคะแนนเพิ่มขึ้น
        collision_sound.play() 

    # รับค่าจากผู้เล่น
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_rect.left > 0:
        paddle_rect.x -= SPEED
    if keys[pygame.K_RIGHT] and paddle_rect.right < SCREEN_W:
        paddle_rect.x += SPEED

    # การเคลื่อนที่ลูกบอล
    if ball_rect.y < SCREEN_H:
        ball_rect.y += BALL_SPEED
    else:
        # ทะลุหน้าจอเกม
        ball_rect.x = random.randint(0, SCREEN_W - 32)
        ball_rect.y = 0

    # แสดงภาพ
    screen.blit(bg, bg_rect)
    screen.blit(paddle, paddle_rect)
    screen.blit(ball, ball_rect)
    screen.blit(score_text, score_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
