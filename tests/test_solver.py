import numpy as np
import pytest
from sudoku_solver.solver import Solver
from numpy.testing import assert_array_equal


class TestSolver:
    def testIncorrectSudoku(self):
        sudoku = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ])

        pytest.raises(ValueError, Solver, sudoku)

    def testIncorrect3DMatrix(self):
        sudoku = np.array([[[1]]])

        pytest.raises(ValueError, Solver, sudoku)

    def testSimpleSudoku(self):
        sudoku = np.array([
            [0,7,0, 5,8,3, 0,2,0],
            [0,5,9, 2,0,0, 3,0,0],
            [3,4,0, 0,0,6, 5,0,7],

            [7,9,5, 0,0,0, 6,3,2],
            [0,0,3, 6,9,7, 1,0,0],
            [6,8,0, 0,0,2, 7,0,0],

            [9,1,4, 8,3,5, 0,7,6],
            [0,3,0, 7,0,1, 4,9,5],
            [5,6,7, 4,2,9, 0,1,3]
        ])

        solver = Solver(sudoku)
        solver.solve_sudoku()

        solved_sudoku = np.array([
            [1,7,6, 5,8,3, 9,2,4],
            [8,5,9, 2,7,4, 3,6,1],
            [3,4,2, 9,1,6, 5,8,7],

            [7,9,5, 1,4,8, 6,3,2],
            [4,2,3, 6,9,7, 1,5,8],
            [6,8,1, 3,5,2, 7,4,9],

            [9,1,4, 8,3,5, 2,7,6],
            [2,3,8, 7,6,1, 4,9,5],
            [5,6,7, 4,2,9, 8,1,3]
        ])
        assert_array_equal(sudoku, solved_sudoku)

    def testHardSudoku(self):
        sudoku = np.array([
            [0,0,3, 9,0,4, 8,0,0],
            [8,0,0, 0,0,0, 0,0,2],
            [5,1,0, 2,0,3, 0,6,9],

            [1,0,0, 0,0,0, 0,0,7],
            [0,3,0, 7,0,8, 0,9,0],
            [0,0,9, 0,0,0, 5,0,0],

            [9,7,0, 8,0,1, 0,4,3],
            [0,0,0, 0,0,0, 0,0,0],
            [4,2,0, 0,7,0, 0,5,8],
        ])

        solver = Solver(sudoku)
        solver.solve_sudoku()

        solved_sudoku = np.array([
            [2,6,3, 9,1,4, 8,7,5],
            [8,9,4, 5,6,7, 3,1,2],
            [5,1,7, 2,8,3, 4,6,9],

            [1,5,8, 6,4,9, 2,3,7],
            [6,3,2, 7,5,8, 1,9,4],
            [7,4,9, 1,3,2, 5,8,6],

            [9,7,5, 8,2,1, 6,4,3],
            [3,8,6, 4,9,5, 7,2,1],
            [4,2,1, 3,7,6, 9,5,8],
        ])
        assert_array_equal(sudoku, solved_sudoku)

    def testIncorrect4x4Sudoku(self):
        sudoku = np.array([
            [2, 2, 3, 4],
            [0, 0, 0, 0],
            [2, 1, 4, 3],
            [0, 0, 0, 0]
        ])

        pytest.raises(ValueError, Solver, sudoku)

    def testIncorrect4x4Sudoku1(self):
        sudoku = np.array([
            [2, 2, 3, 4],
            [0, 0, 0, 0],
            [0, 1, 4, 3],
            [0, 0, 0, 0]
        ])

        pytest.raises(ValueError, Solver, sudoku)

    def testIncorrectSudokuWithBadValues(self):
        sudoku = np.array([
            [1, 2, 3, 4],
            [0, 0, 0, 0],
            [0, 1, 4, 6],
            [0, 0, 0, 0]
        ])

        pytest.raises(ValueError, Solver, sudoku)
