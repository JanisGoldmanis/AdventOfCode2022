def day14_first_half():
    data = [line.rstrip() for line in open('Day14.txt', 'r')]
    x = []
    y = []

    for line in data:
        coordinates = line.split(' -> ')
        for coordinate in coordinates:
            x.append(int(coordinate.split(',')[0]))
            y.append(int(coordinate.split(',')[1]))

    min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)

    start = [500 - min_x, 0]

    grid = []

    for line in range(max_y + 1):
        row = []
        for column in range(max_x - min_x + 1):
            row.append('.')
        grid.append(row)

    grid[start[1]][start[0]] = '+'

    def print_grid(grid):
        for index in range(len(grid)):
            print(' ' * (4 - len(str(index))), index, ' ', end='')
            for char in grid[index]:
                print(char, end='')
            print()

    for line in data:
        coordinates = line.split(' -> ')
        for index in range(len(coordinates) - 1):
            x1 = int(coordinates[index].split(',')[0]) - min_x
            y1 = int(coordinates[index].split(',')[1])
            x2 = int(coordinates[index + 1].split(',')[0]) - min_x
            y2 = int(coordinates[index + 1].split(',')[1])
            if x2 < x1:
                x1, x2 = x2, x1
            if y2 < y1:
                y1, y2 = y2, y1
            if x1 - x2 != 0:  # Horizontal
                for num in range(x2 - x1 + 1):
                    grid[y1][x1 + num] = '#'
            if y1 - y2 != 0:  # Vertical
                for num in range(y2 - y1 + 1):
                    grid[y1 + num][x1] = '#'

    print_grid(grid)
    print()
    count = 0

    print_grid(grid)
    print(count - 1)


    while True:
        try:
            count+=1
            current = start.copy()


            while True:

                down = False
                down_left = False
                down_right = False

                if grid[current[1] + 1][current[0]] == '#' or grid[current[1] + 1][current[0]] == 'O':
                    down = True
                if grid[current[1] + 1][current[0] - 1] == '#' or grid[current[1] + 1][current[0] - 1] == 'O':
                    down_left = True
                if grid[current[1] + 1][current[0] + 1] == '#' or grid[current[1] + 1][current[0] + 1] == 'O':
                    down_right = True

                if down and down_left and down_right:
                    grid[current[1]][current[0]] = 'O'
                    break

                elif not down:
                    current[1] += 1
                    continue
                elif down and not down_left:
                    current[0] = current[0] - 1
                    current[1] = current[1] + 1
                    continue
                elif down and not down_right:
                    current[0] = current[0] + 1
                    current[1] = current[1] + 1
                    continue
        except IndexError:
            break



    print_grid(grid)
    print(count - 1)
