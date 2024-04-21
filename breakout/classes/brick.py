import pygame

class Brick:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def hit(self, bx, by, bsize):
        if bx + bsize > self.x and bx - bsize < self.x + self.width and by + bsize > self.y and by - bsize < self.y + self.height:
            return True
        return False
