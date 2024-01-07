import numpy as np
import pytest
from sudoku_solver.solver import Solver

class TestSolver():
    def testIncorrectSudoku(self):
        sudoku = np.array([
            [1, 2, 3, 4],
            [5, 6 ,7 ,8]
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
