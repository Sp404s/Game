import pygame
import sys
from player import Player
from item import Item
from platform import Platform
from camera import Camera
from menu import Menu
from wall import Wall  # Импортируем класс Wall из файла wall.py
from npc import NPC  # Импортируем класс NPC из файла npc.py

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 1000
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Мрачный Платформер")

# Цвета
white = (255, 255, 255)


# Основная функция игры
def main():
    clock = pygame.time.Clock()
    player = Player()
    platform = Platform(0, screen_height - 30, 3000, 30)  # Увеличенная платформа

    # Устанавливаем игрока на платформе
    player.rect.y = platform.rect.y - player.rect.height  # Игрок стоит на платформе

    # Создаем группу для всех предметов
    items = pygame.sprite.Group()

    # Создаем восемь предметов на разных дистанциях
    for i in range(8):
        item = Item(200 + i * 100, screen_height - 60, f"Предмет {i + 1}")  # Размещаем предметы
        items.add(item)

    # Создаем стену
    wall = Wall(screen_width + 500, platform.rect.y - 200, 50, 200)  # Стена справа
    all_sprites = pygame.sprite.Group()
    all_sprites.add(platform)
    all_sprites.add(player)
    all_sprites.add(items)
    all_sprites.add(wall)

    # Создаем NPC
    npc = NPC(400, platform.rect.y - 50)  # Устанавливаем NPC над платформой
    all_sprites.add(npc)

    # Инициализация камеры
    camera = Camera(3000, screen_height)  # Размеры игрового мира

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка клика мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # ЛКМ
                    mouse_x, mouse_y = event.pos
                    player.move_to(mouse_x - camera.camera.x)  # Перемещаем игрока по оси X

                    # Проверка клика на предметах
                    for item in items:
                        if item.rect.collidepoint(mouse_x - camera.camera.x, mouse_y - camera.camera.y):
                            player.set_target_item(item)  # Устанавливаем цель для подбора предмета
                            break  # Выходим из цикла после нахождения предмета

                    # Проверка клика на NPC
                    if npc.rect.collidepoint(mouse_x - camera.camera.x, mouse_y - camera.camera.y):
                        if npc.interact(player):  # Если обмен успешен
                            wall.is_visible = False  # Убираем стену
                            # Двигаем стену вниз, если она еще не опустилась
                            if wall.rect.y < platform.rect.y:
                                wall.rect.y += 1  # Скорость опускания стены (1 пиксель за кадр)

        # Обновление состояния игрока и стены
        player.update()

        # Проверка столкновения игрока со стеной
        if pygame.sprite.collide_rect(player, wall) and wall.is_visible:
            if player.rect.right > wall.rect.left:  # Проверяем, что игрок сталкивается с левой стороной стены
                player.rect.right = wall.rect.left  # Останавливаем игрока перед стеной
                player.target_pos = player.rect.x  # Сбрасываем цель перемещения игрока

        # Обновление положения камеры
        camera.update(player)

        # Обновление экрана
        screen.fill(white)  # Цвет фона

        # Отрисовка всех спрайтов
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite))  # Применяем смещение камеры

        # Отрисовка инвентаря игрока
        player.draw_inventory(screen)

        # Отрисовка стены, если она видима
        if wall.is_visible:
            screen.blit(wall.image, camera.apply(wall))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    menu = Menu(screen)  # Создаем экземпляр Menu
    action = menu.show()  # Показываем начальный экран

    if action == "start":
        main()  # Начинаем игру
    elif action == "settings":
        print("Настройки")  # Тут можно добавить логику для настроек
