from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA
from IA import heuristic
from IA.negAlphaBeta import NegAlphaBeta

# Description d'une IA très complexe qui a 3 coups d'avances, qui utilise
# l'algorithme NegAlphaBeta et l'heuristique d'occupation.

class VeryHardIA(AbstractIA):
    calculatoryIA = NegAlphaBeta(p = 3, h = heuristic.occupation)

    def __init__(self):
        super().__init__()

    def getMove(self, boardModel: OthelloBoardModel) -> tuple[int, int]:
        return self.calculatoryIA.getMove(boardModel)