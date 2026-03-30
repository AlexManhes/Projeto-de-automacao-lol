import pyautogui

def clicar(pos):

    if pos is None:
        return

    x, y = pos

    pyautogui.moveTo(x, y, duration=0.3)
    pyautogui.click()