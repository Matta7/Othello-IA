################################################################################
###                              HEURISTIC                                   ###
################################################################################
import numpy as np
from Model.OthelloBoardModel import OthelloBoardModel
from Model.Color import Color

# Plus la valeur renvoyer par une heuristique est grande, 
# meilleur est l'évaluation du board

# Les valeurs renvoyées par 2 heuristiques différentes n'ont pas vocation à être
# comparées.

# parité: Calcule le nombre de jetons allié - nb jetons adverses
def parity(board: OthelloBoardModel, color: Color) -> int:
    res = board.getBlackScore() - board.getWhiteScore()
    if color == Color.BLACK:
        return res
    else:
        return res * -1

EVALUATION_MATRIX = [[1000, -25, 200, 100, 100, 200 , -25, 1000],
                    [-25 , -50,-10, -5, -5, -10, -50, -25],
                    [200  , -10,  1, 1 , 1 , 1  , -10,  200],
                    [100  , -5 ,  1, 0 , 0 , 1  ,  -5,  100],
                    [100  , -5 ,  1, 0 , 0 , 1  ,  -5,  100],
                    [200  , -10,  1, 1 , 1 , 1  , -10,  200],
                    [-25 , -50,-10, -5, -5, -10, -50, -25],
                    [1000 , -25, 200, 100, 100, 200 , -25, 1000]]

# occupation: Jouer sur le bord => ne pas jamais jouer sur le bord du bord
def occupation(board: OthelloBoardModel, color: Color) -> int:
    b = board.getBoard()
    res = 0
    for i in range(0, 7):
        for j in range(0, 7):
           res += b[i][j].value * EVALUATION_MATRIX[i][j]
    res *= color.value
    return res

SIZE = 64

# mobilité: Réduire les coups de son adversaire
def mobility(board: OthelloBoardModel, color: Color) -> int:
    if board.getTurn() == color:
        b = board.copy()
        b.switchTurn()
        return SIZE - len(b.getValidMoves())
    return SIZE - len(board.getValidMoves())
