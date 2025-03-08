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
SKY_BLUE = (135, 206, 235)  # 空色
GREEN = (34, 139, 34)       # 深い緑（地面用）
BLUE = (0, 0, 255)

# 地面の設定
GROUND_HEIGHT = 100

# 鳥の設定
bird_x = WINDOW_WIDTH // 3
bird_y = WINDOW_HEIGHT // 2
bird_velocity = 0
GRAVITY = 0.5
FLAP_STRENGTH = -10
bird_size = 30

# 雲の設定
clouds = []
for _ in range(3):
    cloud = {
        'x': random.randint(0, WINDOW_WIDTH),
        'y': random.randint(50, WINDOW_HEIGHT//2),
        'width': random.randint(60, 120),
        'speed': random.uniform(0.5, 1.5)
    }
    clouds.append(cloud)

# ゲームループ
clock = pygame.time.Clock()

def draw_cloud(x, y, width):
    """雲を描画する関数"""
    height = width // 2
    pygame.draw.ellipse(screen, WHITE, (x, y, width, height))

def update_clouds():
    """雲を更新する関数"""
    for cloud in clouds:
        # 雲を左に移動
        cloud['x'] -= cloud['speed']
        # 画面外に出たら右端に戻す
        if cloud['x'] + cloud['width'] < 0:
            cloud['x'] = WINDOW_WIDTH
            cloud['y'] = random.randint(50, WINDOW_HEIGHT//2)

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

    # 地面との衝突判定
    if bird_y + bird_size > WINDOW_HEIGHT - GROUND_HEIGHT:
        bird_y = WINDOW_HEIGHT - GROUND_HEIGHT - bird_size
        bird_velocity = 0

    # 画面の描画
    # 背景（空）
    screen.fill(SKY_BLUE)
    
    # 雲の更新と描画
    update_clouds()
    for cloud in clouds:
        draw_cloud(cloud['x'], cloud['y'], cloud['width'])
    
    # 地面の描画
    pygame.draw.rect(screen, GREEN, (0, WINDOW_HEIGHT - GROUND_HEIGHT, WINDOW_WIDTH, GROUND_HEIGHT))
    
    # 装飾（地面の模様）
    for i in range(0, WINDOW_WIDTH, 30):
        pygame.draw.line(screen, (45, 160, 45), 
                        (i, WINDOW_HEIGHT - GROUND_HEIGHT),
                        (i + 15, WINDOW_HEIGHT - GROUND_HEIGHT + 10),
                        3)
    
    # 鳥の描画
    pygame.draw.circle(screen, BLUE, (bird_x, int(bird_y)), bird_size)
    
    # 画面の更新
    pygame.display.flip()
    
    # FPSの設定
    clock.tick(60)