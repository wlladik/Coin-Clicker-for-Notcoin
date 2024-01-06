import random
import time
import pyautogui

# def get_mouse_coordinates():
#     print("Йоу, наведи мишку на монетку і зачекай 5 секунд.")
#     time.sleep(5)
#     x, y = pyautogui.position()
#     print(f"Координати кліку: x = {x}, y = {y}")
#     return x, y
#
# if __name__ == "__main__":
#     click_x, click_y = get_mouse_coordinates()
#     print(f"Встановлені координати для кліку: x = {click_x}, y = {click_y}")


def clicker(x, y):
    start_time = time.time()

    while True:
        click_x, click_y = random.choice(rand_x), random.choice(rand_y)
        pyautogui.click(click_x, click_y)
        time.sleep(0.03)  # Швидкість кліків, за потреби можна змінити
        if time.time() - start_time >= clicks_duration:
            time.sleep(rest)
            start_time = time.time()


if __name__ == "__main__":
    clicks_duration = 100  # Тривалість циклу (в секундах)
    rest = 1250  # Час очікування (в секундах)
    rand_x = [1526, 1500, 1564]
    rand_y = [302, 287, 321]
    clicker(rand_x, rand_y)

