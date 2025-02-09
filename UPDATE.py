import pyautogui as pg, time, os

def window_up(window_title):
  try:
    # Получаем список всех открытых окон, содержащих заданный заголовок.
    windows = pg.getWindowsWithTitle(window_title)

    if windows:
      # Берем первое окно из списка (обычно это нужное окно).
      window = windows[0]
      window.activate()
      print(f"Окно с заголовком '{window_title}' активировано.")
    else:
      print(f"Окно с заголовком '{window_title}' не найдено.")
  except Exception as e:
    print(f"Произошла ошибка: {e}")

def github_update():
    pg.click(750, 80)

if __name__ == "__main__":
    os.system("taskkill /IM python.exe /F")
    window_up("GitHub Desktop")
    github_update()

    time.sleep(10)
    github_update()

    time.sleep(10)
    os.system("start python bot_test.py")
    exit()

