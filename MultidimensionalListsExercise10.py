size = int(input())
matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "B":
            bunny_row = row
            bunny_col = col
    matrix.append(row_elements)

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        row, col = directions[direction](bunny_row, bunny_col)
    print(f"Direction: {direction}; Sum: {current_sum}")
