import cv2
import numpy as np
import pyautogui


def tirar_screenshot():

    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    return screenshot


def encontrar(screenshot, imagem, threshold=0.7):

    template = cv2.imread(imagem)

    if template is None:
        print(f"Erro ao carregar imagem: {imagem}")
        return None

    resultado = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= threshold:

        h, w = template.shape[:2]

        centro_x = max_loc[0] + w // 2
        centro_y = max_loc[1] + h // 2

        return centro_x, centro_y

    return None