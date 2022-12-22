def day18_first_half():
    class cube:
        def __init__(self, coordinate_list):
            self.x = int(coordinate_list[0])
            self.y = int(coordinate_list[1])
            self.z = int(coordinate_list[2])

            self.top = 0
            self.bottom = 0
            self.N = 0
            self.S = 0
            self.W = 0
            self.E = 0

            self.free = 6

    cube_list = []

    data = [line.rstrip() for line in open('Day18.txt', 'r')]
    for line in data:
        cube_list.append(cube(line.split(',')))

    max_x = 0
    max_y = 0
    max_z = 0

    for cube in cube_list:
        if max_x < cube.x:
            max_x = cube.x
        if max_y < cube.y:
            max_y = cube.y
        if max_z < cube.z:
            max_z = cube.z
    # print(max_x, max_y, max_z, 'Array size:', max_x * max_y * max_z)

    array = []

    for level in range(max_z + 2):
        single_level = []
        for row in range(max_y + 2):
            single_row = []
            for column in range(max_x + 2):
                single_row.append(0)
            single_level.append(single_row)
        array.append(single_level)

    for cube in cube_list:
        x = cube.x
        y = cube.y
        z = cube.z

        array[z][y][x] = 1

    def print_array(array):
        for level in array:
            for row in level:
                print(row)
            print()

    # print_array(array)

    result = 0

    for cube in cube_list:
        x = cube.x
        y = cube.y
        z = cube.z

        # TOP
        if array[z + 1][y][x] == 1:
            cube.top = 1
            cube.free -= 1
        # BOT
        if array[z - 1][y][x] == 1:
            cube.bottom = 1
            cube.free -= 1

        # N
        if array[z][y - 1][x] == 1:
            cube.N = 1
            cube.free -= 1

        # S
        if array[z][y + 1][x] == 1:
            cube.S = 1
            cube.free -= 1

        # W
        if array[z][y][x - 1] == 1:
            cube.W = 1
            cube.free -= 1

        # E
        if array[z][y][x + 1] == 1:
            cube.E = 1
            cube.free -= 1

        result += cube.free

    print(result)



