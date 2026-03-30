import cv2
import numpy as np
import pyautogui


def encontrar_minions():

    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # converter para HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # faixa de vermelho
    lower_red1 = np.array([0,120,70])
    upper_red1 = np.array([10,255,255])

    lower_red2 = np.array([170,120,70])
    upper_red2 = np.array([180,255,255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # encontrar contornos
    contornos, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    minions = []

    for c in contornos:

        area = cv2.contourArea(c)

        if area > 50 and area < 500:

            x, y, w, h = cv2.boundingRect(c)

            centro_x = x + w // 2
            centro_y = y + h + 20

            minions.append((centro_x, centro_y))

    return minions