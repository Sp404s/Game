# camera.py

import pygame


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        # Смещение спрайта на экране в зависимости от камеры
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        # Двигаем камеру, центрируя её на игроке
        x = -target.rect.centerx + int(pygame.display.get_surface().get_width() / 2)
        y = -target.rect.centery + int(pygame.display.get_surface().get_height() / 2)

        # Ограничиваем движение камеры, чтобы не выходила за пределы уровня
        x = min(0, x)  # Левый край
        x = max(-(self.width - pygame.display.get_surface().get_width()), x)  # Правый край
        y = min(0, y)  # Верхний край
        y = max(-(self.height - pygame.display.get_surface().get_height()), y)  # Нижний край

        self.camera = pygame.Rect(x, y, self.width, self.height)
