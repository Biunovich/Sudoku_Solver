import math

class Solver:
    def __init__(self, sudoku: list[list[int]]) -> None:
        size = len(sudoku)
        if (not math.sqrt(size).is_integer()):
            raise ValueError("Incorrect sudoku: impossible sudoku")
        for line in sudoku:
            if len(line) != size:
                raise ValueError("Incorrect sudoku: sudoku must be a square shape")
        allowed_numbers = set(range(0, size + 1))
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
                col_set = self.col_sets[j]
                block_set = self.__get_block_set__(i, j)
                if val not in allowed_numbers or val in row_set or val in col_set or val in block_set:
                    raise ValueError("Incorrect sudoku: initial sudoku does not satisfy sudoku rules")
                row_set.add(val)
                col_set.add(val)
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
                self.__add_val_to_sets__(i, j, val)
                if self.__try_solve__(next_i, next_j):
                    return True
                self.__remove_val_from_sets__(i, j)
        self.sudoku[i][j] = 0
        return False

    def __val_is_fit_optimized__(self, i: int, j: int, val: int) -> bool:
        row_set = self.row_sets[i]
        col_set = self.col_sets[j]
        block_set = self.__get_block_set__(i, j)
        if val in row_set or val in col_set or val in block_set:
            return False
        return True

    def __add_val_to_sets__(self, i: int, j: int, val: int) -> None:
        self.row_sets[i].add(val)
        self.col_sets[j].add(val)
        self.__get_block_set__(i, j).add(val)

    def __remove_val_from_sets__(self, i: int, j: int) -> None:
        val = self.sudoku[i][j]
        if not val:
            return
        self.row_sets[i].remove(val)
        self.col_sets[j].remove(val)
        self.__get_block_set__(i, j).remove(val)

    def __get_block_set__(self, i: int, j: int) -> set:
        block_row = (i // self.block_size)
        block_col = (j // self.block_size)
        return self.block_sets[block_row * self.block_size + block_col]

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
