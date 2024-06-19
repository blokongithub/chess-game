import pygame
import gamecode.board as board

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
timer = pygame.time.Clock()
fps = 60
c = [0, 0]
green = True
board.pygameDrawBoard(screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False