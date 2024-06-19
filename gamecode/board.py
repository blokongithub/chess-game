import pygame
    
    
class gameboard:
    def __init__(self, screen):
        self.board = self.setupDataBoard()
        self.screen = screen
        
    def setupDataBoard(self):
        self.board = [["--" for i in range(8)] for i in range(8)]
        self.board[0] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        self.board[1] = ["bp" for i in range(8)]
        self.board[6] = ["wp" for i in range(8)]
        self.board[7] = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        
    def getpeice(self, x, y):
        return self.board[y][x]

    def highlight(self, x, y):
        pygame.draw.rect(self.screen, (255, 0, 0), (x*100, y*100, 100, 100))
        self.screen.blit(pygame.image.load("images/black_pawn.png"), (x*100, y*100))
        
    def pygameLoadImages(self):
        for i in range(8):
            bp = pygame.image.load("images/black_pawn.png")
            self.screen.blit(bp, (100*i, 100))
            wp = pygame.image.load("images/white_pawn.png")
            self.screen.blit(wp, (100*i, 600))
        br = pygame.image.load("images/black_rook.png")
        self.screen.blit(br, (0, 0)); self.screen.blit(br, (700, 0))
        wr = pygame.image.load("images/white_rook.png")
        self.screen.blit(wr, (0, 700)); self.screen.blit(wr, (700, 700))
        bn = pygame.image.load("images/black_knight.png")
        self.screen.blit(bn, (100, 0)); self.screen.blit(bn, (600, 0))
        wn = pygame.image.load("images/white_knight.png")
        self.screen.blit(wn, (100, 700)); self.screen.blit(wn, (600, 700))
        bb = pygame.image.load("images/black_bishop.png")
        self.screen.blit(bb, (200, 0)); self.screen.blit(bb, (500, 0))
        wb = pygame.image.load("images/white_bishop.png")
        self.screen.blit(wb, (200, 700)); self.screen.blit(wb, (500, 700))
        bq = pygame.image.load("images/black_queen.png")
        self.screen.blit(bq, (300, 0))
        wq = pygame.image.load("images/white_queen.png")
        self.screen.blit(wq, (300, 700))
        bk = pygame.image.load("images/black_king.png")
        self.screen.blit(bk, (400, 0))
        wk = pygame.image.load("images/white_king.png")
        self.screen.blit(wk, (400, 700))
        
    def pygameDrawBoard(self):
        c = [0, 0]
        green = True
        for i in range(64):
            if green == True:
                pygame.draw.rect(self.screen, (51, 204, 51), (c[0], c[1], 100, 100))
                green = False
            else:
                pygame.draw.rect(self.screen, (255, 255, 255), (c[0], c[1], 100, 100))
                green = True
            c[0] += 100
            if c[0] == 800:
                c[0] = 0
                c[1] += 100
                green = not green
        self.pygameLoadImages()
        pygame.display.flip()