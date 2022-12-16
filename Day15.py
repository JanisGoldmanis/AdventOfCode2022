def day15_first_half():
    data = [line.rstrip() for line in open('Day15.txt', 'r')]
    beacons, sensors = [], []
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

    distances = []
    for index in range(len(sensors)):
        distance = abs(sensors[index][0] - beacons[index][0]) + abs(sensors[index][1] - beacons[index][1])
        distances.append(distance)

    row = 2000000

    hidden_zones = []
    for index in range(len(sensors)):
        sensor_x = sensors[index][0]
        sensor_y = sensors[index][1]
        d = distances[index]
        distance_y = abs(row - sensor_y)
        if distance_y < d:
            negative_x = sensor_x - (d - distance_y)
            positive_x = sensor_x + (d - distance_y)
            hidden_zones.append([negative_x, positive_x])

    result = 0

    while True:
        flag = False
        for index in range(len(hidden_zones) - 1):
            first = hidden_zones[index]
            second = hidden_zones[index + 1]
            if first[0] > second[0]:
                hidden_zones[index] = second
                hidden_zones[index + 1] = first
                flag = True
                break
        if not flag:
            break

    last_position = -5000000
    for index in range(len(hidden_zones)):
        interval = hidden_zones.pop(0)
        new_start = interval[0] - 1
        new_end = interval[1]
        if new_start < last_position:
            new_start = last_position
        if new_end < last_position:
            continue
        result += new_end - new_start
        last_position = new_end

    beacon_set = set()
    for beacon in beacons:
        beacon_set.add((beacon[0], beacon[1]))
    for beacon in beacon_set:
        if beacon[1] == row:
            result -= 1
    print(result)
