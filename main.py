import time
import keyboard

matrica1 = [[0, 2, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 2, 0, 2, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 2, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 0, "@", 0, 0, 0, 0, 0, 0, 0, 0]]


class Menu:

    def printMenu(self):
        print("Приветствую игрока новой игры, в которой нужно доехать до места назначения\n"
              "Автоматический режим - 1\n"
              "Ручной режим - 2\n"
              "Закончить - 3")


a = "@"


def up(matrix, x, y):
    matrix[x][y] = 0
    matrix[x - 1][y] = a
    return matrix


def down(matrix, x, y):
    matrix[x][y] = 0
    matrix[x + 1][y] = a
    return matrix


def right(matrix, x, y):
    matrix[x][y] = 0
    matrix[x][y + 1] = a
    return matrix


def left(matrix, x, y):
    matrix[x][y] = 0
    matrix[x][y - 1] = a
    return matrix


def printMatrix(matrix):
    print()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 3:
                print(matrix[i][j], " ", end="")
        print()
    print()
    # sleep()


def convert(matrix):
    a = []
    for i in range(len(matrix) + 2):
        a.append("3")
    for i in range(len(matrix)):
        matrix[i].append("3")
        matrix[i].insert(0, "3")
    matrix.append(a)
    matrix.insert(0, a)
    return matrix


def sleep():
    time.sleep(0.5)


def auto(matrix):
    xCount = len(matrix) - 1
    yCount = len(matrix[0]) - 1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == a:
                x = i
                y = j
            if matrix[i][j] == 8:
                xEnd = i
                yEnd = j

    while True:
        while matrix[x - 1][y] == 0 and x > 0:
            up(matrix, x, y)
            x -= 1
            printMatrix(matrix)

        while y < yCount and matrix[x - 1][y] != 0 and matrix[x][y + 1] == 0:
            right(matrix, x, y)
            y += 1
            printMatrix(matrix)

        # правый верхний
        if matrix[x - 1][y] != 0 and matrix[x][y + 1] != 0:
            while x < xCount and matrix[x][y + 1] != 0 and matrix[x + 1][y] == 0:
                down(matrix, x, y)
                x += 1
                printMatrix(matrix)
            if matrix[x][y + 1] == 0:
                right(matrix, x, y)
                y += 1
                printMatrix(matrix)
            while matrix[x - 1][y] != 0 and matrix[x][y + 1] == 0:
                right(matrix, x, y)
                y += 1
                printMatrix(matrix)

        if matrix[x][y + 1] != 0 and x == xCount or x < xCount and matrix[x + 1][y] != 0 and matrix[x][y + 1] != 0:
            while matrix[x][y + 1] != 0 and matrix[x - 1][y] == 0 and x > 0:
                up(matrix, x, y)
                x -= 1
                printMatrix(matrix)
            while matrix[x - 1][y] != 0 and matrix[x][y - 1] == 0 and y > 0:
                left(matrix, x, y)
                y -= 1
                printMatrix(matrix)
            while matrix[x][y - 1] != 0 and matrix[x + 1][y] == 0 and x < xCount:
                down(matrix, x, y)
                x += 1
                printMatrix(matrix)
            if matrix[x][y - 1] == 0 and y > 0:
                left(matrix, x, y)
                y -= 1
                printMatrix(matrix)
            while matrix[x - 1][y] != 0 and matrix[x][y - 1] == 0 and y > 0:
                left(matrix, x, y)
                y -= 1
                printMatrix(matrix)

        # проверка на конец
        if x == 0 and y < yEnd:
            while matrix[x][y + 1] == 0:
                right(matrix, x, y)
                y += 1
                printMatrix(matrix)
        elif x == 0 and y > yEnd:
            while matrix[x][y - 1] == 0 or matrix[x][y - 1] == 8:
                left(matrix, x, y)
                y -= 1
                printMatrix(matrix)
                if x == xEnd and y == yEnd:
                    print("Поздравляю, уровень пройден! ")
                    return

        if x == xEnd and y == yEnd:
            print("Поздравляю, уровень пройден! ")
            return


def manual(matrix):
    printMatrix(matrix)
    print("Включен ручной режим игры.\n"
          "Используйте WASD для передвижения")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == a:
                x = i
                y = j
            if matrix[i][j] == 8:
                xEnd = i
                yEnd = j

    while True:
        event = keyboard.read_event()
        moving = ""
        if event.event_type == keyboard.KEY_DOWN:
            moving = event.name
        if moving == "w":
            if matrix[x - 1][y] == 0:
                up(matrix, x, y)
                x -= 1
                printMatrix(matrix)
            elif x - 1 == xEnd and y == yEnd:
                print()
                print("Поздравляю, уровень пройден! ")
                break
            else:
                print("Осторожнее, вы врезались в препятствие")
        elif moving == "a":
            if matrix[x][y - 1] == 0:
                left(matrix, x, y)
                y -= 1
                printMatrix(matrix)
            elif x == xEnd and y - 1 == yEnd:
                print()
                print("Поздравляю, уровень пройден! ")
                break
            else:
                print("Осторожнее, вы врезались в препятствие")
        elif moving == "s":
            if matrix[x + 1][y] == 0:
                down(matrix, x, y)
                x += 1
                printMatrix(matrix)
            elif x + 1 == xEnd and y == yEnd:
                print()
                print("Поздравляю, уровень пройден! ")
                break
            else:
                print("Осторожнее, вы врезались в препятствие")
        elif moving == "d":
            if matrix[x][y + 1] == 0:
                right(matrix, x, y)
                y += 1
                printMatrix(matrix)
            elif x == xEnd and y + 1 == yEnd:
                print()
                print("Поздравляю, уровень пройден! ")
                break
            else:
                print("Осторожнее, вы врезались в препятствие")


menu = Menu()
menu.printMenu()

while True:
    q = int(input())
    if q == 1:
        auto(matrica1)
    elif q == 2:
        manual(matrica1)
    elif q == 3:
        break
