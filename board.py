from string import ascii_uppercase

class Board:
    IDENTIFIER = ascii_uppercase
    NONE_STR = 'X'
    MAXIMUM = 26

    def __init__(self, row, column):
        MAX = self.MAXIMUM
        error_str = f"{{}} must be greater than 0 and less than or equal to {MAX}"
        
        if 0 >= row or row > MAX:
            raise ValueError(error_str.format('Row'))
        self.row = row
        
        if 0 >= column or column > MAX:
            raise ValueError(error_str.format('Column'))
        self.column = column
        
        self.board = [[None for _ in range(column)] for _ in range(row)]
    
    def __getitem__(self, index):
        return self.board[index]
    
    def __str__(self):
        str_ = []
        NONE_STR = self.NONE_STR
        for index, row in enumerate(self.board, 1):
            row = [str(item) if item is not None else NONE_STR for item in row]
            row.append(str(index))
            str_.append(''.join(row))
        str_.insert(0, self.IDENTIFIER[:index])
        return ''.join(str_)
