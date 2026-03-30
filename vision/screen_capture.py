import mss
import numpy as np

def capturar_tela():

    with mss.mss() as sct:

        monitor = sct.monitors[1]  # monitor principal

        img = np.array(sct.grab(monitor))

        return img