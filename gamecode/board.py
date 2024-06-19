import pygame

def pygameDrawBoard(screen):
    c = [0, 0]
    green = True
    for i in range(64):
        if green == True:
            pygame.draw.rect(screen, (51, 204, 51), (c[0], c[1], 100, 100))
            green = False
        else:
            pygame.draw.rect(screen, (255, 255, 255), (c[0], c[1], 100, 100))
            green = True
        c[0] += 100
        if c[0] == 800:
            c[0] = 0
            c[1] += 100
            green = not green
    for i in range(8):
        bp = pygame.image.load("images/black_pawn.png")
        screen.blit(bp, (100*i, 100))
        wp = pygame.image.load("images/white_pawn.png")
        screen.blit(wp, (100*i, 600))
    br = pygame.image.load("images/black_rook.png")
    screen.blit(br, (0, 0)); screen.blit(br, (700, 0))
    wr = pygame.image.load("images/white_rook.png")
    screen.blit(wr, (0, 700)); screen.blit(wr, (700, 700))
    bn = pygame.image.load("images/black_knight.png")
    screen.blit(bn, (100, 0)); screen.blit(bn, (600, 0))
    wn = pygame.image.load("images/white_knight.png")
    screen.blit(wn, (100, 700)); screen.blit(wn, (600, 700))
    bb = pygame.image.load("images/black_bishop.png")
    screen.blit(bb, (200, 0)); screen.blit(bb, (500, 0))
    wb = pygame.image.load("images/white_bishop.png")
    screen.blit(wb, (200, 700)); screen.blit(wb, (500, 700))
    bq = pygame.image.load("images/black_queen.png")
    screen.blit(bq, (300, 0))
    wq = pygame.image.load("images/white_queen.png")
    screen.blit(wq, (300, 700))
    bk = pygame.image.load("images/black_king.png")
    screen.blit(bk, (400, 0))
    wk = pygame.image.load("images/white_king.png")
    screen.blit(wk, (400, 700))
    pygame.display.flip()

def setupDataBoard():
    board = [["--" for i in range(8)] for i in range(8)]
    board[0] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
    board[1] = ["bp" for i in range(8)]
    board[6] = ["wp" for i in range(8)]
    board[7] = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    return board
print(setupDataBoard())