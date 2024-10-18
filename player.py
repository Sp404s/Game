import pygame
from inventory import Inventory

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.target_pos = None  # Позиция, куда движется игрок
        self.target_item = None  # Предмет, который игрок хочет подобрать
        self.target_npc = None  # NPC, с которым игрок хочет поговорить
        self.inventory = Inventory()  # Создаем объект инвентаря
        self.talking = False  # Флаг, указывающий, ведется ли разговор
        self.name = "Игрок"  # Имя игрока, используемое для взаимодействия с NPC

    def update(self):
        if self.target_pos:
            if abs(self.target_pos - self.rect.x) > self.speed:
                if self.target_pos > self.rect.x:
                    self.rect.x += self.speed
                else:
                    self.rect.x -= self.speed
            else:
                # Если дошел до целевой позиции
                self.rect.x = self.target_pos
                self.target_pos = None
                if self.target_item:
                    self.pick_item(self.target_item)
                    self.target_item = None
                elif self.target_npc:
                    self.talking = True  # Начинаем разговор
                    self.target_npc = None  # Сброс цели, чтобы не двигаться дальше

    def move_to(self, x):
        self.target_pos = x

    def pick_item(self, item):
        self.inventory.add_item(item.name)  # Добавляем предмет в инвентарь
        item.kill()  # Удаляем предмет из группы

    def set_target_item(self, item):
        self.target_item = item
        self.target_pos = item.rect.x

    def set_target_npc(self, npc):
        self.target_npc = npc
        self.target_pos = npc.rect.x - 50  # Остановиться в 50 пикселях слева от NPC

    def draw_inventory(self, screen):
        self.inventory.draw(screen)
