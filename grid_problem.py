def traverse(rows, columns):
    if rows == 1:
        return 'R'
    elif columns == 1:
        return 'D'

    matrix = [[False for j in range(columns)] for i in range(rows)]
    direction = 'R'
    row = 0
    column = 0
    elements_traversed = []

    while len(elements_traversed) < (rows * columns) - 1:
        elements_traversed.append(matrix[row][column])
        matrix[row][column] = True # Visited

        if direction == 'R':
            if column + 1 == columns or matrix[row][column + 1]: # If reaching the right edge or the next element has been visited
                row += 1 # Move down
                direction = 'D'
            else:
                column += 1 # Move right
        elif direction == 'D':
            if row + 1 == rows or matrix[row + 1][column]: # If reaching the bottom edge or the next element has been visited
                column -= 1 # Move left
                direction = 'L'
            else:
                row += 1 # Move down
        elif direction == 'L':
            if column == 0 or matrix[row][column - 1]: # If reaching the left edge or the next element has been visited
                row -= 1 # Move up
                direction = 'U'
            else:
                column -= 1 # Move left
        else:
            if row == 0 or matrix[row - 1][column]: # If reaching the top edge or the next element has been visited
                column += 1 # Move right
                direction = 'R'
            else:
                row -= 1 # Move up

    return direction


T = int(input())

direction_final = []

for i in range(T):
    N, M = map(int, input().split())
    direction = traverse(N, M)
    direction_final.append(direction)

for i in range(T):
    print(direction_final[i])
