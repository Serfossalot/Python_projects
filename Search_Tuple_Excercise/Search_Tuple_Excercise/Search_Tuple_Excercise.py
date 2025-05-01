def Search(matrix, value):
    locations = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                locations.append((i, j))
    return locations
matrix = (
(1, 2, 3,5,5),
(4, 5, 5,5,),
(7, 8, 9),
(10, 11, 5)
)
value_to_search = 5
result = Search(matrix, value_to_search)
print(f"Locations of {value_to_search}: {result}")

