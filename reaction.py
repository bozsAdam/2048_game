import random 
import os
import time
import itertools

row_1 = [2,2,2,2]
row_2 = [4,4,4,8]
row_3 = [4,4,4,8]
row_4 = [4,4,4,8]

g = 0
name = ("")
action = 0


current_score = 0

matrix = [row_1,row_2,row_3,row_4]

def print_table():
    p_row_1 = []
    p_row_2 = []
    p_row_3 = []
    p_row_4 = []

    for x in range (0,4):
        p_row_1.append(row_1[x])
        p_row_2.append(row_2[x])
        p_row_3.append(row_3[x])
        p_row_4.append(row_4[x])

    for x in range (0,4):
        if  p_row_1[x] == 0:
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

    print (print_row_1)
    print ("---------------------------------")
    print (print_row_2)
    print ("---------------------------------")
    print (print_row_3)
    print ("---------------------------------")
    print (print_row_4)
    print ("Score = ",current_score)

def w_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for row, column in itertools.product (range(1,4),range(0,4)):
            if matrix[row - 1][column] == 0 and matrix[row][column] != 0:
                matrix[row - 1][column] = matrix[row][column]
                print_table()
                '''
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                '''
                matrix[row][column] = 0
                action += 1
            elif matrix[row - 1][column] == matrix[row][column] and matrix[row - 1][column] != 0 and [row - 1, column] not in occupied_block and [row, column] not in occupied_block:
                matrix[row - 1][column] = matrix[row - 1][column] + matrix[row][column]
                print_table()
                '''
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                '''
                matrix[row][column] = 0
                occupied_block.append([row - 1, column])
                current_score = current_score + matrix[row - 1][column]
                action += 1

        i = i + 1

print_table()
w_reaction()