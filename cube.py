import pygame.image


class Cube():
    def __init__(self, te_game):
        """ Инициализирует форму и задает ее начальное положение"""
        self.screen = te_game.screen
        self.screen_rect = te_game.screen.get_rect()

        """Загружает изображение и создает прямоугольник"""
        self.image = pygame.image.load('cube_four.bmp')
        self.rect = self.image.get_rect()
        """Кождый новый корабль появляется у нижнего края экрана"""
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
