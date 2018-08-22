import random
import os
import time
import itertools
import getch as z
import myprints
import reaction


row_1 = [2, 2, 2, 2]
row_2 = [4, 4, 4, 8]
row_3 = [4, 4, 4, 8]
row_4 = [4, 4, 4, 8]

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


def w_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for x in range(0, 4):
            if row_1[x] == 0 and row_2[x] != 0:
                row_1[x] = row_2[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                action = action + 1
            elif row_1[x] == row_2[x] and row_1[x] != 0 and [1, x] not in occupied_block and [2, x] not in occupied_block:
                row_1[x] = row_1[x] + row_2[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([1, x])
                current_score = current_score + row_1[x]
                action = action + 1

            if row_2[x] == 0 and row_3[x] != 0:
                row_2[x] = row_3[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                action = action + 1
            elif row_2[x] == row_3[x] and row_2[x] != 0 and [2, x] not in occupied_block and [3, x] not in occupied_block:
                row_2[x] = row_2[x] + row_3[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([2, x])
                current_score = current_score + row_2[x]
                action = action + 1

            if row_3[x] == 0 and row_4[x] != 0:
                row_3[x] = row_4[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                action = action + 1
            elif row_3[x] == row_4[x] and row_3[x] != 0 and [3, x] not in occupied_block and [4, x] not in occupied_block:
                row_3[x] = row_3[x] + row_4[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                occupied_block.append([3, x])
                current_score = current_score + row_3[x]
                action = action + 1

        i = i + 1


def s_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for x in range(0, 4):
            if row_4[x] == 0 and row_3[x] != 0:
                row_4[x] = row_3[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                action = action + 1
            elif row_3[x] == row_4[x] and row_3[x] != 0 and [3, x] not in occupied_block and [4, x] not in occupied_block:
                row_4[x] = row_3[x] + row_4[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([4, x])
                current_score = current_score + row_4[x]
                action = action + 1

            if row_3[x] == 0 and row_2[x] != 0:
                row_3[x] = row_2[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                action = action + 1
            elif row_2[x] == row_3[x] and row_2[x] != 0 and [2, x] not in occupied_block and [3, x] not in occupied_block:
                row_3[x] = row_2[x] + row_3[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([3, x])
                current_score = current_score + row_3[x]
                action = action + 1

            if row_2[x] == 0 and row_1[x] != 0:
                row_2[x] = row_1[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                action = action + 1
            elif row_1[x] == row_2[x] and row_1[x] != 0 and [1, x] not in occupied_block and [2, x] not in occupied_block:
                row_2[x] = row_1[x] + row_2[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                occupied_block.append([2, x])
                current_score = current_score + row_2[x]
                action = action + 1

        i = i + 1


def a_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for x in range(1, 4):
            if row_1[x - 1] == 0 and row_1[x] != 0:
                row_1[x - 1] = row_1[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                action = action + 1
            elif row_1[x - 1] == row_1[x] and row_1[x - 1] != 0 and [1, x] not in occupied_block and [1, x - 1] not in occupied_block:
                row_1[x - 1] = row_1[x - 1] + row_1[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[x] = 0
                occupied_block.append([1, x - 1])
                current_score = current_score + row_1[x - 1]
                action = action + 1

            if row_2[x - 1] == 0 and row_2[x] != 0:
                row_2[x - 1] = row_2[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                action = action + 1
            elif row_2[x - 1] == row_2[x] and row_2[x - 1] != 0 and [2, x] not in occupied_block and [2, x - 1] not in occupied_block:
                row_2[x - 1] = row_2[x - 1] + row_2[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[x] = 0
                occupied_block.append([2, x - 1])
                current_score = current_score + row_2[x - 1]
                action = action + 1

            if row_3[x - 1] == 0 and row_3[x] != 0:
                row_3[x - 1] = row_3[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                action = action + 1
            elif row_3[x - 1] == row_3[x] and row_3[x - 1] != 0 and [3, x] not in occupied_block and [3, x - 1] not in occupied_block:
                row_3[x - 1] = row_3[x - 1] + row_3[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[x] = 0
                occupied_block.append([3, x - 1])
                current_score = current_score + row_3[x - 1]
                action = action + 1

            if row_4[x - 1] == 0 and row_4[x] != 0:
                row_4[x - 1] = row_4[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                action = action + 1
            elif row_4[x - 1] == row_4[x] and row_4[x - 1] != 0 and [4, x] not in occupied_block and [4, x - 1] not in occupied_block:
                row_4[x - 1] = row_4[x - 1] + row_4[x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[x] = 0
                occupied_block.append([4, x - 1])
                current_score = current_score + row_4[x - 1]
                action = action + 1

        i = i + 1


def d_reaction():
    i = 0
    occupied_block = []
    global current_score
    global action
    while i < 3:
        for x in range(0, 3):
            if row_1[3 - x] == 0 and row_1[2 - x] != 0:
                row_1[3 - x] = row_1[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[2 - x] = 0
                action = action + 1
            elif row_1[3 - x] == row_1[2 - x] and row_1[3 - x] != 0 and [1, 3 - x] not in occupied_block and [1, 2 - x] not in occupied_block:
                row_1[3 - x] = row_1[3 - x] + row_1[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_1[2 - x] = 0
                occupied_block.append([1, 3 - x])
                current_score = current_score + row_1[3 - x]
                action = action + 1

            if row_2[3 - x] == 0 and row_2[2 - x] != 0:
                row_2[3 - x] = row_2[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[2 - x] = 0
                action = action + 1
            elif row_2[3 - x] == row_2[2 - x] and row_2[3 - x] != 0 and [2, 2 - x] not in occupied_block and [2, 3 - x] not in occupied_block:
                row_2[3 - x] = row_2[3 - x] + row_2[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_2[2 - x] = 0
                occupied_block.append([2, 3 - x])
                current_score = current_score + row_2[3 - x]
                action = action + 1

            if row_3[3 - x] == 0 and row_3[2 - x] != 0:
                row_3[3 - x] = row_3[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[2 - x] = 0
                action = action + 1
            elif row_3[3 - x] == row_3[2 - x] and row_3[3 - x] != 0 and [3, 2 - x] not in occupied_block and [3, 3 - x] not in occupied_block:
                row_3[3 - x] = row_3[3 - x] + row_3[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_3[2 - x] = 0
                occupied_block.append([3, 3 - x])
                current_score = current_score + row_3[3 - x]
                action = action + 1

            if row_4[3 - x] == 0 and row_4[2 - x] != 0:
                row_4[3 - x] = row_4[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[2 - x] = 0
                action = action + 1
            elif row_4[3 - x] == row_4[2 - x] and row_4[3 - x] != 0 and [4, 2 - x] not in occupied_block and [4, 3 - x] not in occupied_block:
                row_4[3 - x] = row_4[3 - x] + row_4[2 - x]
                myprints.print_table(row_1, row_2, row_3, row_4, current_score)
                time.sleep(0.01)
                os.system("cls" if os.name == "nt" else "clear")
                row_4[2 - x] = 0
                occupied_block.append([4, 3 - x])
                current_score = current_score + row_4[3 - x]
                action = action + 1

        i = i + 1


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
                result_list = reaction.up_reaction(matrix,action,temp_score)
            elif user_input == "s":
                result_list = reaction.down_reaction(matrix,action,temp_score)
            elif user_input == "a":
                result_list = reaction.left_reaction(matrix,action,temp_score)
            elif user_input == "d":
                result_list = reaction.right_reaction(matrix,action,temp_score)
            else:
                print("Press a valid key")
                continue
            action = result_list[0]
            current_score += result_list[1]

            if action > 0:
                number_generator()
                check_if_gameover()
