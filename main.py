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
# get_mouse_coordinates()


def clicker(x, y):
    start_time = time.time()

    while True:
        click_x, click_y = random.choice(rand_x), random.choice(rand_y)
        pyautogui.click(click_x, click_y)
        time.sleep(0.03)  # Швидкість кліків в мс, за потреби можна змінити
        if time.time() - start_time >= clicks_duration:
            time.sleep(rest)
            start_time = time.time()


if __name__ == "__main__":
    clicks_duration = 100  # Тривалість циклу (в секундах)/ залежить на скільки у вас прокачені кліки (в мене по 10 за клік)
    rest = 1250  # Час очікування (в секундах)/ залкжить від того скільки у вас прокачена енергія і відновлення (в мене 5000 і по 4 відновлює в секунду)
    rand_x = [1526, 1500, 1564]
    rand_y = [302, 287, 321]
    clicker(rand_x, rand_y)

