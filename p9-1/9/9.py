class TicTacToe:
    def __init__(self):
        self._marks = [[' ', ' ', ' '] for _ in range(3)]
        self.cross_moves = True
        
    def show(self):
        for i, line in enumerate(self._marks):
            print('|'.join(line))
            if i < len(self._marks) - 1:  # Не печатать после последней строки
                print('-----')

    def mark(self, x, y):
        x -= 1
        y -= 1
        winner = self.winner()
        if not winner:
            if self._marks[x][y] == ' ':
                if self.cross_moves:
                    self._marks[x][y] = 'X'
                else:
                    self._marks[x][y] = 'O'
                self.cross_moves = not self.cross_moves
            else:
                print('Недоступная клетка')
        else:
            print('Игра окончена')

    def winner(self):
        for row in self._marks:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        for col in range(3):
            if self._marks[0][col] == self._marks[1][col] == self._marks[2][col] != ' ':
                return self._marks[0][col]
        
        if self._marks[0][0] == self._marks[1][1] == self._marks[2][2] != ' ':
            return self._marks[0][0]
        if self._marks[0][2] == self._marks[1][1] == self._marks[2][0] != ' ':
            return self._marks[0][2]
        
        draw = True
        for line in self._marks:
            if any(i == ' ' for i in line):
                draw = False
        if draw:
            return 'Ничья'
        return None
