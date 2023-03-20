import random

# Draw the Tic Tac Toe board
def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# Get player input
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Do you want to be X or O? ').upper()

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

# AI makes a random move
def random_move(board, marker):
    available_moves = []
    for i in range(1, 10):
        if space_check(board, i):
            available_moves.append(i)

    if available_moves:
        return random.choice(available_moves)
    else:
        return None

# AI makes an intelligent move
def intelligent_move(board, marker):
    for i in range(1, 10):
        if space_check(board, i):
            board[i] = marker
            if win_check(board, marker):
                return i
            else:
                board[i] = ' '

    for i in range(1, 10):
        if space_check(board, i):
            board[i] = player1_marker
            if win_check(board, player1_marker):
                return i
            else:
                board[i] = ' '

    for i in [5, 1, 3, 7, 9, 2, 4, 6, 8]:
        if space_check(board, i):
            return i
    return random_move(board, marker)

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

def play_game():
    print('Welcome to Tic Tac Toe!')


while True:
    # Set up the game
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    # Play the game
    game_on = True
    while game_on:
        if turn == 'Player 1':
            # Player 1's turn
            draw_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                draw_board(the_board)
                print('Congratulations! You have won the game!')
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
            position = intelligent_move(the_board, player2_marker)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                draw_board(the_board)
                print('The AI has won the game!')
                game_on = False
            else:
                if full_board_check(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'Player 1'

    # Ask the player if they want to play again
    if not replay():
        break

play_game()
