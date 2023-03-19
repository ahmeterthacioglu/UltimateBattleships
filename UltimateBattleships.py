# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = False  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

    player1_board = [['-' for i in range(board_size)] for j in range(board_size)]
    player2_board = [['-' for i in range(board_size)] for j in range(board_size)]
    fakeboard1 = [['-' for i in range(board_size)] for j in range(board_size)]
    fakeboard2 = [['-' for i in range(board_size)] for j in range(board_size)]
    fakelist1 = [player1_board,fakeboard2]
    fakelist2 = [fakeboard1,player2_board]
    my_list = [player1_board, player2_board]
    #print_3d_list(my_list)
    for u in range(2):
        #if u == 1:
        #    print_3d_list(fakelist2)
        #ship_list = ['Carrier','Battleship','Cruiser','Submarine','Destroyer']
        ship_length = dict()
        ship_length['Carrier'] = 5
        ship_length['Battleship'] = 4
        ship_length['Cruiser'] = 3
        ship_length['Submarine'] = 3
        ship_length['Destroyer'] = 2
        # print_ships_to_be_placed()
        # for i in ship_length.keys():
        # print(i,end=' ')

        temp_list = []

        m = True
        while m:
            if u == 0:
                print_3d_list(fakelist1)
            if u == 1:
                print_3d_list(fakelist2)
            print_ships_to_be_placed()
            #print_single_element(ship_list)
            for i in ship_length.keys():
                print(i, end=' ')
            print_empty_line()
            print_player_turn_to_place(u+1)
            print_to_place_ships()
            while True:
                x = input()
                x = x.split()

                shipName = x[0]
                shipName = shipName.lower()
                shipName = shipName.capitalize()

                if len(x) >= 4:
                    number1 = x[1]
                    number2 = x[2]
                    try:
                        int(x[1]) and int(x[2])
                        break
                    except:
                        print_incorrect_input_format()
                        if u == 0:
                            print_3d_list(fakelist1)
                        else:
                            print_3d_list(fakelist2)
                        print_ships_to_be_placed()
                        for i in ship_length.keys():
                            print(i, end=' ')
                        print_empty_line()
                        print_player_turn_to_place(u + 1)
                        print_to_place_ships()
                        continue
                else:
                    print_incorrect_input_format()
                    break
            if len(x) >= 4:
                if 0 < int(number1) < 11 and 0 < int(number2) < 11:
                    if shipName in ship_length.keys() or shipName in temp_list:
                        if x[3] == 'h' or x[3] == 'v' or x[3] == 'H' or x[3] == 'V':
                            if x[3] == 'h' or x[3] == 'H':
                                if shipName not in temp_list:
                                    if int(number1) + ship_length[shipName] <= 11:
                                        if '#' not in my_list[u][int(number2) - 1][int(number1) - 1:int(number1) + ship_length[shipName]-1]:
                                            for i in range(ship_length[shipName]):
                                                my_list[u][int(number2) - 1][int(number1) - 1 + i] = '#'
                                            ship_length.pop(shipName)
                                            temp_list.append(shipName)


                                            if len(ship_length) < 1:
                                                if u == 0:
                                                    print_3d_list(fakelist1)
                                                else:
                                                    print_3d_list(fakelist2)
                                                n = True
                                                while n:
                                                    print_confirm_placement()
                                                    a = input()
                                                    if a == 'Y' or a == 'y' :
                                                        m = False
                                                        break
                                                    elif a == 'N' or a == 'n':
                                                        if u == 0:
                                                            player1_board = [['-' for i in range(board_size)] for j in
                                                                         range(board_size)]
                                                        if u ==1:
                                                            player2_board = [['-' for i in range(board_size)] for j in
                                                                         range(board_size)]
                                                        fakeboard1 = [['-' for i in range(board_size)] for j in
                                                                      range(board_size)]
                                                        fakeboard2 = [['-' for i in range(board_size)] for j in
                                                                      range(board_size)]
                                                        fakelist1 = [player1_board, fakeboard2]
                                                        fakelist2 = [fakeboard1, player2_board]
                                                        my_list = [player1_board, player2_board]
                                                        ship_length = dict()
                                                        ship_length['Carrier'] = 5
                                                        ship_length['Battleship'] = 4
                                                        ship_length['Cruiser'] = 3
                                                        ship_length['Submarine'] = 3
                                                        ship_length['Destroyer'] = 2
                                                        temp_list = []
                                                        #print_3d_list(my_list)

                                                        n = False
                                                        continue
                                                    else:
                                                        continue
                                        else:
                                            print_ship_cannot_be_placed_occupied(shipName)
                                    else:
                                        print_ship_cannot_be_placed_outside(shipName)
                                else:
                                    print_ship_is_already_placed(shipName)

                            elif x[3] == 'v' or x == 'V':
                                if shipName not in temp_list:
                                    if int(number2) + ship_length[shipName] <= 11:
                                        for i in range(ship_length[shipName]):
                                            if my_list[u][int(number2) - 1 + i][int(number1) - 1] == '#':
                                                print_ship_cannot_be_placed_occupied(shipName)
                                                break
                                                # m = True
                                                # continue

                                        for i in range(ship_length[shipName]):
                                            my_list[u][int(number2) - 1 + i][int(number1) - 1] = '#'
                                        # if '#' not in my_list[u][int(number2) - 1:int(number2) -1+ship_length[shipName][int(number1) - 1]:
                                        #     for i in range(ship_length[shipName]):
                                        #         my_list[u][int(number2) - 1 + i][int(number1) - 1] = '#'
                                        ship_length.pop(shipName)
                                        temp_list.append(shipName)


                                        if len(ship_length) < 1:
                                            if u == 0:
                                                print_3d_list(fakelist1)
                                            else:
                                                print_3d_list(fakelist2)
                                            n = True
                                            while n:
                                                print_confirm_placement()
                                                a = input()
                                                if a == 'Y' or a == 'y':
                                                    m = False
                                                    break
                                                elif a == 'N' or a == 'n':
                                                    player1_board = [['-' for i in range(board_size)] for j in
                                                                     range(board_size)]
                                                    player2_board = [['-' for i in range(board_size)] for j in
                                                                     range(board_size)]
                                                    fakeboard1 = [['-' for i in range(board_size)] for j in
                                                                  range(board_size)]
                                                    fakeboard2 = [['-' for i in range(board_size)] for j in
                                                                  range(board_size)]
                                                    fakelist1 = [player1_board, fakeboard2]
                                                    fakelist2 = [fakeboard1, player2_board]
                                                    my_list = [player1_board, player2_board]
                                                    ship_length = dict()
                                                    ship_length['Carrier'] = 5
                                                    ship_length['Battleship'] = 4
                                                    ship_length['Cruiser'] = 3
                                                    ship_length['Submarine'] = 3
                                                    ship_length['Destroyer'] = 2
                                                    temp_list = []
                                                    # print_3d_list(my_list)

                                                    n = False
                                                    continue
                                                else:
                                                    continue
                                        #
                                        # else:
                                        #     print_ship_cannot_be_placed_occupied(shipName)
                                    else:
                                        print_ship_cannot_be_placed_outside(shipName)
                                else:
                                    print_ship_is_already_placed(shipName)
                        else:
                            print_incorrect_orientation()
                    else:
                        print_incorrect_ship_name()
                else:
                    print_ship_cannot_be_placed_outside(shipName)



    #print_3d_list(my_list)
    l1 = True
    while l1:
        for u1 in range(2):


            while u1 == 0:
                print_3d_list(fakelist1)
                print_player_turn_to_strike(1)
                print_choose_target_coordinates()
                s = input()
                s = s.split()
                if len(s) >= 2:
                    number3 = s[0]
                    number4 = s[1]
                    try:
                        int(s[0]) and int(s[1])
                    except:
                        print_incorrect_input_format()
                        continue
                else:
                    print_incorrect_input_format()
                    continue
                if len(s) >= 2:
                    if 0< int(number3) < 11 and 0< int(number4) < 11:
                        if '#' in my_list[1][int(number4)-1][int(number3)-1]:
                            print_hit()
                            fakelist1[1][int(number4)-1][int(number3)-1] = '!'
                            my_list[1][int(number4)-1][int(number3)-1] = '!'
                            # print_3d_list(fakelist1)
                            if sum(x.count('!') for x in fakelist1[1]) == 17:
                                print_3d_list(fakelist1)
                                print_player_won(1)
                                l1 = False
                                break
                            else:
                                continue
                        elif '-' in my_list[1][int(number4)-1][int(number3)-1]:
                            print_miss()
                            fakelist1[1][int(number4)-1][int(number3)-1] = 'O'
                            my_list[1][int(number4)-1][int(number3)-1] = 'O'
                            print_3d_list(fakelist1)
                            while True:
                                print_type_done_to_yield(1)
                                r = input()
                                r = r.lower()
                                if r == 'done':
                                    break
                                else:
                                    continue
                            break
                        elif 'O' or '!' in my_list[1][int(number4)-1][int(number3)-1]:
                            print_tile_already_struck()
                            #print_3d_list(fakelist1)
                            continue
                    else:
                        print_incorrect_coordinates()
                else:
                    print_incorrect_input_format()
            if sum(x.count('!') for x in fakelist1[1]) == 17:
                l1 = False
                break



            while u1 == 1:
                print_3d_list(fakelist2)
                print_player_turn_to_strike(2)
                print_choose_target_coordinates()
                s = input()
                s = s.split()

                if len(s) >= 2:
                    number3 = s[0]
                    number4 = s[1]
                    try:
                        int(s[0]) and int(s[1])
                    except:
                        print_incorrect_input_format()
                        continue
                else:
                    print_incorrect_input_format()
                    continue
                if len(s) >= 2:
                    if 0 < int(number3) < 11 and 0 < int(number4) < 11:
                        if '#' in my_list[0][int(number4)-1][int(number3)-1]:
                            print_hit()
                            fakelist2[0][int(number4)-1][int(number3)-1] = '!'
                            my_list[0][int(number4)-1][int(number3)-1] = '!'
                            #print_3d_list(fakelist2)
                            if sum(x.count('!') for x in fakelist2[0]) == 17:
                                print_3d_list(fakelist2)
                                print_player_won(2)
                                l1 = False
                                break
                            else:
                                continue
                        elif '-' in my_list[0][int(number4)-1][int(number3)-1]:
                            print_miss()
                            fakelist2[0][int(number4)-1][int(number3)-1] = 'O'
                            my_list[0][int(number4)-1][int(number3)-1] = 'O'
                            print_3d_list(fakelist2)
                            while True:
                                print_type_done_to_yield(2)
                                r = input()
                                r = r.lower()
                                if r == 'done':
                                    break
                                else:
                                    continue

                            break
                        elif 'O' or '!' in my_list[0][int(number4)-1][int(number3)-1]:
                            print_tile_already_struck()
                            continue
                    else:
                        print_incorrect_coordinates()
                else:
                    print_incorrect_input_format()
            if sum(x.count('!') for x in fakelist2[1]) == 17:
                l1 = False
    print_thanks_for_playing()





    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()



