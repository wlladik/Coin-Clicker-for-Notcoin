import random
import time
import pyautogui


def get_mouse_coordinates():
    print("Йоу, наведи мишку на монетку і зачекай 5 секунд.")
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"Координати кліку: x = {x}, y = {y}")
    return x, y


coin_coordinate_1, coin_coordinate_2 = get_mouse_coordinates()


def reload_mouse_coordinates():
    print("Наведи мишку на три крапки зверху і зачекай 8 секунд.")
    time.sleep(8)
    x1, y1 = pyautogui.position()
    print(f"Координати кліку 1: x = {x1}, y = {y1}")
    print("Наведи мишку на 'Reload Page' і зачекай 8 секунд.")
    time.sleep(8)
    x2, y2 = pyautogui.position()
    print(f"Координати кліку 2: x = {x2}, y = {y2}")
    return x1, y1, x2, y2


x1_reload, y1_reload, x2_reload, y2_reload = reload_mouse_coordinates()


def clicker(x_coin, y_coin, x1_dots, y1_dots, x2_refresh, y2_refresh):
    start_time = time.time()

    while True:
        click_x, click_y = random.choice(x_coin), random.choice(y_coin)
        pyautogui.tripleClick(click_x, click_y)
        time.sleep(0.025)  # Швидкість кліків в мс, за потреби можна змінити
        if time.time() - start_time >= clicks_duration:
            time.sleep(15)
            pyautogui.click(x1_dots, y1_dots)
            time.sleep(2)
            pyautogui.click(x2_refresh, y2_refresh)
            pyautogui.click()
            time.sleep(rest)
            start_time = time.time()


if __name__ == "__main__":
    clicks_duration = 50  # Тривалість циклу (в секундах)/ залежить на скільки у вас прокачені кліки (в мене по 11 за клік)
    rest = 1375  # Час очікування (в секундах)/ залкжить від того скільки у вас прокачена енергія і відновлення (в мене 5000 і по 4 відновлює в секунду)
    rand_x = []
    rand_y = []

    for position in range(1, 4):
        if position == 1:
            rand_x.append(coin_coordinate_1)
            rand_y.append(coin_coordinate_2)
        elif position == 2:
            coin_coordinate_1 += 25
            coin_coordinate_2 += 20
            rand_x.append(coin_coordinate_1)
            rand_y.append(coin_coordinate_2)
        elif position == 3:
            coin_coordinate_1 -= 25
            coin_coordinate_2 -= 20
            rand_x.append(coin_coordinate_1)
            rand_y.append(coin_coordinate_2)

    clicker(rand_x, rand_y, x1_reload, y1_reload, x2_reload, y2_reload)

