def sky_diff(M):

    memo = []
    for index_of_a_row in range(len(M)):
        max_of_a_row = max(M[index_of_a_row])
        column_numbers = []
        for row_index in range(len(M)):
            column_numbers.append(M[row_index][index_of_a_row])
        min_of_column = min(column_numbers)
        memo.append((max_of_a_row, min_of_column))

    for i in range(len(memo)):
        print(memo[i][0]-memo[0][1], memo[i][0]-memo[1][1],memo[i][0]-memo[2][1])

matrix = [
    [4, 1, 8],
    [5, 2, 5],
    [9, 7, 1]
]
sky_diff(matrix)


