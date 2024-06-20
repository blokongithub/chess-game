import pygame

class gameboard:
    def __init__(self, screen):
        self.board = None
        self.setupDataBoard()
        self.screen = screen
        self.piece_images = self.load_piece_images()
        self.selectedsquare = [0, 0]
        self.movesoptions = [[3, 5], [5, 6]]
        self.selectedpeice = None
        self.blackpieces = ["bp", "bN", "bR", "bB", "bQ", "bK"]
        self.whitepieces = ["wp", "wN", "wR", "wB", "wQ", "wK"]
    def setupDataBoard(self):
        self.board = [["--" for _ in range(8)] for _ in range(8)]
        self.board[0] = ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
        self.board[1] = ["bp" for _ in range(8)]
        self.board[6] = ["wR" for _ in range(8)]
        self.board[7] = ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]

    def get_piece(self, x, y):
        return self.board[y][x]

    def pygameDrawBoard(self):
        c = [0, 0]
        green = True
        for i in range(64):
            if green:
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

    def load_piece_images(self):
        pieces = ["bR", "wR", "bN", "wN", "bB", "wB", "bQ", "wQ", "bK", "wK", "bp", "wp"]
        images = {}
        for piece in pieces:
            try:
                images[piece] = pygame.image.load(f"images/{piece}.png")
            except pygame.error as e:
                print(f"Error loading image for {piece}: {e}")
                images[piece] = None
        return images

    def pygameLoadImages(self):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece != "--" and self.piece_images[piece]:
                    self.screen.blit(self.piece_images[piece], (x * 100, y * 100))

    def highlight(self, coords):
        if self.selectedsquare:
            prev_x, prev_y = self.selectedsquare
            prev_color = (51, 204, 51) if (prev_x + prev_y) % 2 == 0 else (255, 255, 255)
            pygame.draw.rect(self.screen, prev_color, (prev_x * 100, prev_y * 100, 100, 100), 3)

        if self.board[coords[1]][coords[0]] != "--":
            self.selectedsquare = coords
            self.selectedpeice = [coords[0], coords[1], self.board[coords[1]][coords[0]]]
            match self.selectedpeice[2]:
                case "wp":
                    self.getpawnoptions()
                case "bp":
                    self.getpawnoptions()
                case "wR":
                    self.getrookoptions()
                case "bR":
                    self.getrookoptions()
            pygame.draw.rect(self.screen, (255, 0, 0), (coords[0] * 100, coords[1] * 100, 100, 100), 3)
            pygame.display.flip()

    def drawoptions(self):
        for i in self.movesoptions:
            pygame.draw.circle(self.screen, (0, 0, 255), (i[0] * 100 + 50, i[1] * 100 + 50), 15)

    def getpawnoptions(self):
        self.movesoptions = []
        x, y = self.selectedpeice[0], self.selectedpeice[1]
        if self.selectedpeice[2] == "wp":

            # Forward moves
            if y > 0 and self.board[y - 1][x] == "--":
                self.movesoptions.append([x, y - 1])
                if y == 6 and self.board[y - 2][x] == "--":
                    self.movesoptions.append([x, y - 2])

            # Capture moves
            if x < 7 and y > 0 and self.board[y - 1][x + 1] in self.blackpieces:
                self.movesoptions.append([x + 1, y - 1])
            if x > 0 and y > 0 and self.board[y - 1][x - 1] in self.blackpieces:
                self.movesoptions.append([x - 1, y - 1])
        elif self.selectedpeice[2] == "bp":
            if y > 0 and self.board[y + 1][x] == "--":
                self.movesoptions.append([x, y + 1])
                if y == 1 and self.board[y + 2][x] == "--":
                    self.movesoptions.append([x, y + 2])

            # Capture moves
            if x < 7 and y > 0 and self.board[y + 1][x + 1] in self.whitepieces:
                self.movesoptions.append([x + 1, y + 1])
            if x > 0 and y > 0 and self.board[y + 1][x - 1] in self.whitepieces:
                self.movesoptions.append([x - 1, y + 1])
        self.pygameDrawBoard()
        self.drawoptions()

    def getrookoptions(self):
        self.movesoptions = []
        x, y = self.selectedpeice[0], self.selectedpeice[1]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction in directions:
            dx, dy = direction
            v, w = x + dx, y + dy
            while 0 <= v < 8 and 0 <= w < 8:
                if self.selectedpeice[2] == "wR":
                    if self.board[w][v] == "--":
                        self.movesoptions.append([v, w])
                    elif self.board[w][v] in self.blackpieces:
                        self.movesoptions.append([v, w])
                        break
                    else:
                        break
                elif self.selectedpeice[2] == "bR":
                    if self.board[w][v] == "--":
                        self.movesoptions.append([v, w])
                    elif self.board[w][v] in self.whitepieces:
                        self.movesoptions.append([v, w])
                        break
                    else:
                        break
                v += dx
                w += dy

        self.pygameDrawBoard()
        self.drawoptions()
        pygame.display.flip()