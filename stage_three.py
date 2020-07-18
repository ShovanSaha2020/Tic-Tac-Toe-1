answer = input("Enter cells: ")
# answer = "XXXOO__O_" # X wins
# answer = "XOXOXOXXO" #X wins
# answer = "XOOOXOXXO" # O wins
# answer = "XOXOOXXXO"  # draw

# answer = "XO_XO_XOX"  # impossible

# answer = "_O_X__X_X"  # impossible
# answer = "_OOOO_X_X"  # impossible

# answer = "XO_OOX_X_"  # game not finished

print("---------")
print(f"| {answer[0]} {answer[1]} {answer[2]} |")
print(f"| {answer[3]} {answer[4]} {answer[5]} |")
print(f"| {answer[6]} {answer[7]} {answer[8]} |")
print("---------")


def is_X_winner():
    if answer[0] == 'X' and answer[1] == 'X' and answer[2] == 'X':
        return True
    if answer[6] == 'X' and answer[7] == 'X' and answer[8] == 'X':
        return True
    if answer[0] == 'X' and answer[3] == 'X' and answer[6] == 'X':
        return True
    if answer[2] == 'X' and answer[5] == 'X' and answer[8] == 'X':
        return True
    if answer[2] == 'X' and answer[4] == 'X' and answer[6] == 'X':
        return True
    if answer[1] == 'X' and answer[4] == 'X' and answer[7] == 'X':
        return True


def is_O_winner():
    if answer[0] == 'O' and answer[1] == 'O' and answer[2] == 'O':
        return True
    if answer[6] == 'O' and answer[7] == 'O' and answer[8] == 'O':
        return True
    if answer[0] == 'O' and answer[3] == 'O' and answer[6] == 'O':
        return True
    if answer[2] == 'O' and answer[5] == 'O' and answer[8] == 'O':
        return True
    if answer[2] == 'O' and answer[4] == 'O' and answer[6] == 'O':
        return True
    if answer[1] == 'O' and answer[4] == 'O' and answer[7] == 'O':
        return True


def empty_cell():
    for element in answer:
        if element == '_':
            return True
    return False


def impossible():
    X_count = 0
    for item in answer:
        if item == 'X':
            X_count = X_count + 1
    O_count = 0
    for item in answer:
        if item == 'O':
            O_count = O_count + 1

    if is_X_winner() and is_O_winner() or abs(X_count - O_count) >= 2:
        return True


if impossible():
    print("Impossible")
else:
    if is_X_winner():
        print("X wins")
    if is_O_winner():
        print("O wins")
    # if empty_cell():
    #     print('empty cells')
    if not is_X_winner() and not is_O_winner() and not empty_cell():
        print("Draw")
    if not is_X_winner() and not is_O_winner() and empty_cell():
        print("Game not finished")
