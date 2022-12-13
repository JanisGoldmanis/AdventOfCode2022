def Day12_first_half():
    grid = [list(line.rstrip()) for line in open('Day12.txt', 'r')]
    start = [[i, j] for i, line in enumerate(grid) for j, char in enumerate(line) if char == 'S'][0]
    end = [[i, j] for i, line in enumerate(grid) for j, char in enumerate(line) if char == 'E'][0]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    visited = [start]
    steps = 1
    queue = [[start]]
    flag = True
    result = 0
    while len(queue) > 0 and flag:
        next_iteration_queue = []
        current_queue = queue.pop(0)
        for origin in current_queue:
            for pos in directions:
                new = [origin[0] + pos[0], origin[1] + pos[1]]
                if new[0] < 0 or new[1] < 0 or new[0] >= len(grid) or new[1] >= len(grid[0]) or new in visited:
                    continue  # Out of bounds or already visited
                if grid[origin[0]][origin[1]] != 'S':
                    if ord(grid[new[0]][new[1]]) - ord(grid[origin[0]][origin[1]]) > 1:
                        continue  # Too high
                if grid[origin[0]][origin[1]] != 'z' and new[0] == end[0] and new[1] == end[1]:
                    continue  # Adjacent not 'z'
                if new[0] == end[0] and new[1] == end[1]:
                    flag = False
                    result = steps
                    continue
                visited.append(new)
                next_iteration_queue.append(new)
        queue.append(next_iteration_queue)
        steps += 1
    print(flag, result)


def Day12_second_half():
    data = [line.rstrip() for line in open('Day12.txt', 'r')]
    grid = []
    for line in data:
        row = []
        for char in line:
            row.append(char)
        grid.append(row)
    start = -1
    drawing_board = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                start = [i, j]
            row.append('O')
        drawing_board.append(row)
    grid[start[0]][start[1]] = 'z'
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    visited = [start]
    steps = 1
    drawing_board[start[0]][start[1]] = 1
    queue = [[start]]
    flag = True
    result = 0
    while len(queue) > 0 and flag:
        next_iteration_queue = []
        current_queue = queue.pop(0)
        for origin in current_queue:
            for pos in directions:
                new = [origin[0] + pos[0], origin[1] + pos[1]]
                if new[0] < 0 or new[1] < 0 or new[0] >= len(grid) or new[1] >= len(grid[0]) or new in visited:
                    continue
                if grid[origin[0]][origin[1]] != 'S':
                    if ord(grid[origin[0]][origin[1]]) - ord(grid[new[0]][new[1]]) > 1:
                        continue
                if grid[new[0]][new[1]] == 'a':
                    flag = False
                    result = steps
                    continue
                visited.append(new)
                next_iteration_queue.append(new)
                drawing_board[new[0]][new[1]] = steps
        queue.append(next_iteration_queue)
        steps += 1
    print(flag, result)
