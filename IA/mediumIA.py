from Model.OthelloBoardModel import OthelloBoardModel
from IA.AbstractIA import AbstractIA

# Description d'une IA ayant 1 coup d'avance, elle recherche juste parmi les
# coups celui qui serait intéressant de jouer pour le très court terme.

class MediumIA(AbstractIA):
    def __init__(self):
        super().__init__()
    
    def getMove(self, boardModel: OthelloBoardModel) -> tuple[int, int]:
        # On simule chacun des coups possibles
        # On prend le coup qui donne le plus haut score pour l'IA
        bestScore = -1000
        bestMove = None

        # On récupère les coups possibles
        validMoves = boardModel.getValidMoves()
        # On simule chacun des coups possibles
        for (row, column) in validMoves:
            # On simule le coup et on récupère son score
            score = self.simulateMove(boardModel, row, column)
            # On compare le score
            if score > bestScore:
                bestScore = score
                bestMove = (row, column)
        return bestMove
    
    def simulateMove(self, boardModel: OthelloBoardModel, row: int, column: int) -> int:
        # On copie le plateau
        board = boardModel.copy()
        # On joue le coup passé en paramètre
        board.setCell(row, column, board.getTurn())
        board.updateBoard(row, column)
        board.updateScores()
        
        return board.getWhiteScore()