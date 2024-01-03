import math

class SudokuSolver:
    def __init__(self, sudoku: list[list[int]]) -> None:
        size = len(sudoku)
        if (not math.sqrt(size).is_integer()):
            raise ValueError("Incorrect sudoku: impossible sudoku")
        for line in sudoku:
            if len(line) != size:
                raise ValueError("Incorrect sudoku: sudoku must be a square shape")
        self.sudoku = sudoku
        self.block_size = int(math.sqrt(size))
        self.size = size

    def solve_sudoku(self) -> None:
        print("Unsolved sudoku:")
        self.print_sudoku()
        if self.__try_solve__(0, 0):
            print("Solved sudoku:")
            self.print_sudoku()
        else:
            print("Incorrect sudoku:")
            self.print_sudoku()

    def __try_solve__(self, i: int, j: int) -> bool:
        if i >= self.size:
            return True
        next_i = i + ((j + 1) // self.size)
        next_j = (j + 1) % self.size
        if self.sudoku[i][j]:
            return self.__try_solve__(next_i, next_j)
        for val in range(1, self.size + 1):
            if self.__val_is_fit__(i, j, val):
                self.sudoku[i][j] = val
                if self.__try_solve__(next_i, next_j):
                    return True
        self.sudoku[i][j] = 0
        return False

    def __val_is_fit__(self, i: int, j: int, val: int) -> bool:
        row_set = set(self.sudoku[i])
        col_set = set([self.sudoku[row][j] for row in range(self.size)])
        block_set = set()
        block_row = (i // self.block_size) * self.block_size
        block_col = (j // self.block_size) * self.block_size
        for block_i in range(self.block_size):
            for block_j in range(self.block_size):
                block_set.add(self.sudoku[block_row + block_i][block_col + block_j])
        if val in row_set or val in col_set or val in block_set:
            return False
        return True

    def print_sudoku(self) -> None:
        for i in range(self.size):
            print()
            if i and i % self.block_size == 0:
                print(" ".join("-" * (self.block_size + self.size - 1)))
            for j in range(self.size):
                if j and j % self.block_size == 0:
                    print("|", end=" ")
                print(self.sudoku[i][j], end=" ")
        print()
