start = [["", "", ""], ["", "", ""], ["", "", ""]]

matrix = start[:]


def draw():
    for r, mat in enumerate(matrix):
        for i, ch in enumerate(mat):
            if ch == "":
                print(" ", end="")
            else:
                print(ch, end="")
            if i == 2:
                break
            print(" | ", end="")
        print()
        if r == 2:
            break
        print("--|---|--")


def validation(n):
    try:
        num = int(n)
    except ValueError:
        return validation(input("Please enter a valid number between 1 to 9 "))
    return num


def update(i, p):
    if p == 1:
        ch = "X"
    else:
        ch = "O"
    if i == 1:
        if matrix[0][0] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[0][0] = ch
        return check(0, 0)
    elif i == 2:
        if matrix[0][1] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[0][1] = ch
        return check(0, 1)
    elif i == 3:
        if matrix[0][2] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[0][2] = ch
        return check(0, 2)
    elif i == 4:
        if matrix[1][0] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[1][0] = ch
        return check(1, 0)
    elif i == 5:
        if matrix[1][1] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[1][1] = ch
        return check(1, 1)
    elif i == 6:
        if matrix[1][2] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[1][2] = ch
        return check(1, 2)
    elif i == 7:
        if matrix[2][0] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[2][0] = ch
        return check(2, 0)
    elif i == 8:
        if matrix[2][1] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[2][1] = ch
        return check(2, 1)
    elif i == 9:
        if matrix[2][2] != "":
            return update(int(input("invalid input please enter again ")), p)
        matrix[2][2] = ch
        return check(2, 2)
    else:
        return update(int(input("invalid input please enter again ")), p)


def check(r, c):
    if matrix[r][0] == matrix[r][1] == matrix[r][2]:
        return True
    if matrix[0][c] == matrix[1][c] == matrix[2][c]:
        return True
    if r == c:
        if matrix[0][0] == matrix[1][1] == matrix[2][2]:
            return True
    if r + c == 2:
        if matrix[0][2] == matrix[1][1] == matrix[2][0]:
            return True
    return False


def play():
    draw()
    for i in range(5):
        n = validation(input("\nPlayer1 - X enter number "))
        isWinner = update(n, 1)
        draw()
        if isWinner:
            print("\nWon Player1 ")
            break
        if i == 4:
            print("Draw Game!!")
            break
        n = validation(input("\nPlayer2 - O enter number "))
        isWinner = update(n, 2)
        draw()
        if isWinner:
            print("\nWon Player2 ")
            break


while True:
    print("                          ** Welcome to Tic Tac Toe **  \n")
    print(
        """RULES:- 1. Please enter any number between 1 to 9
        2. Player1 having symbol "X"
        3. Player2 having symbol "O" \n"""
    )
    matrix = [["", "", ""], ["", "", ""], ["", "", ""]]
    play()
    if input("Wanna restart a game(Y/N): ") == "N":
        print("                            Thank You!")
        break
