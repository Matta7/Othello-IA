import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model.OthelloBoardModel import OthelloBoardModel

class Memory():
    model = None
    memory = None
    nbTurn = None
    memoryTurn = None

    def __init__(self, model: OthelloBoardModel) -> None:
        super().__init__()
        self.model = model
        self.nbTurn = 0
        self.memoryTurn = 0
        self.memory: list[OthelloBoardModel] = [model.copy()]

    # Undo the move done.
    def undo(self):
        if self.memoryTurn > 0:
            self.memoryTurn -= 1
            self.model.setBoard(self.memory[self.memoryTurn].getBoard())
            self.model.switchTurn()
    
    # Redo or play the next move.
    def next(self, move: tuple[int, int]):
        # Play new move.
        if self.memoryTurn == self.nbTurn:
            self.nbTurn += 1
            self.memoryTurn += 1
            self.model.setCell(move[0], move[1], self.model.getTurn())
            self.model.updateBoard(move[0], move[1])
            self.model.switchTurn()
            self.model.updateAll()
            new_board = self.model.copy()
            self.memory.append(new_board)
        # Redo move.
        else:
            if self.memoryTurn < self.nbTurn:
                self.memoryTurn += 1
                self.model.setBoard(self.memory[self.memoryTurn].getBoard())