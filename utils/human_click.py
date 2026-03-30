import pyautogui
import random

def click_humano(x, y):

    pyautogui.moveTo(
        x + random.randint(-4,4),
        y + random.randint(-4,4),
        duration=random.uniform(0.15,0.35)
    )

    pyautogui.click()