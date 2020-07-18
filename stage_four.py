def is_cell_empty(element):
    if element == '_':
        return True
    else:
        return False


def position(pos):
    if pos == '1 3':
        return answer[0]
    if pos == '2 3':
        return answer[1]
    if pos == '3 3':
        return answer[2]
    if pos == '1 2':
        return answer[3]
    if pos == '2 2':
        return answer[4]
    if pos == '3 2':
        return answer[5]
    if pos == '1 1':
        return answer[6]
    if pos == '2 1':
        return answer[7]
    if pos == '3 1':
        return answer[8]


def updated_game():
    if co_ordinates == '1 1':
        print("---------")
        print(f"| {answer[0]} {answer[1]} {answer[2]} |")
        print(f"| {answer[3]} {answer[4]} {answer[5]} |")
        print(f"| X {answer[7]} {answer[8]} |")
        print("---------")

    if co_ordinates == '2 1':
        print("---------")
        print(f"| {answer[0]} {answer[1]} {answer[2]} |")
        print(f"| {answer[3]} {answer[4]} {answer[5]} |")
        print(f"| {answer[6]} X {answer[8]} |")
        print("---------")

    if co_ordinates == '3 1':
        print("---------")
        print(f"| {answer[0]} {answer[1]} {answer[2]} |")
        print(f"| {answer[3]} {answer[4]} {answer[5]} |")
        print(f"| {answer[6]} {answer[7]} X |")
        print("---------")

    if co_ordinates == '1 2':
        print("---------")
        print(f"| {answer[0]} {answer[1]} {answer[2]} |")
        print(f"| X {answer[4]} {answer[5]} |")
        print(f"| {answer[6]} {answer[7]} {answer[8]} |")
        print("---------")

    if co_ordinates == '2 2':
        print("---------")
        print(f"| {answer[0]} {answer[1]} {answer[2]} |")
        print(f"| {answer[3]} X {answer[5]} |")
        print(f"| {answer[6]} {answer[7]} {answer[8]} |")
        print("---------")

    if co_ordinates == '3 2':
        print("---------")
        print(f"| {answer[0]} {answer[1]} {answer[2]} |")
        print(f"| {answer[3]} {answer[4]} X |")
        print(f"| {answer[6]} {answer[7]} {answer[8]} |")
        print("---------")

    if co_ordinates == '1 3':
        print("---------")
        print(f"| X {answer[1]} {answer[2]} |")
        print(f"| {answer[3]} {answer[4]} {answer[5]} |")
        print(f"| {answer[6]} {answer[7]} {answer[8]} |")
        print("---------")

    if co_ordinates == '2 3':
        print("---------")
        print(f"| {answer[0]} X {answer[2]} |")
        print(f"| {answer[3]} {answer[4]} {answer[5]} |")
        print(f"| {answer[6]} {answer[7]} {answer[8]} |")
        print("---------")

    if co_ordinates == '3 3':
        print("---------")
        print(f"| {answer[0]} {answer[1]} X |")
        print(f"| {answer[3]} {answer[4]} {answer[5]} |")
        print(f"| {answer[6]} {answer[7]} {answer[8]} |")
        print("---------")


# ----------------------------------------------------------------------------------
answer = input("Enter cells: ")

# answer = "_XXOO_OX_"

print("---------")
print(f"| {answer[0]} {answer[1]} {answer[2]} |")
print(f"| {answer[3]} {answer[4]} {answer[5]} |")
print(f"| {answer[6]} {answer[7]} {answer[8]} |")
print("---------")

# 1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)

# TODO fix and test this mess
active = True
while active:
    co_ordinates = input("Enter the coordinates: ")
    co_ordinates_list = co_ordinates.split()
    string_int = ''.join(co_ordinates_list)

    if string_int.isnumeric() is False:
        # print(string_int.isnumeric())
        print("You should enter numbers!")
        continue

    if not (1 <= int(string_int[0]) <= 3 and 1 <= int(string_int[1]) <= 3):
        print("Coordinates should be from 1 to 3!")
        continue

    if is_cell_empty(position(co_ordinates)) is False:
        # print(position(co_ordinates))
        # print(is_cell_empty(position(co_ordinates)))
        print("This cell is occupied! Choose another one!")
        continue

    else:
        updated_game()
        break
