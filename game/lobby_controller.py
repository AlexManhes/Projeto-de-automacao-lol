import time
from vision.image_detector import encontrar
from utils.human_click import click_humano

def iniciar_partida():

    print("Procurando botão iniciar...")

    while True:

        pos = encontrar("images/iniciar.png")

        if pos:

            click_humano(pos[0],pos[1])

            print("Partida iniciada")

            return

        time.sleep(1)