#  matrix = [[1,1],[1,2],[1,3]
#           [2,1],[2,2],[2,3]
#           [3,1],[3,2],[3,3]]
# matrix = []
# for i in range(0,3,1):
#     for j in range(0, 3, 1):
#         matrix.append([i+1,j+1])


# print(matrix)


# [[1, 3],[2, 3], [3, 3]
# [1, 2], [2, 2], [3, 2]
# [1, 1], [2, 1], [3, 1]]

# matrix1 = []
dict1 = {}

for column in range(3, 0, -1):
    for row in range(1, 4, 1):
        # matrix1.append([f'{row} {column}'])
        dict1.setdefault(f'{row} {column}', 0)

# print(dict1)

dict1['2 2']= 'X'
# print(dict1)