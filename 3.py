def get_user_board():
    print("Enter the board row by row (use X, O, or space):")
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            while True:
                val = input(f"Enter cell ({i+1},{j+1}): ").upper()
                if val in ['X', 'O', ' ']:
                    row.append(val)
                    break
                else:
                    print("Invalid input! Use 'X', 'O', or space.")
        board.append(row)
    return board

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("---+---+---")


user_board = get_user_board()
print("\nTic-Tac-Toe Board:")
print_board(user_board)