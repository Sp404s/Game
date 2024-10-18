import pygame
import sys

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 74)
        self.small_font = pygame.font.Font(None, 36)
        self.start_button_rect = pygame.Rect(400, 300, 200, 50)
        self.settings_button_rect = pygame.Rect(400, 400, 200, 50)

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen, color, rect)
        label = self.font.render(text, True, (255, 255, 255))
        label_rect = label.get_rect(center=rect.center)
        self.screen.blit(label, label_rect)

    def show(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # ЛКМ
                        mouse_pos = event.pos
                        if self.start_button_rect.collidepoint(mouse_pos):
                            return "start"  # Начинаем игру
                        if self.settings_button_rect.collidepoint(mouse_pos):
                            return "settings"  # Открываем настройки

            # Заполняем экран белым цветом
            self.screen.fill((0, 0, 0))  # Черный фон

            # Отрисовка кнопок
            self.draw_button("Начать игру", self.start_button_rect, (0, 128, 0))  # Зеленая кнопка
            self.draw_button("Настройки", self.settings_button_rect, (0, 0, 128))  # Синяя кнопка

            pygame.display.flip()
            self.clock.tick(60)
