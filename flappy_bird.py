import pygame
import sys
import random

# Pygameの初期化
pygame.init()

# ゲーム画面の設定
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 鳥の設定
bird_x = WINDOW_WIDTH // 3
bird_y = WINDOW_HEIGHT // 2
bird_velocity = 0
GRAVITY = 0.5
FLAP_STRENGTH = -10
bird_size = 30

# ゲームループ
clock = pygame.time.Clock()

while True:
    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = FLAP_STRENGTH

    # 鳥の移動
    bird_velocity += GRAVITY
    bird_y += bird_velocity

    # 画面の描画
    screen.fill(WHITE)
    
    # 鳥の描画
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), bird_size)
    
    # 画面の更新
    pygame.display.flip()
    
    # FPSの設定
    clock.tick(60)