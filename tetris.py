import pygame

import sys

from settings import Settings

from cube import Cube


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Tetris')

        self.cube = Cube(self)

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обработка нажатия клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновление изображения на экране"""
        self.screen.fill(self.settings.bg_color)
        self.cube.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    te = Tetris()
    te.run_game()
