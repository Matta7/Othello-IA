from Model.OthelloBoardModel import OthelloBoardModel
from abc import ABC, abstractclassmethod, abstractproperty


# Défini une interface pour les IA.
# La fonction getMove est celle qui calculera le coups optimal suivant la 
# configuration passée en paramètres.
# C'est principalement celle-ci qui sera appelée par l'interface.

class AbstractIA(ABC):
    @classmethod
    def __init__(self) -> None:
        pass

    @classmethod
    def getMove(self, boardModel: OthelloBoardModel) -> tuple[int, int]:
        pass

    # Fonction qui simule un coups, puis retourne le board simulé.
    # Elle sera utile dans la plupart des calculs d'IAs.
    def simulateMove(self, boardModel: OthelloBoardModel, row: int, column: int) -> OthelloBoardModel:
        # On copie le plateau
        board = boardModel.copy()
        # On joue le coup passé en paramètre
        board.setCell(row, column, board.getTurn())
        board.updateBoard(row, column)
        board.updateScores()
        board.switchTurn()
        board.updateValidMoves()
        board.updateGameOver()
        return board
    
    # Fonction qui permet de savoir si le plateau est une configuration finale
    # du jeu.
    def isFinalMove(self, boardModel: OthelloBoardModel) -> bool:
        return boardModel.getGameOver()
