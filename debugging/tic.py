#!/usr/bin/python3
def print_board(board):
    """Prints the current state of the 3x3 board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:  # لمنع طباعة الخط السفلي الأخير الزائد
            print("-" * 9)

def check_winner(board):
    """Checks if there is a winner on the board."""
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]  # إرجاع رمز اللاعب الفائز بدلاً من True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]  # إرجاع رمز اللاعب الفائز بدلاً من True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]  # إرجاع رمز اللاعب الفائز بدلاً من True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]  # إرجاع رمز اللاعب الفائز بدلاً من True

    return None

def is_full(board):
    """Checks if the board is completely full (Draw condition)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game loop."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid coordinates! Please enter numbers between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter valid integer numbers.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            
    
            winner = check_winner(board)
            if winner:
                print_board(board)
                print("Player " + winner + " wins!")
                break
                

            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            
            
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
