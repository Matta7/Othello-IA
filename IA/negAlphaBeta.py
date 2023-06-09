################################################################################
###                            NEGAPLHABETA                                  ###
################################################################################
import numpy as np
from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA
from IA import heuristic
from Model.Color import Color

class NegAlphaBeta(AbstractIA):
    # les valeurs par défaut pour la profondeur et l'heuristique utilisée sont:
    # 1 et parity.
    def __init__(self, p = 1, h = heuristic.parity):
        super().__init__()
        self.p = p
        self.h = h
        self.color = Color.EMPTY
    
    def getMove(self, board: OthelloBoardModel) -> tuple[int, int]:
        self.color = board.getTurn()
        tup, _ = self.negalphabeta(board, self.p)
        return tup
    
    # Implantation de l'algorithme NegAlphaBeta, qui renvoie le coups
    # optimal selon l'algo et la configuration initiale.
    # On a adapté l'algorithme NegAlphaBeta afin qu'il puisse transmettre le 
    # meilleur coups et pas seulement sa valeur negamax.
    def negalphabeta(self, board: OthelloBoardModel, p: int, alpha = -np.inf, beta = np.inf) -> tuple[tuple[int, int], int]:
        tup = (0, 0)
        val = 0
        if p == 0 or self.isFinalMove(board):
            if self.color == board.getTurn():
                val = self.h(board, self.color)
            else: 
                val = - self.h(board, self.color)
        else:
            val = - np.inf
            validMoves = board.getValidMoves()
            if len(validMoves) == 0:
                _, val = self.negalphabeta(board.switchTurn(), p - 1, -beta, -alpha)
                val = -val
            for (row, column) in validMoves:
                if alpha >= beta:
                    break
                _, v = self.negalphabeta(self.simulateMove(board, row, column), p - 1, -beta, -alpha)
                if val < -v:
                    val = -v
                    tup = (row, column)
                alpha = max(alpha, val)
            beta = max(-alpha, beta)
        return tup, val
