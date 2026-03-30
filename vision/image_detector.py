import cv2
import os
from vision.screen_capture import capturar_tela

def encontrar(template_path, threshold=0.8):

    frame = capturar_tela()

    # converter screenshot para grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # pegar caminho absoluto da pasta do projeto
    base_path = os.path.dirname(os.path.dirname(__file__))

    # montar caminho completo da imagem
    full_path = os.path.join(base_path, template_path)

    # carregar template
    template = cv2.imread(full_path, 0)

    if template is None:
        print("Erro ao carregar imagem:", full_path)
        return None

    result = cv2.matchTemplate(frame_gray, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:

        x = max_loc[0] + template.shape[1] // 2
        y = max_loc[1] + template.shape[0] // 2

        return (x, y)

    return None