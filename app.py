import pygame
import random
import time
import os

pygame.init()

width = 800
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo Snake - Tipografia Ajustada")

# Cores
WHITE = (255, 255, 255)
RED = (220, 20, 60)
GREEN = (50, 205, 50)
BLACK = (20, 20, 20)
YELLOW = (255, 215, 0)

snake_block = 20
snake_speed = 15

clock = pygame.time.Clock()

# Carregar fonte personalizada ou usar fallback
try:
    game_font = pygame.font.Font("PressStart2P-Regular.ttf", 40)
    small_game_font = pygame.font.Font("PressStart2P-Regular.ttf", 20)
except:
    game_font = pygame.font.SysFont("monospace", 40, bold=True)
    small_game_font = pygame.font.SysFont("monospace", 20, bold=True)

# Função para exibir texto com sombra e contorno
def message(msg, color, pos, font_size=game_font, shadow=True, outline=False):
    if shadow:
        shadow_text = font_size.render(msg, True, BLACK)
        window.blit(shadow_text, (pos[0] + 3, pos[1] + 3))
    if outline:
        for offset in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            outline_text = font_size.render(msg, True, BLACK)
            window.blit(outline_text, (pos[0] + offset[0], pos[1] + offset[1]))
    mesg = font_size.render(msg, True, color)
    window.blit(mesg, pos)

# Função para desenhar a cobrinha
def our_snake(snake_block, snake_list):
    for i, x in enumerate(snake_list):
        shade = GREEN if i == len(snake_list) - 1 else (max(30, 50 - i * 5), max(150, 205 - i * 10), 50)
        pygame.draw.rect(window, shade, [x[0], x[1], snake_block - 2, snake_block - 2], border_radius=5)

# Função para desenhar a comida
def draw_food(x, y):
    pygame.draw.circle(window, RED, (int(x + snake_block / 2), int(y + snake_block / 2)), snake_block // 2 - 2)

# Funções de ranking
def load_highscores():
    if not os.path.exists("highscores.txt"):
        return [0, 0, 0, 0, 0]
    with open("highscores.txt", "r") as file:
        scores = [int(line.strip()) for line in file.readlines()]
        return scores[:5] if len(scores) >= 5 else scores + [0] * (5 - len(scores))

def save_highscores(scores):
    scores.sort(reverse=True)
    with open("highscores.txt", "w") as file:
        for score in scores[:5]:
            file.write(f"{score}\n")

def show_highscores(scores):
    ranking_title_y = height / 4 + 80
    message("Ranking:", WHITE, [width / 3, ranking_title_y - 40])

    for i, score in enumerate(scores[:5], 1):
        y_pos = ranking_title_y + i * 35
        message(f"{i}. {score}", YELLOW, [width / 3, y_pos], small_game_font)

# Loop do jogo
def game_loop():
    game_over = False
    game_close = False
    intro = True

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    score = 0

    foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    current_speed = snake_speed
    highscores = load_highscores()

    while intro:
        window.fill(BLACK)
        message("Bem-vindo ao Snake!", WHITE, [width / 4 - 50, height / 3], shadow=True, outline=True)
        message("Pressione qualquer tecla", YELLOW, [width / 6, height / 2], small_game_font)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                intro = False

    while not game_over:
        while game_close:
            window.fill(BLACK)
            message(f"Sua pontuação: {score}", WHITE, [width / 3 - 50, height / 4], shadow=True, outline=True)
            show_highscores(highscores)
            message("Q-Sair  C-Jogar novamente", YELLOW, [width / 6, height / 2 + 200], small_game_font)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change != -snake_block:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            highscores.append(score)
            save_highscores(highscores)
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(BLACK)

        draw_food(foodx, foody)

        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                highscores.append(score)
                save_highscores(highscores)
                game_close = True

        our_snake(snake_block, snake_list)
        # Mensagem de pontuação dinâmica (evita sobreposição)
        label = "Pontuação:"
        label_surface = game_font.render(label, True, WHITE)
        label_width = label_surface.get_width()

        message(label, WHITE, [10, 10], shadow=True, outline=True)
        message(str(score), WHITE, [10 + label_width + 20, 10], shadow=True, outline=True)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1
            score += 10
            if score % 50 == 0:
                current_speed += 2

        clock.tick(current_speed)

    pygame.quit()
    quit()

game_loop()