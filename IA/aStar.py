################################################################################
###                                  A*                                      ###
################################################################################
import numpy as np
from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA
from IA import heuristic
from Model.Color import Color

class AStar(AbstractIA):
    # les valeurs par défaut pour la profondeur et l'heuristique utilisée sont:
    # 1 et parity.
    def __init__(self, p = 1, h = heuristic.parity):
        super().__init__()
        self.p = p
        self.h = h
        self.color = Color.EMPTY
    
    def getMove(self, board: OthelloBoardModel) -> tuple[int, int]:
        self.color = board.getTurn()
        return self.aStar(board)
    
    # Implantation d'une modification de l'algorithme A*, qui renvoie le coups
    # optimal selon l'algo et la configuration initiale.
    def aStar(self, board: OthelloBoardModel) -> tuple[int, int]:
        delta = {}
        pi = {}
        O = {}
        f = {}
        p = self.p
        delta[board] = 0
        O[board] = p
        f[board] = self.h(board, self.color)
        while(p != 0 and len(O) > 0 and not self.isFinalMove(boardModel=board)):
            self.examiner(board, delta, pi, O, f)
            y = - np.inf
            for z in O:
                if y < f[z]:
                    y = f[z]
                    board = z
                    p = O[z]
        return pi[board]
    
    def ouvrir(self, x, p, O):
        O[x] = p

    def fermer(self, x, O):
        O.pop(x)

    def examiner(self, x: OthelloBoardModel, delta: dict, pi: dict, O: list, f: dict):
        for (row, column) in x.getValidMoves():
            y = self.simulateMove(x, row, column)
            p = O[x] - 1
            if y in delta and delta[x] + p < delta[y] or y not in delta:
                delta[y] = delta[x] + p
                if x in pi:
                    pi[y] = pi[x]
                else: 
                    pi[y] = (row, column)
                f[y] = delta[y] + self.h(y, self.color)
                self.ouvrir(y, p, O)
        self.fermer(x, O)
