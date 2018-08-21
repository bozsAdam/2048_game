import random
import os
import time
import itertools

row_1 = [2, 0, 0, 2]
row_2 = [0, 0, 0, 2]
row_3 = [4, 4, 4, 2]
row_4 = [4, 4, 4, 4]

g = 0
name = ("")
action = 0


current_score = 0

matrix = [row_1, row_2, row_3, row_4]

def table_sleep_print():
    print_table()
    time.sleep(0.01)
    os.system("cls" if os.name == "nt" else "clear")

def print_table():
    p_row_1 = []
    p_row_2 = []
    p_row_3 = []
    p_row_4 = []

    for x in range(0, 4):
        p_row_1.append(row_1[x])
        p_row_2.append(row_2[x])
        p_row_3.append(row_3[x])
        p_row_4.append(row_4[x])

    for x in range(0, 4):
        if p_row_1[x] == 0:
            p_row_1[x] = ""
        if p_row_2[x] == 0:
            p_row_2[x] = ""
        if p_row_3[x] == 0:
            p_row_3[x] = ""
        if p_row_4[x] == 0:
            p_row_4[x] = ""

    print_row_1 = "  | ".join('{:4}'.format(item) for item in p_row_1)
    print_row_2 = "  | ".join('{:4}'.format(item) for item in p_row_2)
    print_row_3 = "  | ".join('{:4}'.format(item) for item in p_row_3)
    print_row_4 = "  | ".join('{:4}'.format(item) for item in p_row_4)

    print(print_row_1)
    print("---------------------------------")
    print(print_row_2)
    print("---------------------------------")
    print(print_row_3)
    print("---------------------------------")
    print(print_row_4)
    print("Score = ", current_score)


def up_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for row, column in itertools.product(range(1, 4), range(0, 4)):
            if matrix[row - 1][column] == 0 and matrix[row][column] != 0:
                matrix[row - 1][column] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                table_sleep_print()
            elif (matrix[row - 1][column] == matrix[row][column] and matrix[row - 1][column] != 0 
                and [row - 1, column] not in occupied_block and [row, column] not in occupied_block):
                    matrix[row - 1][column] = matrix[row - 1][column] + matrix[row][column]
                    matrix[row][column] = 0
                    occupied_block.append([row - 1, column])
                    current_score = current_score + matrix[row - 1][column]
                    action += 1
                    table_sleep_print()

        i = i + 1


def down_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for row, column in itertools.product(range(0, 3), range(0, 4)):
            if matrix[row + 1][column] == 0 and matrix[row][column] != 0:
                matrix[row + 1][column] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                table_sleep_print()
            elif (matrix[row + 1][column] == matrix[row][column] and matrix[row + 1][column] != 0 
                and [row + 1, column] not in occupied_block and [row, column] not in occupied_block):
                        matrix[row + 1][column] = matrix[row + 1][column] + matrix[row][column]
                        matrix[row][column] = 0
                        occupied_block.append([row + 1, column])
                        current_score = current_score + matrix[row + 1][column]
                        action += 1
                        table_sleep_print()

        i = i + 1


def right_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for row, column in itertools.product(range(0, 4), range(1, 4)):
            if matrix[row][column - 1] == 0 and matrix[row][column] !=0:
                matrix[row][column - 1] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                table_sleep_print()
            elif (matrix[row][column - 1] == matrix[row][column] and matrix[row][column - 1] != 0 
                and [row, column] not in occupied_block and [row, column - 1] not in occupied_block):
                    matrix[row][column - 1] = matrix[row][column - 1] + matrix[row][column]
                    matrix[row][column] = 0
                    occupied_block.append([row, column - 1])
                    current_score = current_score + matrix[row][column - 1]
                    action += 1
                    table_sleep_print()

        i = i + 1


def left_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for row, column in itertools.product(range(0, 4), range(0, 3)):
            if matrix[row][3 - column] == 0 and matrix[row][2 - column] !=0:
                matrix[row][3 - column] = matrix[row][2 - column]
                matrix[row][2 - column] = 0
                action += 1
                table_sleep_print()
            elif (matrix[row][3 - column] == matrix[row][2 - column] and matrix[row][3 - column] != 0 
                and [row, 3 - column] not in occupied_block and [row, 2 - column] not in occupied_block):
                    matrix[row][3 - column] = matrix[row][3 - column] + matrix[row][2 - column]
                    matrix[row][2 - column] = 0
                    occupied_block.append([row, 3 - column])
                    current_score = current_score + matrix[row][3 - column]
                    action += 1
                    table_sleep_print()

        i = i + 1
'''
print_table()
d_reaction()
print_table()
print(action)
print(matrix[-3][-3])
'''