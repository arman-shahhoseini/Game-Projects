import random
import pygame
from tetromino import Tetromino
from constants import SHAPES, COLORS, GRID_SIZE, WHITE

class Tetris:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.fall_time = 0
        self.fall_speed = 500  
        self.paused = False

    def new_piece(self):
        shape = random.choice(SHAPES)
        return Tetromino(self.width // 2, 0, shape, random.choice(COLORS))

    def valid_move(self, piece, x, y, rotation):
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
            for j, cell in enumerate(row):
                try:
                    if cell == 'O' and (self.grid[piece.y + i + y][piece.x + j + x] != 0):
                        return False
                except IndexError:
                    return False
        return True

    def clear_lines(self):
        lines_cleared = 0
        for i, row in enumerate(self.grid[:-1]):
            if all(cell != 0 for cell in row):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)])
        self.score += lines_cleared * 100
        return lines_cleared

    def lock_piece(self, piece):
        for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.grid[piece.y + i][piece.x + j] = piece.color
        lines_cleared = self.clear_lines()
        self.current_piece = self.new_piece()
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True
        return lines_cleared

    def update(self, delta_time):
        if not self.game_over and not self.paused:
            self.fall_time += delta_time
            if self.fall_time >= self.fall_speed:
                if self.valid_move(self.current_piece, 0, 1, 0):
                    self.current_piece.y += 1
                else:
                    self.lock_piece(self.current_piece)
                self.fall_time = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if self.valid_move(self.current_piece, -1, 0, 0):
                    self.current_piece.x -= 1
            elif event.key == pygame.K_RIGHT:
                if self.valid_move(self.current_piece, 1, 0, 0):
                    self.current_piece.x += 1
            elif event.key == pygame.K_DOWN:
                if self.valid_move(self.current_piece, 0, 1, 0):
                    self.current_piece.y += 1
            elif event.key == pygame.K_UP:
                if self.valid_move(self.current_piece, 0, 0, 1):
                    self.current_piece.rotation += 1
            elif event.key == pygame.K_SPACE:
                while self.valid_move(self.current_piece, 0, 1, 0):
                    self.current_piece.y += 1
                self.lock_piece(self.current_piece)
            elif event.key == pygame.K_p:
                self.paused = not self.paused

    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        if self.current_piece:
            for i, row in enumerate(self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':
                        pygame.draw.rect(screen, self.current_piece.color, ((self.current_piece.x + j) * GRID_SIZE, (self.current_piece.y + i) * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        draw_score(screen, self.score, 10, 10)

    def reset(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0
        self.fall_time = 0

def draw_score(screen, score, x, y):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (x, y))