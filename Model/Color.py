from enum import Enum

class Color(Enum):
    EMPTY = 0 # Empty cell
    BLACK = 1 # Cell with black pawn
    WHITE = -1 # Cell with white pawn

    # Get the opposite color.
    def opposite(self):
        if self == Color.BLACK:
            return Color.WHITE
        elif self == Color.WHITE:
            return Color.BLACK
        else:
            return Color.EMPTY