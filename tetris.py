import pygame

import sys

from settings import Settings

from cube import Cube

from bullet import Bullet

from alien import Alien


class Tetris:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # или три следущие строки

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('Tetris')

        self.cube = Cube(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            self.cube.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom >= self.settings.screen_height:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        """Обработка нажатия клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.cube.moving_right = True
            print(event)
        elif event.key == pygame.K_LEFT:
            self.cube.moving_left = True
            print(event)
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.cube.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.cube.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Обновление изображения на экране"""
        self.screen.fill(self.settings.bg_color)
        self.cube.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _create_fleet(self):
        """Создание флота"""
        # Создание первого ряда
        alien = Alien(self)
        alien_width = alien.rect.width
        available_spase_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_spase_x // (2 * alien_width)
        for alien_number in range(number_aliens_x):
            self._creat_alien(alien_number)

    def _creat_alien(self, alien_number):

        # создание пришельца в размещение в ряду
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)


if __name__ == '__main__':
    te = Tetris()
    te.run_game()
