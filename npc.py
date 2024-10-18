import pygame

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = "NPC"

    def interact(self, player):
        """Обработка взаимодействия с игроком."""
        if len(player.inventory.items) == player.inventory.slots:  # Проверяем, собраны ли все предметы
            print(f"{player.name} отдал все предметы {self.name}.")
            player.inventory.clear()  # Очищаем инвентарь
            return True  # Успешный обмен
        else:
            print(f"{player.name} не имеет всех предметов для обмена.")
            return False  # Неуспешный обмен
