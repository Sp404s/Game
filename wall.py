# wall.py
import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((139, 69, 19))  # Коричневый цвет для стены
        self.rect = self.image.get_rect(topleft=(x, y))
        self.is_visible = True

    def update(self):
        if not self.is_visible:
            self.rect.y += 5  # Двигаем стену вниз
