# item.py

import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((50, 200, 50))  # Цвет предмета
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name  # Имя предмета


