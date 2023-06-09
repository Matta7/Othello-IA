import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model.Color import Color

class OthelloBoardModel():
    board = None
    turn = None
    validMoves = None
    blackScore = None
    whiteScore = None
    gameOver = None
    last_valid_moves = None
    last_board_state = None
    last_black_score = None
    last_white_score = None
    memory = None
    nbTurn = None
    memoryTurn = None

    def __init__(self):
        super().__init__()
        self.board = [[Color.EMPTY for _ in range(8)] for _ in range(8)]
        # Les 4 cases centrales sont initialisées avec 2 pions blancs et 2 pions noirs
        self.setCell(3, 3, Color.WHITE)
        self.setCell(4, 4, Color.WHITE)
        self.setCell(3, 4, Color.BLACK)
        self.setCell(4, 3, Color.BLACK)
        self.setTurn(Color.BLACK)
        # Les mouvements valides sont les cases adjacentes à un pion de l'adversaire
        # qui sont vides et qui permettent de capturer des pions de l'adversaire
        self.setValidMoves([(3, 2), (2, 3), (5, 4), (4, 5)])
        self.setBlackScore(2)
        self.setWhiteScore(2)
        self.setGameOver(False)
        self.last_valid_moves = [] 
        self.last_board_state = []
        self.last_black_score = 0
        self.last_white_score = 0
        self.nbTurn = 0
        self.memoryTurn = self.nbTurn
        self.memory = [self.board]

    def copy(self):
        board = OthelloBoardModel()
        board.setBoard([[self.getCell(row, column) for column in range(8)] for row in range(8)])
        board.setTurn(self.getTurn())
        board.setValidMoves(self.getValidMoves())
        board.setBlackScore(self.getBlackScore())
        board.setWhiteScore(self.getWhiteScore())
        board.setGameOver(self.getGameOver())
        return board

    # Get the board.
    def getBoard(self):
        return self.board
    
    # Set the board.
    def setBoard(self, board):
        self.board = board


    # Get the color's turn.
    def getTurn(self) -> Color:
        return self.turn

    # Set the color's turn.
    def setTurn(self, turn: Color):
        self.turn = turn

    # Switch the turn.
    def switchTurn(self):
        if self.getTurn() == Color.BLACK:
            self.setTurn(Color.WHITE)
        else:
            self.setTurn(Color.BLACK)


    #def getValidMoves(self) -> list[tuple[int, int]]:
        #return self.validMoves
    
    # Set the valid moves.
    def setValidMoves(self, validMoves: list[tuple[int, int]]):
        self.validMoves = validMoves

    # Calcul the valid moves.
    def getValidMoves(self):
        validMoves = []
        for row in range(8):
            for column in range(8):
                if self.getCell(row, column) == Color.EMPTY: # Si la case est vide.
                    if self.isCellValidMove(row, column): # Si la case est valide.
                        validMoves.append((row, column))
        return validMoves

    # Get the black score.
    def getBlackScore(self) -> int:
        return self.black_score
    
    # Set the black score.
    def setBlackScore(self, black_score: int):
        self.black_score = black_score

    # Get the white score.
    def getWhiteScore(self) -> int:
        return self.white_score
    
    # Set the white score.
    def setWhiteScore(self, white_score: int):
        self.white_score = white_score

    # Return True if game is over. 
    def getGameOver(self) -> bool:
        return self.game_over

    def setGameOver(self, game_over: bool):
        self.game_over = game_over

    # Get the board[row][column] value.
    def getCell(self, row: int, column: int) -> Color:
        if row < 0 or row >= 8 or column < 0 or column >= 8:
            raise IndexError("Invalid cell index")
        else:
            return self.board[row][column]
        
    # Set the board[row][column] value.
    def setCell(self, row: int, column: int, color: Color):
        if row < 0 or row >= 8 or column < 0 or column >= 8:
            raise IndexError("Invalid cell index")
        else:
            self.board[row][column] = color

    # Get all the adjacent cells.
    def getAdjacentCells(self, row: int, column: int) -> list[tuple[int, int]]:
        adjacent_cells = []
        for i in [-1, 1]:
            for j in [-1, 1]:
                if row + i <= 7 or row + i >= 0 or column + i <= 7 or column + i >= 0:
                    adjacent_cells.append((row + i, column + j))
        return adjacent_cells
    
    def undo(self):
        #print(self.memoryTurn > 1)
        if self.memoryTurn > 0:
            self.memoryTurn -= 1
            self.setBoard(self.memory[self.memoryTurn])
            self.switchTurn()
            print(self.board[4][4])
            print(self.memoryTurn)
            print(self.nbTurn)

    
    def next(self, move: tuple[int, int]):
        if self.memoryTurn == self.nbTurn:
            self.nbTurn += 1
            self.memoryTurn += 1
            self.setCell(move[0], move[1], self.turn)
            self.updateBoard(move[0], move[1])
            self.switchTurn()
            self.updateAll()
            self.memory.append(self.board)
        else:
            if self.memoryTurn < self.nbTurn:
                self.memoryTurn += 1
                self.setBoard(self.memory[self.memoryTurn])
                
    # Return True if the cell is a valid move.
    def isCellValidMove(self, row: int, column: int) -> bool:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0): # On ne vérifie pas pour la case elle-même.
                    if self.checkDirection(row, column, (i, j)): # On vérifie toutes les directions.
                        return True
        return False
    
    # Check the direction from a cell.
    def checkDirection(self, row: int, column: int, direction: tuple) -> bool:
        i = row + direction[0]
        j = column + direction[1]

        if i > 7 or i < 0 or j > 7 or j < 0:
            return False

        if self.getCell(i, j) == self.getTurn().opposite():

            i += direction[0]
            j += direction[1]
            while True:
                # Si nous atteignons un bord.
                if i > 7 or i < 0 or j > 7 or j < 0:
                    return False
                
                cell = self.getCell(i, j)
                # Si la case contient la couleur du tour actuel.
                if cell == self.getTurn():
                    return True
                
                # Si la case contient la couleur opposée du tour actuel.
                elif cell == self.getTurn().opposite():
                    i += direction[0]
                    j += direction[1]
                else: 
                    return False

        return False

    # Update the valid moves.
    def updateValidMoves(self):
        self.setValidMoves(self.getValidMoves())

    # Update the board.
    def updateBoard(self, row: int, column: int):
        # On parcourt la grille pour trouver les pions qui ont été capturés
        # On utilise une liste pour stocker les pions à capturer
        # On ne peut pas capturer les pions directement dans la boucle
        # car on risque de modifier la liste pendant qu'on la parcourt
        # On parcourt la liste des pions à capturer après la boucle
        # pour capturer les pions
        self.last_board_state = self.getBoard()
        self.last_valid_moves = self.getValidMoves()
        self.last_black_score = self.getBlackScore()
        self.last_white_score = self.getWhiteScore()
        captured_pieces = []
        color = self.getCell(row, column)
        for row_direction in [-1, 0, 1]:
            for column_direction in [-1, 0, 1]:
                if row_direction != 0 or column_direction != 0:
                    # Si la case adjacente est celle de l'adversaire
                    # on parcourt les cases dans la même direction jusqu'à trouver
                    # un pion de la même couleur que le joueur en cours.
                    # Si on trouve un pion de la même couleur que le joueur en cours, on retourne tout les pions
                    # entre le pion de la même couleur et le pion qu'on vient de poser
                    # Sinon, on ne fait rien
                    row_to_check = row + row_direction
                    column_to_check = column + column_direction
                    if row_to_check >= 0 and row_to_check < 8 and column_to_check >= 0 and column_to_check < 8:
                        if self.getCell(row_to_check, column_to_check) == color.opposite():
                            while row_to_check >= 0 and row_to_check < 8 and column_to_check >= 0 and column_to_check < 8:
                                if self.getCell(row_to_check, column_to_check) == color:
                                    row_to_check -= row_direction
                                    column_to_check -= column_direction
                                    while row_to_check != row or column_to_check != column:
                                        captured_pieces.append((row_to_check, column_to_check))
                                        row_to_check -= row_direction
                                        column_to_check -= column_direction
                                    break
                                elif self.getCell(row_to_check, column_to_check) == Color.EMPTY:
                                    break
                                row_to_check += row_direction
                                column_to_check += column_direction
        # On parcourt la liste des pions à capturer pour les capturer
        for row, column in captured_pieces:
            self.setCell(row, column, self.getTurn())

    # Update the scores.
    def updateScores(self):
        black_score = 0
        white_score = 0
        for row in range(8):
            for column in range(8):
                if self.getCell(row, column) == Color.BLACK:
                    black_score += 1
                elif self.getCell(row, column) == Color.WHITE:
                    white_score += 1
        self.setBlackScore(black_score)
        self.setWhiteScore(white_score)

    def updateGameOver(self):
        if len(self.getValidMoves()) == 0:
            print("No valid moves : Switching turn")
            self.switchTurn()
            self.updateValidMoves()
            if len(self.getValidMoves()) == 0:
                print("Game over")
                self.setGameOver(True)

    def updateAll(self):
        self.updateValidMoves()
        self.updateScores()
        self.updateGameOver()