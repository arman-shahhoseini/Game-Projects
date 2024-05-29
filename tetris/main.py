import pygame
from tetris import Tetris
from constants import WIDTH, HEIGHT, GRID_SIZE, BLACK, WHITE, RED

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    clock = pygame.time.Clock()
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)

    while True:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game.paused = not game.paused
            game.handle_event(event)

        game.update(clock.get_rawtime())
        game.draw(screen)

        if game.game_over:
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)
            if any(event.type == pygame.KEYDOWN for event in pygame.event.get()):
                game.reset()

        pygame.display.flip()
        clock.tick(60)

def draw_game_over(screen, x, y):
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (x, y))

if __name__ == "__main__":
    main()