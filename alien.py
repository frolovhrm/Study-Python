import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс представляющий одного пришельца"""

    def __init__(self, te_game):
        """Инициализирует пришельца и создает его начальную позицию"""
        super().__init__()
        self.screen = te_game.screen

        #Загрузка пришельца и назначение rect
        self.image = pygame.image.load('cube_four.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции
        self.x = float(self.rect.x)

