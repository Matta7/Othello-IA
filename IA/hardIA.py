from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA
from IA import heuristic
from IA.minimax import Minimax

# Description d'une IA compliquée qui a 2 coups d'avances, qui utilise
# l'algorithme Minimax et l'heuristique de parité.

class HardIA(AbstractIA):
    calculatoryIA = Minimax(p = 2, h = heuristic.parity)

    def __init__(self):
        super().__init__()

    def getMove(self, boardModel: OthelloBoardModel) -> tuple[int, int]:
        return self.calculatoryIA.getMove(boardModel)
