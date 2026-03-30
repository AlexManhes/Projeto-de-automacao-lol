import time
from core.image_finder import tirar_screenshot, encontrar
from core.bot_actions import clicar
from core.windows_input import mover_mouse
from game.gameplay_bot import jogar


# -----------------------
# Detectar estado inicial
# -----------------------

screenshot = tirar_screenshot()

if encontrar(screenshot, "images/in_game.png"):
    estado = "IN_GAME"

elif encontrar(screenshot, "images/confirmar_personagem.png"):
    estado = "CHAMP_SELECT"

elif encontrar(screenshot, "images/fim_partida.png"):
    estado = "END_GAME"

else:
    estado = "LOBBY"

print("Estado inicial detectado:", estado)


# controle do end game
fim_partida_clicado = False


# -----------------------
# Loop principal
# -----------------------

while True:

    screenshot = tirar_screenshot()

    print("Estado atual:", estado)


    # -----------------
    # LOBBY
    # -----------------
    if estado == "LOBBY":

        pos = encontrar(screenshot, "images/encontrar_partida.png")

        if pos:
            print("Encontrar partida")
            clicar(pos)
            mover_mouse(100, 100)
            time.sleep(3)
            continue


        pos = encontrar(screenshot, "images/aceitar_partida.png")

        if pos:
            print("Aceitar partida")
            clicar(pos)
            mover_mouse(100, 100)
            estado = "CHAMP_SELECT"
            time.sleep(3)
            continue


    # -----------------
    # CHAMP SELECT
    # -----------------
    elif estado == "CHAMP_SELECT":

        pos = encontrar(screenshot, "images/confirmar_personagem.png")

        if pos:
            print("Confirmar personagem")
            clicar(pos)
            mover_mouse(100, 100)
            estado = "IN_GAME"
            time.sleep(5)
            continue


    # -----------------
    # IN GAME
    # -----------------
    elif estado == "IN_GAME":

        pos = encontrar(screenshot, "images/fim_partida.png")

        if pos:
            print("Partida terminou")
            estado = "END_GAME"
            continue


        pos = encontrar(screenshot, "images/in_game.png")

        if pos:
            jogar()


    # -----------------
    # END GAME
    # -----------------
    elif estado == "END_GAME":

        # clicar apenas uma vez no botão fim_partida
        if not fim_partida_clicado:

            pos = encontrar(screenshot, "images/fim_partida.png")

            if pos:
                print("Clicando em fim da partida")
                clicar(pos)

                mover_mouse(100, 100)

                fim_partida_clicado = True

                # esperar carregar próxima tela
                time.sleep(6)
                continue

        # agora procurar apenas continuar
        pos = encontrar(screenshot, "images/continuar.png")

        if pos:
            print("Voltando ao lobby")
            clicar(pos)

            mover_mouse(100, 100)

            estado = "LOBBY"
            fim_partida_clicado = False

            time.sleep(5)
            continue


    time.sleep(1)