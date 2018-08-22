import time
import os

def welcome_print():
    with open("welcome_print.txt", "r") as opened_txt:
        welcome_print = opened_txt.read()
        print(welcome_print)

def game_over_print():
    with open("game_over_print.txt", "r") as opened_txt:
        game_over_print = opened_txt.read()
        print(game_over_print)


def print_table(row_1, row_2, row_3, row_4, current_score):
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

def table_sleep_print(row_1, row_2, row_3, row_4, current_score):
    print_table(row_1, row_2, row_3, row_4, current_score)
    time.sleep(0.01)
    os.system("cls" if os.name == "nt" else "clear")