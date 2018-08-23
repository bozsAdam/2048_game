import random
import os
import time
import itertools
import getch as z
import myprints
import csv


row_1 = [0, 0, 0, 0]
row_2 = [0, 0, 0, 0]
row_3 = [0, 0, 0, 0]
row_4 = [0, 0, 0, 0]

name = ("")
action = 0
current_score = 0
temp_score = 0
matrix = [row_1, row_2, row_3, row_4]
quit = False

# function for saving game as csv file (table, name, score)
def save_the_game():
    with open("save_game.csv", "w", newline='') as save_game_csv:
        thewriter = csv.writer(save_game_csv,delimiter=" ")
        for item in row_1:
            thewriter.writerow(str(item))
        for item in row_2:
            thewriter.writerow(str(item))
        for item in row_3:
            thewriter.writerow(str(item))
        for item in row_4:
            thewriter.writerow(str(item))
        thewriter.writerow(str(current_score))
        thewriter.writerow(name)

# function for continuing from a saved game
def open_save_game(current_score,name):
    opened_rows = []
    with open("save_game.csv", "r") as save_game_csv:
        thereader = csv.reader(save_game_csv)
        thereader = list(thereader)
        for x in range(0, (len(thereader))):
            thereader[x][0] = thereader[x][0].replace(" ","")
            opened_rows.append(thereader[x][0])

    for x in range(0, ((len(opened_rows)-1))):
        opened_rows[x] = int(opened_rows[x])

    opened_row_1 = opened_rows[0:4]
    opened_row_2 = opened_rows[4:8]
    opened_row_3 = opened_rows[8:12]
    opened_row_4 = opened_rows[12:16]
    for x in range(0, 4):
        row_1[x] = opened_row_1[x]
    for x in range(0, 4):
        row_2[x] = opened_row_2[x]
    for x in range(0, 4):
        row_3[x] = opened_row_3[x]
    for x in range(0, 4):
        row_4[x] = opened_row_4[x]
    current_score = opened_rows[16]
    name = opened_rows[17]
    return [current_score,name]

# function for starting with a matrix full of zeroes
def clear_table():
    for x in range(0, 4):
        row_1[x] = 0
        row_2[x] = 0
        row_3[x] = 0
        row_4[x] = 0

# function for saving player name and score in a txt file
def txt_write(name, highscore, current_score):
    
    with open(highscore, "a+") as open_text:
        high_score = str(current_score)
        open_text.write("\n")
        open_text.write(name)
        open_text.write(":")
        open_text.write(high_score)
      
# reading highscore.txt into a dictionary
def read_high_score():
    with open("high_score.txt", 'r') as document:
        highscore_dict = {}
        for line in document:
            if line.strip():  # non-empty line?
                key, value = line.split(':', 1)  # None means 'all whitespace', the default
                highscore_dict[key] = int(value.split()[0])
    return highscore_dict

# function for checking if a name exits in the highscore file
def checking_high_score(name, highscore, current_score):
    if highscore_dict.get(name) < current_score:
        with open(highscore, "r") as r:
            lines = r.readlines()
        with open(highscore, "w") as w:
            for line in lines:
                if name not in line:
                    w.write(line)
        return True

# function for printing highscore dictionary
def print_highscore(dictionary):
    max_length_keys = 2 + max(map(len, dictionary))
    max_length_values = 5 + len(str(max(dictionary.values())))
    for k, v in sorted(dictionary.items(),
                           key=lambda x: x[1], reverse=True):
        print("{:>{max_length_keys}} {:>{max_length_values}}".format(
                k, v, max_length_keys=max_length_keys, max_length_values=max_length_values))

# function for checking game over condition
def check_if_gameover(matrix):

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
        myprints.print_table(row_1, row_2, row_3, row_4, current_score)
        myprints.game_over_print()
        time.sleep(3)
        return True

# generates a 2 or 4 
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

# up movement function
def up_reaction(matrix, action, temp_score):
    i = 0
    occupied_block = []

    while i < 3:
        for row, column in itertools.product(range(1, 4), range(0, 4)):
            if matrix[row - 1][column] == 0 and matrix[row][column] != 0:
                matrix[row - 1][column] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row - 1][column] == matrix[row][column] and matrix[row - 1][column] != 0
                  and [row - 1, column] not in occupied_block and [row, column] not in occupied_block):
                matrix[row - 1][column] = matrix[row -
                                                 1][column] + matrix[row][column]
                matrix[row][column] = 0
                occupied_block.append([row - 1, column])
                temp_score += matrix[row - 1][column]
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action, temp_score]

# down movement function
def down_reaction(matrix, action, temp_score):
    i = 0
    occupied_block = []

    while i < 3:
        for row, column in itertools.product(range(0, 3), range(0, 4)):
            if matrix[row + 1][column] == 0 and matrix[row][column] != 0:
                matrix[row + 1][column] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row + 1][column] == matrix[row][column] and matrix[row + 1][column] != 0
                  and [row + 1, column] not in occupied_block and [row, column] not in occupied_block):
                matrix[row + 1][column] = matrix[row +
                                                 1][column] + matrix[row][column]
                matrix[row][column] = 0
                occupied_block.append([row + 1, column])
                temp_score += matrix[row + 1][column]
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action, temp_score]

# left movement function
def left_reaction(matrix, action, temp_score):
    i = 0
    occupied_block = []

    while i < 3:
        for row, column in itertools.product(range(0, 4), range(1, 4)):
            if matrix[row][column - 1] == 0 and matrix[row][column] != 0:
                matrix[row][column - 1] = matrix[row][column]
                matrix[row][column] = 0
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row][column - 1] == matrix[row][column] and matrix[row][column - 1] != 0
                  and [row, column] not in occupied_block and [row, column - 1] not in occupied_block):
                matrix[row][column - 1] = matrix[row][column - 1] + \
                    matrix[row][column]
                matrix[row][column] = 0
                occupied_block.append([row, column - 1])
                temp_score += matrix[row][column - 1]
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action, temp_score]

# right movement function
def right_reaction(matrix, action, temp_score):
    i = 0
    occupied_block = []

    while i < 3:
        for row, column in itertools.product(range(0, 4), range(0, 3)):
            if matrix[row][3 - column] == 0 and matrix[row][2 - column] != 0:
                matrix[row][3 - column] = matrix[row][2 - column]
                matrix[row][2 - column] = 0
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)
            elif (matrix[row][3 - column] == matrix[row][2 - column] and matrix[row][3 - column] != 0
                  and [row, 3 - column] not in occupied_block and [row, 2 - column] not in occupied_block):
                matrix[row][3 - column] = matrix[row][3 -
                                                      column] + matrix[row][2 - column]
                matrix[row][2 - column] = 0
                occupied_block.append([row, 3 - column])
                temp_score += matrix[row][3 - column]
                action += 1
                myprints.table_sleep_print(
                    row_1, row_2, row_3, row_4, current_score)

        i = i + 1
    return [action, temp_score]



# the main function runs here
while quit is not True:
    os.system("cls" if os.name == "nt" else "clear")
    myprints.welcome_print()
    start_input = input(
        "START THE GAME: any key \nFOR HIGH SCORES: h \nFOR LOADING A SAVED GAME: s \nTO QUIT: q \n")
    if start_input == "q":
        quit = True
    elif start_input == "h":
        os.system("cls" if os.name == "nt" else "clear")
        highscore_dict = read_high_score()
        print_highscore(highscore_dict)
        back_wards = input("Press any key to go back to the main menu:")

    else:
        clear_table()
        number_generator()
        number_generator()
        if start_input == "s":
            save_game_list=open_save_game(current_score,name)
            current_score = save_game_list[0]
            name = save_game_list[1]
        if start_input != "s":
            current_score = 0
            name = input("Please enter your name:")
        input_reader = z.Getch()       
        game_over = False
        os.system("cls" if os.name == "nt" else "clear")
        while game_over is not True:
            action = 0
            myprints.print_table(row_1, row_2, row_3, row_4, current_score)
            print("Please press 'w','a','s' or 'd':")
            user_input = input_reader()
            os.system("cls" if os.name == "nt" else "clear")
            if user_input == "q":
                break
            if user_input == "w":
                result_list = up_reaction(matrix, action, temp_score)
            elif user_input == "s":
                result_list = down_reaction(matrix, action, temp_score)
            elif user_input == "a":
                result_list = left_reaction(matrix, action, temp_score)
            elif user_input == "d":
                result_list = right_reaction(matrix, action, temp_score)
            elif user_input == "o":
                save_the_game()
                break
            else:
                print("Press a valid key")
                continue
            action = result_list[0]
            current_score += result_list[1]

            if action > 0:
                number_generator()
                game_over_save = check_if_gameover(matrix) # checking for end of game
                if game_over_save is True:
                    highscore_dict = read_high_score()
                    if name in dict.keys(highscore_dict): # if a name is already in the highscore list it checks for its score
                        bigger = checking_high_score(name, "high_score.txt", current_score)
                        if bigger is True:
                            txt_write(name,"high_score.txt",current_score)
                    else:
                        txt_write(name,"high_score.txt",current_score)
                    game_over = True
