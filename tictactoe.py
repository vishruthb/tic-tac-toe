from IPython.display import clear_output

# Draw the Tic Tac Toe board
def draw_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Get player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Place the marker on the board
def place_marker(board, marker, position):
    board[position] = marker

# Check if the player has won
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

# Check if the space on the board is available
def space_check(board, position):
    return board[position] == ' '

# Check if the board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Get the player's next position
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

# Ask the player if they want to play again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Start the game
print('Welcome to Tic Tac Toe!')

while True:
    # Set up the game
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = 'Player 1'
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    # Start playing the game
    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            draw_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                draw_board(the_board)
                print('Congratulations! Player 1 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
        # Player 2's turn
            draw_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                draw_board(the_board)
                print('Congratulations! Player 2 has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

# Ask the players if they want to play again
    if not replay():
        break

