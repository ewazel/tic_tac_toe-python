def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.'] *3 for i in range(3)]     # board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board

def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0

    while True:
        user_input = input("\nSpecify coordinates of your move on board or 'quit': ")

        if user_input == 'quit':
            raise ValueError("Thank you for the game.\n\n\n")

        else:
            try:
                if len(user_input) != 2:
                    continue
                else:
                    if user_input[0].lower() == "a":
                        row = 0
                    elif user_input[0].lower() == "b":
                        row = 1
                    elif user_input[0].lower() == "c":
                        row = 2
                    else:
                        continue

                    if user_input[1] == "1":
                        col = 0
                    elif user_input[1] == "2":
                        col = 1
                    elif user_input[1] == "3":
                        col = 2
                    else:
                        continue

                    if board[row][col] == '.':
                        break
                    else:
                        continue

            except IndexError:
                continue

    return row, col

def check_for_win(board, player):

    for i in range(len(board)):
        col_win_list = [board[0][i], board[1][i], board[2][i]]
        diag_win_list_1 = [board[0][0], board[1][1], board[2][2]]
        diag_win_list_2 = [board[0][2], board[1][1], board[2][0]]
        diag_win_list_2_rev = [board[2][0], board[1][1], board[0][2]]

        # wygrana w rzędzie
        if board[i].count(player) == 2 and board[i].count('.') == 1:
            row, col = i, board[i].index('.')
            return row, col
        # wygrana w kolumnie
        elif col_win_list.count(player) == 2 and col_win_list.count('.') == 1:
            row, col = col_win_list.index('.'), i
            # print(row, col)
            return row, col
        # wygrana po skosie
        elif (diag_win_list_1.count(player) == 2 and diag_win_list_1.count('.') == 1):
            row, col = diag_win_list_1.index('.'), diag_win_list_1.index('.')
            return row, col
        elif (diag_win_list_2.count(player) == 2 and diag_win_list_2.count('.') == 1):
            row, col = diag_win_list_2.index('.'), diag_win_list_2_rev.index('.')
            return row, col
        else:
            continue

    return None

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    import random
    count = sum(x.count('.') for x in board)

    if player == 'X':
        player_temp = "0"
    elif player == "0":
        player_temp = 'X'

    if count == 0:
        return None
    else:
        # easy win
        if check_for_win(board, player) != None:
            row, col = check_for_win(board, player)
            return row, col
        # print(row, col)

        # prevent easy lose
        elif check_for_win(board, player_temp) != None:
            row, col = check_for_win(board, player_temp)
            return row, col

        else:
        # random move
            while True:
                row, col = random.randint(0, 2), random.randint(0, 2)
                if board[row][col] != '.':
                    continue
                else:
                    return row, col

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""

    try:
        if board[row][col] == '.':
            board[row][col] = player
            return board
    except:
        pass

def has_won(board, player):
    """Returns True if player has won the game."""

    for i in range(len(board)):
        # wygrana w rzędzie
        if board[i] == [player, player, player]:
            return True
        # wygrana w kolumnie
        elif board[0][i] == board[1][i] == board[2][i] == player:
            return True
        # wygrana po skosie
        elif board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            return True
        else:
            continue

    return False

def is_full(board):
    """Returns True if board is full."""
    count = sum(x.count('.') for x in board)

    if count == 0:
        return True
    else:
        return False

def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    rows = ["A", "B", "C"]

    format_num = "{:<3} {:<3} {:<3} {:<3}"
    format_board = "{:<3} {:<2}| {:<2}| {:<2}"

    print('\n')
    print(format_num.format(' ', 1, 2, 3))
    for a, i in zip(rows, board):
        print(format_board.format(a, i[0].center(1, " "), i[1].center(1, " "), i[2].center(1, " ")))
        if rows.index(a) != 2:
            print("   ---+---+---")
    print('\n')

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == 'X':
        print('\nX has won!\n\n')
    elif winner == '0':
        print('\n0 has won!\n\n')
    if winner == 'Noone':
        print("\nIt's a tie!\n\n")

def tictactoe_game(mode='HUMAN-HUMAN'):
    import time

    board = init_board()
    player = '0'
    winner = 'Noone'
    print_board(board)


    while has_won(board, player) == False:

        try:
            if mode == 'AI-HUMAN' and player == '0' or mode == 'HUMAN-AI' and player == 'X' or mode == 'AI-AI':
                row, col = get_ai_move(board, player)
                time.sleep(1)
            else:
                row, col = get_move(board, player)
        except ValueError as error:
            print(error)
            break

        board = mark(board, player, row, col)
        print_board(board)

        if has_won(board, player) == True:
            winner = player
            print_board(board)
            print_result(winner)
            break
        if is_full(board) == True:
            print_result(winner)
            break
        else:
            if player == 'X':
                player = "0"
            elif player == "0":
                player = 'X'

def main_menu():

    user_input = 0

    while user_input != 1 or user_input != 2 or user_input != 3:
        user_input = input('Hello! Please choose which gamemode you want to play: HUMAN vs HUMAN ("1"), HUMAN vs AI ("2") or AI vs AI ("3"). ')

        if user_input == "1":
            tictactoe_game('HUMAN-HUMAN')

        elif user_input == "2":
            user_mark = " "

            while user_mark.lower() != "x" or user_mark != "0":
                user_mark = input('Choose your mark: X or 0. ')
                if user_mark.lower() == "x":
                    tictactoe_game('AI-HUMAN')
                    break
                elif user_mark == "0":
                    tictactoe_game('HUMAN-AI')
                    break
                else:
                    continue

        elif user_input == "3":
            tictactoe_game('AI-AI')
        else:
            continue


if __name__ == '__main__':
    main_menu()