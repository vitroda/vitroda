import pygame
import time
import random

# Configurações iniciais
pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Inicialização da cobra
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_speed = 15

# Comida
food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
food_spawn = True

# Direção
direction = 'RIGHT'
change_to = direction

# Função para exibir mensagem na tela
def show_text(text, color, x, y):
    font = pygame.font.Font(None, 30)
    score = font.render(text, True, color)
    win.blit(score, (x, y))

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validar a mudança de direção
    if change_to == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'

    # Mover a cobra
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Comida
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.insert(0, list(snake_pos))
        if len(snake_body) > 1:
            snake_body.pop()
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        food_spawn = True
    win.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(win, GREEN, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    # Colisão com as bordas
    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10:
        show_text("Game Over!", (255, 0, 0), WIDTH//4, HEIGHT//2)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
    if snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        show_text("Game Over!", (255, 0, 0), WIDTH//4, HEIGHT//2)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        quit()
    # Colisão com o próprio corpo
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            show_text("Game Over!", (255, 0, 0), WIDTH//4, HEIGHT//2)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            quit()
    pygame.display.update()
    pygame.time.Clock().tick(snake_speed)
