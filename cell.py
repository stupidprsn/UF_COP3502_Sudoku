import pygame
class Cell:
    def __init__(self, row, col, screen, value = 0):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.place_rect = False
        self.sketched_value = 0
    def set_cell_value(self, value):
        self.value = value
    def set_sketched_value(self, value):
        self.sketched_value = value
    def draw(self):
        pygame.draw.line(self.screen, "black", (self.col * 64, self.row * 64), ((self.col + 1) * 64, self.row * 64))
        pygame.draw.line(self.screen, "black", (self.col * 64, self.row * 64), (self.col * 64, (self.row + 1) * 64))
        pygame.draw.line(self.screen, "black", (self.col * 64, (self.row + 1) * 64), ((self.col + 1) * 64, (self.row + 1) * 64))
        pygame.draw.line(self.screen, "black", ((self.col + 1) * 64, self.row * 64), ((self.col + 1) * 64, (self.row + 1) * 64))
        if self.value != 0:
            num_rect = self.font.render(str(self.value), 0, (0, 0, 0)).get_rect(center=(self.col * 64 + 64 / 2, self.row * 64 + 64 / 2))
            self.screen.blit(self.font.render(str(self.value), 0, (0, 0, 0)), num_rect)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if abs(event.pos[0] - (self.col * 64 + 64 / 2)) < 32 and abs(event.pos[1] - (self.row * 64 + 64 / 2)) < 32:
                    if self.place_rect:
                        self.place_rect = False
                    else:
                        self.place_rect = True
            if self.place_rect:
                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.row * 64, self.col * 64, (self.row + 1) * 64, (self.col + 1) * 64), 2)
