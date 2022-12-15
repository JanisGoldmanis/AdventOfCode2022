import re


def day15_first_half():
    data = [line.rstrip() for line in open('Day15.txt', 'r')]
    beacons, sensors = [], []
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for line in data:
        char_list = list(line)
        numbers = []
        for i in range(4):
            number_string = ""
            while True:
                if len(char_list) == 0:
                    numbers.append(int(number_string))
                    break
                char = char_list.pop(0)
                if (char == ' ' or char == ',') and len(number_string) > 0:
                    numbers.append(int(number_string))
                    break
                if char.isnumeric() or char == '-':
                    number_string += char
        sensor_x = numbers[0]
        sensor_y = numbers[1]
        beacon_x = numbers[2]
        beacon_y = numbers[3]
        sensors.append([sensor_x, sensor_y])
        beacons.append([beacon_x, beacon_y])

    # print('Coordinates')
    # for index in range(len(sensors)):
    #     print(sensors[index], beacons[index])

    distances = []
    for index in range(len(sensors)):
        distance = abs(sensors[index][0] - beacons[index][0]) + abs(sensors[index][1] - beacons[index][1])
        distances.append(distance)

    row = 2000000

    # for index in range(len(sensors)):
    #     sensor = sensors[index]
    #     d = distances[index]
    #     if min_x > sensor[0] - d:
    #         min_x = sensor[0] - d
    #     if max_x < sensor[0] + d:
    #         max_x = sensor[0] + d
    #     if min_y > sensor[1] - d:
    #         min_y = sensor[1] - d
    #     if max_y < sensor[1] + d:
    #         max_y = sensor[1] + d
    # print(min_x, max_x, min_y, max_y)

    # result = 0

    # array = []
    # for num in range(max_x-min_x):
    #     array.append(0)

    # for num in range(max_x-min_x):
    #
    #     x = min_x+num
    #     y = row
    #     for index in range(len(sensors)):
    #         x_s = sensors[index][0]
    #         y_s = sensors[index][1]
    #         d = distances[index]
    #         if (abs(x_s-x)+abs(y_s-y))<=d:
    #             array[num]=1
    # for beacon in beacons:
    #     if beacon[1] == row:
    #         result-=1
    # print(sum(array)+result)

    hidden_zones = []
    for index in range(len(sensors)):
        sensor_x = sensors[index][0]
        sensor_y = sensors[index][1]
        d = distances[index]
        distance_y = abs(row - sensor_y)
        # print(f"Sensor:{sensors[index]},Distance to Row {row} is {distance_y}, Closest beacon: {d}")
        if distance_y < d:
            # print(f"Sensor:{sensors[index]},Distance to Row {row} is {distance_y}, Closest beacon: {d}")
            # print('Adding some zones')
            negative_x = sensor_x - (d - distance_y)
            positive_x = sensor_x + (d - distance_y)
            hidden_zones.append([negative_x, positive_x])

    result = 0
    added_lines = []
    for index in range(len(hidden_zones)):
        interval = hidden_zones.pop(0)
        print(f"Interval: {interval}")
        new_start = interval[0]
        new_end = interval[1]
        for line in added_lines:
            old_start = line[0]
            old_end = line[1]
            if new_start < old_end:
                new_start = old_end
            if new_end > old_start:
                new_end = old_start
        result += new_end - new_start
    print('Result before removing beacons:', result)

    for beacon in beacons:
        if beacon[1] == row:
            result -= 1
    print(result)
