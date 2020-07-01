import random, time, copy
WIDTH = 60
HEIGHT = 20

# create a list of lists for the cells
next_cells = []

for x in range(WIDTH):
    column = [] # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True: 
    print('\n\n\n\n\n')
    current_cells = copy.deepcopy(next_cells)
    
    # print current cells on sceen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')
        print()

    # calculate next steps
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left_co = (x - 1) % WIDTH
            right_co = (x + 1) % WIDTH
            above_co = (y - 1) % HEIGHT
            below_co = (y + 1) % HEIGHT

            num_neighbors = 0

            if current_cells[left_co][above_co] == '#':
                num_neighbors += 1
            if current_cells[x][above_co] == '#':
                num_neighbors += 1
            if current_cells[right_co][above_co] == '#':
                num_neighbors += 1
            if current_cells[left_co][y] == '#':
                num_neighbors += 1
            if current_cells[right_co][y] == '#':
                num_neighbors += 1
            if current_cells[left_co][below_co] == '#':
                num_neighbors += 1
            if current_cells[x][below_co] == '#':
                num_neighbors += 1
            if current_cells[right_co][below_co] == '#':
                num_neighbors += 1

            if current_cells[x][y] == '#' and num_neighbors in (2, 3):
                # living cells with 2 or 3 neighbors stay alive
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                # dead cells with 3 neighbor come alive
                next_cells[x][y] = '#'
            else:
                # everything else is dead
                next_cells[x][y] = ' '
    time.sleep(1)

