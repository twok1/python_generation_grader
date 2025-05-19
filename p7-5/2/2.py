from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        move_to_horizontal = ord(self.horizontal) - ord(horizontal)
        move_to_vertical = self.vertical - vertical
        if (move_to_horizontal in range(-1, 2) and move_to_vertical in (-1, 1)) or move_to_horizontal in (-1, 1) and move_to_vertical in range(-1, 2):
            return True
        return False

class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        move_to_horizontal = ord(self.horizontal) - ord(horizontal)
        move_to_vertical = self.vertical - vertical
        if (move_to_vertical in (-2, 2) and move_to_horizontal in (-1, 1)) or move_to_vertical in (-1, 1) and move_to_horizontal in (-2, 2):
            return True
        return False