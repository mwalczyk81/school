def is_valid(board, row, col, num):
    """
    Determine if it's valid to place 'num' at position (row, col) on the Sudoku board.
    Implement the necessary checks.
    """
    # Check if the same number exists in the same row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the same number exists in the same column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the same number exists in the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    # If the number doesn't violate any Sudoku rules, it's valid
    return True

def solve_sudoku(board):
    """
    Solve the provided Sudoku board using backtracking.
    Fill in the solution directly into the board.
    Return True if a solution exists, otherwise return False.
    """
    # Find an empty cell
    empty_cell = find_empty_cell(board)
    
    # If no empty cells left on the board, the Sudoku is solved
    if not empty_cell:
        return True
    
    row, col = empty_cell
    
    # Try placing numbers 1 to 9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # Place the number if it's valid
            board[row][col] = num
            
            # Recursively try to solve the Sudoku
            if solve_sudoku(board):
                return True
            
            # If no solution is found, backtrack
            board[row][col] = 0
    
    # If no number works, backtrack
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

if __name__ == "__main__":
    import sys

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py <input_file>")
        sys.exit(1)

    # Read Sudoku board from the input file
    input_file = sys.argv[1]
    with open(input_file, "r") as file:
        sudoku_board = [[int(num) for num in line.split()] for line in file.readlines()]

    print("Input Sudoku Board:")
    for row in sudoku_board:
        print(" ".join(map(str, row)))

    # Solve the Sudoku board
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku Board:")
        for row in sudoku_board:
            print(" ".join(map(str, row)))
    else:
        print("\nNo solution exists.")
