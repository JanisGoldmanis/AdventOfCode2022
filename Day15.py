import re


def day15_first_half():
    data = [line.rstrip() for line in open('Day15Example.txt', 'r')]
    beacons, sensors = [], []

    for line in data:
        numbers = []
        char_list = list(line)

        for i in range(4):
            number_string = ""
            while True:
                if len(char_list) == 0:
                    break

                char = char_list.pop(0)
                if char == ' ':
                    break
                if char.isnumeric() or char == '-':
                    number_string += char
            numbers.append(int(number_string))
            sensor_x = numbers[0]
            sensor_y = numbers[1]
            beacon_x = numbers[2]
            beacon_y = numbers[3]
            sensors.append([sensor_x, sensor_y])
            beacons.append([beacon_x, beacon_y])
    for index in range(len(sensors)):
        print(sensors[index], beacons[index])
