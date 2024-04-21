import pygame

class Paddle:
    def __init__(self, screen, width, y, screen_width):
        self.screen = screen
        self.width = width
        self.height = 20
        self.y = y
        self.x = (screen_width - width) / 2
        self.speed = 25

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 255), (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        elif direction == "right":
            self.x += self.speed
            if self.x + self.width > self.screen.get_width():
                self.x = self.screen.get_width() - self.width
