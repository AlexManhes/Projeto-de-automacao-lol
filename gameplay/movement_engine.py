import random
import time
from utils.human_click import click_humano

def mover():

    print("Movendo personagem")

    for i in range(150):

        x = random.randint(1000,1300)
        y = random.randint(450,700)

        click_humano(x,y)

        time.sleep(random.uniform(0.8,1.6))