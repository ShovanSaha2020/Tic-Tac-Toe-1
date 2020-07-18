dict1 = {}
turn_count = 0


def board(co_ordinates1):
    global dict1
    global turn_count
    for column in range(3, 0, -1):
        for row in range(1, 4, 1):
            dict1.setdefault(f'{row} {column}', '_')

    if turn_count % 2 != 0:
        dict1[co_ordinates1] = 'X'
    elif turn_count % 2 == 0:
        dict1[co_ordinates1] = 'O'
    # [[1, 3],[2, 3], [3, 3]
    # [1, 2], [2, 2], [3, 2]
    # [1, 1], [2, 1], [3, 1]]

    print("---------")
    print(f"| {dict1['1 3']} {dict1['2 3']} {dict1['3 3']} |")
    print(f"| {dict1['1 2']} {dict1['2 2']} {dict1['3 2']} |")
    print(f"| {dict1['1 1']} {dict1['2 1']} {dict1['3 1']} |")
    print("---------")


def cell_occupied(co_ordinates2):
    if dict1.get(co_ordinates2) == 'X' or dict1.get(co_ordinates2) == 'O':
        return True
    elif dict1.get(co_ordinates2) == '_' or dict1.get(co_ordinates2) is None:
        return False


def is_ex_winner():
    try:
        if dict1["1 3"] == 'X' and dict1["2 3"] == 'X' and dict1["3 3"] == 'X':
            return True
        if dict1["1 1"] == 'X' and dict1["2 1"] == 'X' and dict1["3 1"] == 'X':
            return True
        if dict1["1 2"] == 'X' and dict1["2 2"] == 'X' and dict1["3 2"] == 'X':
            return True
        if dict1["1 3"] == 'X' and dict1["1 2"] == 'X' and dict1["1 1"] == 'X':
            return True
        if dict1["3 3"] == 'X' and dict1["3 2"] == 'X' and dict1["3 1"] == 'X':
            return True
        if dict1["2 3"] == 'X' and dict1["2 2"] == 'X' and dict1["2 1"] == 'X':
            return True
        if dict1["1 3"] == 'X' and dict1["2 2"] == 'X' and dict1["3 1"] == 'X':
            return True
        if dict1["1 1"] == 'X' and dict1["2 2"] == 'X' and dict1["3 3"] == 'X':
            return True
    except KeyError:
        pass


def is_zero_winner():
    try:
        if dict1["1 3"] == 'O' and dict1["2 3"] == 'O' and dict1["3 3"] == 'O':
            return True
        if dict1["1 1"] == 'O' and dict1["2 1"] == 'O' and dict1["3 1"] == 'O':
            return True
        if dict1["1 2"] == 'O' and dict1["2 2"] == 'O' and dict1["3 2"] == 'O':
            return True
        if dict1["1 3"] == 'O' and dict1["1 2"] == 'O' and dict1["1 1"] == 'O':
            return True
        if dict1["3 3"] == 'O' and dict1["3 2"] == 'O' and dict1["3 1"] == 'O':
            return True
        if dict1["2 3"] == 'O' and dict1["2 2"] == 'O' and dict1["2 1"] == 'O':
            return True
        if dict1["1 3"] == 'O' and dict1["2 2"] == 'O' and dict1["3 1"] == 'O':
            return True
        if dict1["1 1"] == 'O' and dict1["2 2"] == 'O' and dict1["3 3"] == 'O':
            return True
    except KeyError:
        pass


def empty_cell():
    for value in dict1.values():
        if value == '_':
            return True
    else:
        return False


def tic_tac_toe():
    while True:
        global turn_count
        co_ordinates = input("Enter the coordinates: ")
        co_ordinates_list = co_ordinates.split()
        string_int = ''.join(co_ordinates_list)

        if string_int.isnumeric() is False:
            print("You should enter numbers!")
            continue
        if not (1 <= int(string_int[0]) <= 3 and 1 <= int(string_int[1]) <= 3):
            print("Coordinates should be from 1 to 3!")
            continue
        if cell_occupied(co_ordinates):
            print("This cell is occupied! Choose another one!")
            continue

        turn_count = turn_count + 1
        board(co_ordinates)
        if is_ex_winner():
            print("X wins")
            break
        if is_zero_winner():
            print("O wins")
            break
        # TODO: fix this if clause
        if not is_ex_winner() and not is_zero_winner() and not empty_cell():
            print("Draw")
            break


print("---------")
print(f"| _ _ _ |")
print(f"| _ _ _ |")
print(f"| _ _ _ |")
print("---------")
tic_tac_toe()
