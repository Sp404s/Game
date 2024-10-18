import pygame

class Inventory:
    def __init__(self, slots=8):
        self.slots = slots  # Количество слотов в инвентаре
        self.items = []  # Список предметов в инвентаре

    def add_item(self, item_name):
        """Добавляет предмет в инвентарь, если есть свободное место."""
        if len(self.items) < self.slots:
            self.items.append(item_name)
            print(f"Item '{item_name}' added to inventory.")
        else:
            print("Inventory is full!")

    def clear(self):
        """Очищает инвентарь, удаляя все предметы."""
        self.items.clear()  # Очищаем список предметов
        print("Inventory cleared.")

    def draw(self, screen):
        """Отрисовка инвентаря в левом верхнем углу."""
        slot_width = 50
        slot_height = 50
        slot_margin = 10
        start_x = 10
        start_y = 10

        # Отрисовка пустых слотов
        for i in range(self.slots):
            x = start_x + i * (slot_width + slot_margin)
            pygame.draw.rect(screen, (50, 50, 50), (x, start_y, slot_width, slot_height), 2)

        # Отрисовка предметов в слотах
        font = pygame.font.Font(None, 24)
        for index, item in enumerate(self.items):
            if index < self.slots:
                x = start_x + index * (slot_width + slot_margin)
                item_text = font.render(item[:2], True, (0, 0, 0))  # Отображаем первые две буквы предмета
                screen.blit(item_text, (x + 10, start_y + 10))
