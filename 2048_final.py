import random
import os
import time
import itertools
import getch as z
import myprints


row_1 = [2, 16, 2, 0]
row_2 = [4, 8, 4, 0]
row_3 = [8, 4, 8, 0]
row_4 = [16, 2, 16, 0]

g = 0
name = ("")
action = 0


current_score = 0
temp_score = 0
matrix = [row_1, row_2, row_3, row_4]

def read_high_score():
    with open("high_score.txt", "r") as opened_file:
        outprinted_txt = opened_file.read()
        print(outprinted_txt)


def txt_save():
    with open("high_score.txt", "a+") as open_text:
        high_score = str(current_score)
        open_text.write("\n")
        open_text.write(name)
        open_text.write(":")
        open_text.write(high_score)


def clear_table():
    for x in range(0, 4):
        row_1[x] = 0
        row_2[x] = 0
        row_3[x] = 0
        row_4[x] = 0


def check_if_gameover():

    matrix = [row_1, row_2, row_3, row_4]
    check_zero = []
    for x in range(0, 4):
        check_zero.append(row_1[x])
        check_zero.append(row_2[x])
        check_zero.append(row_3[x])
        check_zero.append(row_4[x])

    gameover_value = 0

    for x, y in itertools.product(range(0, 4), range(1, 4)):
        if matrix[x][y] == matrix[x][y - 1]:
            gameover_value = gameover_value + 1
        if matrix[y][x] == matrix[y - 1][x]:
            gameover_value = gameover_value + 1
    if gameover_value == 0 and 0 not in check_zero:
        txt_save()
        myprints.print_table(row_1, row_2, row_3, row_4, current_score)
        myprints.game_over_print()
        time.sleep(3)
        global g
        g = g + 1


def number_generator():
    nulls_places = [[], [], [], []]

    for x in range(0, 4):
        if row_1[x] == 0:
            nulls_places[0].append(x)
        if row_2[x] == 0:
            nulls_places[1].append(x)
        if row_3[x] == 0:
            nulls_places[2].append(x)
        if row_4[x] == 0:
            nulls_places[3].append(x)
    temp_nulls = []

    for x in range(0, 4):
        if len(nulls_places[x]) != 0:
            temp_nulls.append(x)
    n_temp_nulls = len(temp_nulls)

    if n_temp_nulls > 0:
        random_row = random.choice(temp_nulls)
        two_or_four = [2, 4]
        if random_row == 0:
            rand_1 = random.choice(nulls_places[0])
            row_1[rand_1] = random.choice(two_or_four)
        elif random_row == 1:
            rand_2 = random.choice(nulls_places[1])
            row_2[rand_2] = random.choice(two_or_four)
        elif random_row == 2:
            rand_3 = random.choice(nulls_places[2])
            row_3[rand_3] = random.choice(two_or_four)
        elif random_row == 3:
            rand_4 = random.choice(nulls_places[3])
            row_4[rand_4] = random.choice(two_or_four)

def up_reaction(matrix,action,temp_score):
    i = 0
    occupied_block = []
    
    while i < 3:
        for row, column in itertools.product(range(1, 4), range(0, 4)):
            if matrix[row - 1][column] == 0 and matrix[row][column] != 0:
                matrix[row - 1][column] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row - 1][column] == matrix[row][column] and matrix[row - 1][column] != 0 
                and [row - 1, column] not in occupied_block and [row, column] not in occupied_block):
                    matrix[row - 1][column] = matrix[row - 1][column] + matrix[row][column]
                    matrix[row][column] = 0
                    occupied_block.append([row - 1, column])
                    temp_score +=  matrix[row - 1][column]
                    action += 1
                    myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action,temp_score]


def down_reaction(matrix,action,temp_score):
    i = 0
    occupied_block = []
    
    while i < 3:
        for row, column in itertools.product(range(0, 3), range(0, 4)):
            if matrix[row + 1][column] == 0 and matrix[row][column] != 0:
                matrix[row + 1][column] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row + 1][column] == matrix[row][column] and matrix[row + 1][column] != 0 
                and [row + 1, column] not in occupied_block and [row, column] not in occupied_block):
                        matrix[row + 1][column] = matrix[row + 1][column] + matrix[row][column]
                        matrix[row][column] = 0
                        occupied_block.append([row + 1, column])
                        temp_score += matrix[row + 1][column]
                        action += 1
                        myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action,temp_score]


def left_reaction(matrix,action,temp_score):
    i = 0
    occupied_block = []
   
    while i < 3:
        for row, column in itertools.product(range(0, 4), range(1, 4)):
            if matrix[row][column - 1] == 0 and matrix[row][column] !=0:
                matrix[row][column - 1] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row][column - 1] == matrix[row][column] and matrix[row][column - 1] != 0 
                and [row, column] not in occupied_block and [row, column - 1] not in occupied_block):
                    matrix[row][column - 1] = matrix[row][column - 1] + matrix[row][column]
                    matrix[row][column] = 0
                    occupied_block.append([row, column - 1])
                    temp_score += matrix[row][column - 1]
                    action += 1
                    myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action,temp_score]


def right_reaction(matrix,action,temp_score):
    i = 0
    occupied_block = []
  
    while i < 3:
        for row, column in itertools.product(range(0, 4), range(0, 3)):
            if matrix[row][3 - column] == 0 and matrix[row][2 - column] !=0:
                matrix[row][3 - column] = matrix[row][2 - column]
                matrix[row][2 - column] = 0
                action += 1
                myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row][3 - column] == matrix[row][2 - column] and matrix[row][3 - column] != 0 
                and [row, 3 - column] not in occupied_block and [row, 2 - column] not in occupied_block):
                    matrix[row][3 - column] = matrix[row][3 - column] + matrix[row][2 - column]
                    matrix[row][2 - column] = 0
                    occupied_block.append([row, 3 - column])
                    temp_score += matrix[row][3 - column]
                    action += 1
                    myprints.table_sleep_print(row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action,temp_score]


q = 0

while q < 1:
    os.system("cls" if os.name == "nt" else "clear")
    myprints.welcome_print()
    start_input = input(
        "Press 'h' for high scores, 'q' to quit or any other key to begin:")
    if start_input == "q":
        q = q + 1
    elif start_input == "h":
        read_high_score()
        back_wards = input("Press any key to go back to the main menu:")

    else:
        input_reader = z.Getch()
        name = input("Please enter your name:")
        clear_table()
        number_generator()
        number_generator()
        current_score = 0
        g = 0
        os.system("cls" if os.name == "nt" else "clear")
        while g < 1:
            action = 0
            myprints.print_table(row_1, row_2, row_3, row_4, current_score)
            print("Please press 'w','a','s' or 'd':")
            user_input = input_reader()
            os.system("cls" if os.name == "nt" else "clear")
            if user_input == "q":
                break
            if user_input == "w":
                result_list = up_reaction(matrix,action,temp_score)
            elif user_input == "s":
                result_list = down_reaction(matrix,action,temp_score)
            elif user_input == "a":
                result_list = left_reaction(matrix,action,temp_score)
            elif user_input == "d":
                result_list = right_reaction(matrix,action,temp_score)
            else:
                print("Press a valid key")
                continue
            action = result_list[0]
            current_score += result_list[1]

            if action > 0:
                number_generator()
                check_if_gameover()
