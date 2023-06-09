################################################################################
###                               MINIMAX                                    ###
################################################################################
import numpy as np
from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA
from IA import heuristic
from Model.Color import Color

class Minimax(AbstractIA):
    # les valeurs par défaut pour la profondeur et l'heuristique utilisée sont:
    # 1 et parity.
    def __init__(self, p = 1, h = heuristic.parity):
        super().__init__()
        self.p = p
        self.h = h
        self.color = Color.EMPTY

    def getMove(self, board: OthelloBoardModel) -> tuple[int, int]:
        self.color = board.getTurn()
        tup, _ = self.minimax(board, self.p)
        return tup
    
    # Implantation de l'algorithme Minimax, qui renvoie le coups
    # optimal selon l'algo et la configuration initiale.
    # On a adapté l'algorithme Minimax afin qu'il puisse transmettre le meilleur
    # coups et pas seulement sa valeur minimax.
    def minimax(self, board: OthelloBoardModel, p: int):
        tup = (0, 0)
        val = 0
        if p == 0 or self.isFinalMove(board):
            return tup, self.h(board, self.color)
        validMoves = board.getValidMoves()
        if len(validMoves) == 0:
            return self.minimax(board.switchTurn(), p - 1)
        elif self.color == board.getTurn():
            val = - np.inf
            for (row, column) in validMoves:
                _, v = self.minimax(self.simulateMove(board, row, column), p - 1)
                if val < v:
                    val = v
                    tup = (row, column)
        else:
            val = np.inf
            for (row, column) in validMoves:
                _, v = self.minimax(self.simulateMove(board, row, column), p - 1)
                if val > v:
                    val = v
                    tup = (row, column)
        return tup, val
