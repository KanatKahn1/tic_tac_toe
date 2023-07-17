import random


def print_board(board):

    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + ' | '.join(row) + ' |')


def game():
    board = [' ' for i in range(9)]
    counter = 0
    turn = 'X'
    print_board(board)
    print('Welcome, please choose number from 0 to 8   ')
    for i in range(10):
        if win(counter, board, turn):
            print(f'{turn} победитель!')
            return 'Endgame'
        available_moves = [i for i, v in enumerate(board) if v == " "]
        user_pos = int(input('Your turn(0-8):'))
        opponent = int(random.choice(available_moves))
        if board[user_pos] == ' ':
            board[user_pos] = 'X'
            available_moves.pop(user_pos)
            board[opponent] = 'O'
            available_moves.pop(opponent)
            counter += 2
            print_board(board)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
def win(counter, board, turn):
    if counter >= 5:
        if board[0] == board[1] == board[2]:
            return True
        elif board[3] == board[4] == board[5]:
            return True
        elif board[6] == board[7] == board[8]:
            return True
        #строки
        elif board[0] == board[3] == board[6]:
            return True
        elif board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[5] == board[8]:

            return True
        # столбцы

        elif all([board[i] == turn for i in (0, 4, 8)]):
            return True
        elif all ([board[i] == turn for i in (2,4,6)]):
            return True
        #диогонали
        else:
         return False
game()