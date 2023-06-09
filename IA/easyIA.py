import random
from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA

# Description de l'IA la plus naïve et avec le moins de calcul possible.
# Elle renvoie un coup aléatoire parmi les coups possibles.
# Elle a 0 coup d'avance.

class EasyIA(AbstractIA):
    def __init__(self):
        super().__init__()

    def getMove(self, boardModel: OthelloBoardModel) -> tuple[int, int]:
        # On retourne un coup aléatoire parmi les coups possibles
        return random.choice(boardModel.getValidMoves())