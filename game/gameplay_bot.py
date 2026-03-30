import time
import random
import pyautogui

from core.image_finder import tirar_screenshot, encontrar


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.05


def mover_aleatorio():

    largura, altura = pyautogui.size()

    x = random.randint(int(largura * 0.3), int(largura * 0.7))
    y = random.randint(int(altura * 0.3), int(altura * 0.7))

    print("Movendo para:", x, y)

    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.rightClick()


def atacar():

    print("Ataque básico")

    pyautogui.press("a")
    time.sleep(0.1)

    largura, altura = pyautogui.size()

    x = random.randint(int(largura * 0.3), int(largura * 0.7))
    y = random.randint(int(altura * 0.3), int(altura * 0.7))

    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.leftClick()


def usar_habilidades():

    habilidades = ["q", "w", "e"]

    habilidade = random.choice(habilidades)

    print("Usando habilidade:", habilidade)

    pyautogui.press(habilidade)


def jogar():

    print("Bot começou a jogar")

    ultimo_movimento = time.time()

    while True:

        screenshot = tirar_screenshot()

        # verifica se a partida terminou
        fim = encontrar(screenshot, "images/fim_partida.png", 0.8)

        if fim:
            print("Fim da partida detectado")
            break

        agora = time.time()

        if agora - ultimo_movimento > random.randint(4, 7):

            mover_aleatorio()

            if random.random() > 0.5:
                atacar()

            if random.random() > 0.7:
                usar_habilidades()

            ultimo_movimento = agora

        time.sleep(1)