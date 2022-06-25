import pygame
import sys


class Tetris:
    def __init__(self):
        pygame.init()
        self.left = 10
        self.right = 10
        self.left_flag = False
        self.right_flag = False

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()
            if self.left_flag == True or self.left_flag == True:
                print(f'{self.left} - {self.right}')
                self.left_flag = False
                self.right_flag = False

    def _check_events(self):
        """Обработка нажатия клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT:
                    self.right += 1
                    self.right_flag = True


                elif event.type == pygame.K_LEFT:
                    self.left += 1
                    self.left_flag = True


if __name__ == '__main__':
    te = Tetris()
    te.run_game()

# class Tetris:
#     def __init__(self):
#         pygame.init()
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.type == pygame.K_RIGHT:
#                 print('R')
#             if event.type == pygame.K_LEFT:
#                 print('L')
#             else:
#                 print(event.type)
