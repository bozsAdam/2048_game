def welcome_print():
    print('''
    222222222222222         000000000            444444444       888888888
    2:::::::::::::::22     00:::::::::00         4::::::::4     88:::::::::88
    2::::::222222:::::2  00:::::::::::::00      4:::::::::4   88:::::::::::::88
    2222222     2:::::2 0:::::::000:::::::0    4::::44::::4  8::::::88888::::::8
                2:::::2 0::::::0   0::::::0   4::::4 4::::4  8:::::8     8:::::8
                2:::::2 0:::::0     0:::::0  4::::4  4::::4  8:::::8     8:::::8
            2222::::2  0:::::0     0:::::0 4::::4   4::::4   8:::::88888:::::8
        22222::::::22   0:::::0 000 0:::::04::::444444::::444  8:::::::::::::8
    22::::::::222     0:::::0 000 0:::::04::::::::::::::::4 8:::::88888:::::8
    2:::::22222        0:::::0     0:::::04444444444:::::4448:::::8     8:::::8
    2:::::2             0:::::0     0:::::0          4::::4  8:::::8     8:::::8
    2:::::2             0::::::0   0::::::0          4::::4  8:::::8     8:::::8
    2:::::2       2222220:::::::000:::::::0          4::::4  8::::::88888::::::8
    2::::::2222222:::::2 00:::::::::::::00         44::::::44 88:::::::::::::88
    2::::::::::::::::::2   00:::::::::00           4::::::::4   88:::::::::88
    22222222222222222222     000000000             4444444444     888888888 ''', "\n", "\n",
          "                              ", "All the copyrights goes to: Laszlo and Adam")


def game_over_print():
    print('''
    .g8"""bgd       db      `7MMM.     ,MMF'`7MM"""YMM        .g8""8q.`7MMF'   `7MF'`7MM"""YMM  `7MM"""Mq.
    .dP'     `M      ;MM:       MMMb    dPMM    MM    `7      .dP'    `YM.`MA     ,V    MM    `7    MM   `MM.
    dM'       `     ,V^MM.      M YM   ,M MM    MM   d        dM'      `MM VM:   ,V     MM   d      MM   ,M9
    MM             ,M  `MM      M  Mb  M' MM    MMmmMM        MM        MM  MM.  M'     MMmmMM      MMmmdM9
    MM.    `7MMF'  AbmmmqMA     M  YM.P'  MM    MM   Y  ,     MM.      ,MP  `MM A'      MM   Y  ,   MM  YM.
    `Mb.     MM   A'     VML    M  `YM'   MM    MM     ,M     `Mb.    ,dP'   :MM;       MM     ,M   MM   `Mb.
    `"bmmmdPY .AMA.   .AMMA..JML. `'  .JMML..JMMmmmmMMM       `"bmmd"'      VF      .JMMmmmmMMM .JMML. .JMM.''', "\n", "\n", "                           ", "But don't worry, you can always start the game again.")


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
