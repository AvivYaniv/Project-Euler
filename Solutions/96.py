from functools import wraps
from time import time

from z3 import *

from itertools import product

def split_to_blocks(line, block_size):
    return [line[i:(i + block_size)] for i in range(0, len(line), block_size)]

class SudokuParser:
    @staticmethod
    def parse_line_digits(line, digits=list(range(1, 10))):
        return [d if d in digits else None for d in [int(x) for x in line] ]
    @staticmethod
    def parse(sudoku_lines):
        return [SudokuParser.parse_line_digits(sudoku_row) for sudoku_row in split_to_blocks(sudoku_lines, 9)]

class SudokuSolver:
    @staticmethod
    def solve(B):
        B = SudokuParser.parse(B) if isinstance(B, str) else B
        s = Solver()
        # Cell variables
        board = [[Int('[{}][{}]'.format(row, col)) for row in range(9)] for col in range(9)]
        # Cell constraints
        for row, col in product(range(9), range(9)):
            s.add(And(board[row][col] > 0, board[row][col] <= 9))
            if B[row][col]:
                s.add(board[row][col] == B[row][col])
        # Row & Col constraints
        for x in range(9):
          s.add(Distinct([board[x][col] for col in range(9)]))
          s.add(Distinct([board[row][x] for row in range(9)]))
        # Group constraints
        for grow, gcol in product(range(3), range(3)):
            s.add(Distinct([board[grow * 3 + row][gcol * 3 + col] for row, col in product(range(3), range(3))]))
        if s.check() == sat:
            return [[s.model()[board[row][col]].as_long() for col in range(9)] for row in range(9)]
        return None
    @staticmethod
    def draw_board(B):
        print('┌───────┬───────┬───────┐')
        for i in range(9):
            if (i in [3, 6]):
                print('├───────┼───────┼───────┤')
            for j in range(9):
                if not j % 3:
                    print('│', end=' ')
                if not B[i][j]:
                    print(' ', end=' ')
                else:
                    print(B[i][j], end=' ')
            print('│')
        print('└───────┴───────┴───────┘')

def measure_time_tresholded_decorator(RUNTIME_THRESHOLD=60):
    def measure_time_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            end = time()
            time_diff = end - start
            if 60 < time_diff:
                print(f'Fails {RUNTIME_THRESHOLD} runtime threshold ({time_diff}s)')
            else:
                print(f'Elapsed time: {time_diff}s')
            return result

        return wrapper

    return measure_time_decorator


# Main
@measure_time_tresholded_decorator()
def main():
    # Read Sudoku file
    sudoku_file_lines = []
    with open('sudoku.txt', 'r') as sudoku_file:
        sudoku_file_lines = sudoku_file.readlines()

    sudoku_file_numeric_lines   = ''.join([line[:9] for line in sudoku_file_lines if not any([c.isalpha() for c in line])])
    sudoku_solutions            = [SudokuSolver.solve(p) for p in split_to_blocks(sudoku_file_numeric_lines, 9**2)]

    # 24702
    result = sum([sum([(10**(3-i-1))*(sudoku_solution[0][i]) for i in range(3)]) for sudoku_solution in sudoku_solutions])
    print(result)

if __name__ == "__main__":
    main()
