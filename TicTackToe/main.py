ValuesInPosition = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
WinningPosition = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def check(ch, name):
    for i in WinningPosition:
        if ValuesInPosition[i[0]] == ValuesInPosition[i[1]] == ValuesInPosition[i[2]] == ch:
            print(f"{ValuesInPosition[1]} | {ValuesInPosition[2]} | {ValuesInPosition[3]}\n{ValuesInPosition[4]} | {ValuesInPosition[5]} | {ValuesInPosition[6]}\n{ValuesInPosition[7]} | {ValuesInPosition[8]} | {ValuesInPosition[9]}")
            print(f"{name} winner")
            exit()
    if ValuesInPosition[1] != " " and ValuesInPosition[2] != " " and ValuesInPosition[3] != " " and ValuesInPosition[
        4] != " " and ValuesInPosition[5] != " " and ValuesInPosition[6] != " " and ValuesInPosition[7] != " " and \
            ValuesInPosition[8] != " " and ValuesInPosition[9] != " ":
        print("DRAW")
        exit()


def player2input(position, ch, name):
    if ValuesInPosition[position] == " ":
        ValuesInPosition[position] = ch
    else:
        print("already filled")

    check(ch, name)
    print(f"{ValuesInPosition[1]} | {ValuesInPosition[2]} | {ValuesInPosition[3]}\n{ValuesInPosition[4]} | {ValuesInPosition[5]} | {ValuesInPosition[6]}\n{ValuesInPosition[7]} | {ValuesInPosition[8]} | {ValuesInPosition[9]}")


def player1input(position, ch, name):
    if ValuesInPosition[position] == " ":
        ValuesInPosition[position] = ch
    else:
        print("already filled")

    check(ch, name)
    print(f"{ValuesInPosition[1]} | {ValuesInPosition[2]} | {ValuesInPosition[3]}\n{ValuesInPosition[4]} | {ValuesInPosition[5]} | {ValuesInPosition[6]}\n{ValuesInPosition[7]} | {ValuesInPosition[8]} | {ValuesInPosition[9]}")


if __name__ == '__main__':
    print("-------------Instruction---------------")
    print("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9")
    print("always enter the position and ur choice charector whether it is X or O")

    player1Name = input("enter the name of first player")
    player2Name = input("enter the name of second player")

    while True:
        p = int(input("enter the position"))
        ch = input("X or O").lower()
        player1input(p, ch, player1Name)

        p = int(input("enter the position"))
        ch = input("X or O").lower()
        player2input(p, ch, player2Name)


    print("DRAW")
