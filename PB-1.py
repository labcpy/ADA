def initialize_board(size):
    return [[0] * size for _ in range(size)]

def print_board(board):
    for row in board:
        print(row)

def is_attack(i, j, board, size):
    # Check if there is a queen in the same row or column
    for k in range(size):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    # Check diagonals
    for k in range(size):
        for l in range(size):
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False

def solve_n_queens(board, n, size):
    if n == 0:
        return True

    for i in range(size):
        for j in range(size):
            if not is_attack(i, j, board, size) and board[i][j] != 1:
                board[i][j] = 1

                if solve_n_queens(board, n - 1, size):
                    return True

                board[i][j] = 0  # Backtrack

    return False

# Example usage:
print("Enter the number of queens")
N = int(input())

# Initialize the chessboard
board = initialize_board(N)

if solve_n_queens(board, N, N):
    print("Solution exists:")
    print_board(board)
else:
    print("Solution does not exist.")