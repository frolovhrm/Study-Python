import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Клас для управления снарядами, выпущеными кораблем"""

    def __init__(self, te_game):
        super().__init__()
        self.screen = te_game.screen
        self.settings = te_game.settings
        self.color = self.settings.bullet_color

        # создание позиции снераяда
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = te_game.cube.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # Перемещает снаряд по экрану
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
