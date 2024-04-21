import pygame

class Ball:
    def __init__(self, screen, screen_width, screen_height, size):
        self.screen = screen
        self.size = size
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.vx = 7
        self.vy = -7

    def draw(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (int(self.x), int(self.y)), self.size)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x <= 0 or self.x >= self.screen.get_width():
            self.vx = -self.vx
        if self.y <= 0:
            self.vy = -self.vy
        if self.y >= self.screen.get_height():
            return True
        return False

    def check_collision(self, paddle, bricks):
        hit_count = 0
        if self.y + self.size >= paddle.y and self.x >= paddle.x and self.x <= paddle.x + paddle.width:
            self.vy = -self.vy
            self.y = paddle.y - self.size

        for brick in bricks:
            if brick.hit(self.x, self.y, self.size):
                self.vy = -self.vy
                hit_count += 1

        return hit_count
