import pygame.image


class Cube():
    def __init__(self, te_game):
        """ Инициализирует форму и задает ее начальное положение"""
        self.screen = te_game.screen
        self.settings = te_game.settings
        self.screen_rect = te_game.screen.get_rect()

        """Загружает изображение и создает прямоугольник"""
        self.image = pygame.image.load('cube_four.bmp')
        self.rect = self.image.get_rect()
        """Кождый новый корабль появляется у нижнего края экрана"""
        self.rect.midtop = self.screen_rect.midtop

        # Сохранение вещественной координаты центра коробля
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позиции коробля с учетом флага"""
        if self.moving_right:
            self.x += self.settings.cobe_speed

        if self.moving_left:
            self.x -= self.settings.cobe_speed

        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
