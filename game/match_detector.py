import time
from vision.image_detector import encontrar
from core.bot_state import BotState

def detectar_estado():

    if encontrar("images/lobby.png"):
        return BotState.LOBBY

    if encontrar("images/champ_select.png"):
        return BotState.CHAMP_SELECT

    if encontrar("images/loading.png"):
        return BotState.LOADING

    if encontrar("images/in_game.png"):
        return BotState.IN_GAME

    if encontrar("images/match_end.png"):
        return BotState.MATCH_END

    return None