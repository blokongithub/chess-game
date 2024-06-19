import pygame
import gamecode.board as board

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
timer = pygame.time.Clock()
fps = 60
chessboard = board.gameboard(screen)
chessboard.pygameDrawBoard()
chessboard.highlight(0, 0)
pygame.display.flip()

while running:
    print(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False