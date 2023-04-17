# Игровая доска
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

# Игроки
player1 = "X"
player2 = "O"

def print_board(board):
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")

def check_winner(board):
    # Горизонтальные комбинации
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True

    # Вертикальные комбинации
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True

    # Диагональные комбинации
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True

    return False

current_player = player1

while True:
    # Выводим игровое поле
    print_board(board)

    # Предлагаем игроку сделать ход
    move = input("Ход игрока " + current_player + " (1-9): ")

    # Проверяем корректность ввода
    if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
        # Делаем ход
        board[int(move)-1] = current_player

        # Проверяем, есть ли победитель
        if check_winner(board):
            print_board(board)
            print("Игрок", current_player, "победил!")
            break

        # Меняем игрока
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
    else:
        print("Неверный ход. Попробуйте еще раз.")

