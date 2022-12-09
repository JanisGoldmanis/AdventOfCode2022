import numpy as np


def Day8_first_half():
    file = open('Day8.txt', 'r')
    data = [line.strip('\n') for line in file]

    array = []

    for row in range(len(data)):
        single_row = []
        for column in range(len(data[0])):
            single_row.append(int(data[row][column]))
        array.append(single_row)

    result_array = []
    for num in range(len(array)):
        temp_row = []
        for column in range(len(array)):
            temp_row.append(0)
        result_array.append(temp_row)

    for num in range(4):
        for column in range(len(array[0])):
            current_number = 0
            for row in range(len(array)):
                if row == 0:
                    current_number = array[row][column]
                    result_array[row][column] = 1
                else:
                    if int(array[row][column]) > int(current_number):
                        current_number = array[row][column]
                        result_array[row][column] = 1
        array = np.rot90(array)
        result_array = np.rot90(result_array)

    result = 0
    for row in range(len(result_array)):
        for column in range(len(result_array)):
            result += result_array[row][column]
    print(result)


def Day8_second_half():
    file = open('Day8.txt', 'r')
    data = [line.strip('\n') for line in file]

    array = []

    for row in range(len(data)):
        single_row = []
        for column in range(len(data[0])):
            single_row.append(int(data[row][column]))
        array.append(single_row)

    max_dimension = len(array)

    result = 0

    for column in range(len(array)):
        for row in range(len(array)):
            number = array[row][column]

            offset = 0
            while True:  # right
                if offset + column + 2 > max_dimension:
                    break
                offset += 1
                if array[row][column + offset] >= number:
                    break
            visible_trees_right = offset

            offset = 0
            while True:  # left
                if column - offset - 1 < 0: break
                offset += 1
                if array[row][column - offset] >= number:
                    break
            visible_trees_left = offset

            offset = 0
            while True:  # top
                if row - offset - 1 < 0: break
                offset += 1
                if array[row - offset][column] >= number:
                    break
            visible_trees_top = offset

            offset = 0
            while True:  # bottom
                if row + offset + 2 > max_dimension: break
                offset += 1
                if array[row + offset][column] >= number: break
            visible_trees_bottom = offset

            temp_result = visible_trees_left * visible_trees_right * visible_trees_top * visible_trees_bottom
            if temp_result >= result:
                result = temp_result
    print(result)
