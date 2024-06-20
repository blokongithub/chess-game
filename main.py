import pygame
import gamecode.board as board
import math

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
timer = pygame.time.Clock()
fps = 60
chessboard = board.gameboard(screen)
chessboard.pygameDrawBoard()
pygame.display.flip()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = [math.floor(pos[0]/100), math.floor(pos[1]/100)]
            print(pos)
            chessboard.highlight(pos)
