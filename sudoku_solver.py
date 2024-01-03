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
        self.row_sets = [set() for i in range(size)]
        self.col_sets = [set() for i in range(size)]
        self.block_sets = [set() for i in range(size)]
        for i in range(size):
            row_set = self.row_sets[i]
            for j in range(size):
                val = sudoku[i][j]
                if not val:
                    continue
                if val in row_set:
                    raise ValueError("Incorrect sudoku: initial sudoku does not satisfy sudoku rules")
                row_set.add(val)
        for j in range(size):
            col_set = self.col_sets[j]
            for i in range(size):
                val = sudoku[i][j]
                if not val:
                    continue
                if val in col_set:
                    raise ValueError("Incorrect sudoku: initial sudoku does not satisfy sudoku rules")
                col_set.add(val)
        for i in range(size):
            for j in range(size):
                val = sudoku[i][j]
                if not val:
                    continue
                block_row = (i // self.block_size)
                block_col = (j // self.block_size)
                block_set = self.block_sets[block_row * self.block_size + block_col]
                if val in block_set:
                    raise ValueError("Incorrect sudoku: initial sudoku does not satisfy sudoku rules")
                block_set.add(val)

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
            if self.__val_is_fit_optimized__(i, j, val):
                self.sudoku[i][j] = val
                if self.__try_solve__(next_i, next_j):
                    return True
        self.sudoku[i][j] = 0
        return False

    def __val_is_fit_optimized__(self, i: int, j: int, val: int) -> bool:
        row_set = self.row_sets[i]
        col_set = self.col_sets[j]
        block_row = (i // self.block_size)
        block_col = (j // self.block_size)
        block_set = self.block_sets[block_row * self.block_size + block_col]
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
