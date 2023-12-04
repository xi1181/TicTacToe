import turtle

turn = 1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
LINE_LEN = 6

EAST, NORTH = 0, 90

L1_X, L1_Y = -3, 1
L2_X, L2_Y = -3, -1
L3_X, L3_Y = -1, -3
L4_X, L4_Y = 1, -3

coordinates = [(L1_X, L1_Y), (L2_X, L2_Y), (L3_X, L3_Y), (L4_X, L4_Y)]
directions = [0, 0, 90, 90]


def main():
    setup()
    screen.onclick(play)
    turtle.mainloop()


def setup():
    global screen, turt
    screen = turtle.getscreen()
    screen.setup(800, 800)
    screen.title("TicTacToe Game")
    screen.setworldcoordinates(-5, -5, 5, 5)
    turt = turtle.getturtle()
    turt.speed("fastest")
    turtle.hideturtle()
    draw_lines()


def draw_lines():
    turt.color("black")
    turt.pensize(10)

    for i in range(4):
        turt.penup()
        turt.goto(coordinates[i])
        turt.seth(directions[i])
        turt.pendown()
        turt.forward(LINE_LEN)


def draw(board):
    draw_lines()
    for row_index in range(3):
        for col_index in range(3):
            draw_move(row_index, col_index, board[row_index][col_index])


def draw_move(row_index, col_index, move):
    if move == 0: return
    intermediate_x = 2 * (col_index - 1)
    intermediate_y = -2 * (row_index - 1)

    if move == 1:
        draw_cross(intermediate_x, intermediate_y)
    else:
        draw_circle(intermediate_x, intermediate_y)


def draw_cross(x, y):
    turtle.color('blue')
    turtle.up()
    turtle.goto(x - 0.75, y - 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y + 0.75)
    turtle.up()
    turtle.goto(x - 0.75, y + 0.75)
    turtle.down()
    turtle.goto(x + 0.75, y - 0.75)
    turtle.up


def draw_circle(x, y):
    turtle.color('red')
    turtle.up()
    turtle.goto(x, y - 0.75)
    turtle.seth(EAST)
    turtle.down()
    turtle.circle(0.75, steps=100)
    turtle.up()


def play(x, y):
    is_first_row = 1 < y and y < 3
    is_second_row = -1 < y and y < 1
    is_third_row = -3 < y and y < -1

    is_first_col = -3 < x and x < -1
    is_second_col = -1 < x and x < 1
    is_third_col = 1 < x and x < 3

    if is_first_row:
        row_index = 0
    elif is_second_row:
        row_index = 1
    elif is_third_row:
        row_index = 2
    else:
        return

    if is_first_col:
        col_index = 0
    elif is_second_col:
        col_index = 1
    elif is_third_col:
        col_index = 2
    else:
        return
    if board[row_index][col_index] != 0:
        return

    global turn
    board[row_index][col_index] = turn
    if turn == 1:
        turn = 2
    else:
        turn = 1

    draw(board)
    outcome = check_outcome(board)

    if outcome == 1:
        screen.textinput("Game Over!", "X won")
    elif outcome == 2:
        screen.textinput("Game Over!", "O won")
    elif outcome == 3:
        screen.textinput("Game Over!", "Tie")


def check_outcome(board):
    if board[0][0] > 0 and board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        return board[0][0]

    if board[1][0] > 0 and board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        return board[1][0]

    if board[2][0] > 0 and board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        return board[2][0]

    if board[0][0] > 0 and board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]

    if board[0][1] > 0 and board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]

    if board[0][2] > 0 and board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[0][2]

    if board[0][0] > 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    if board[2][0] > 0 and board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[2][0]

    if check_tie(board):
        return 3
    else:
        return 0


def check_tie(board):
    for row in range(3):
        for col in range(3):
            if (board[row][col] == 0):
                return False
    return True


if __name__ == "__main__":
    main()