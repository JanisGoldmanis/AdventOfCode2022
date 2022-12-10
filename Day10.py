def Day10_first_half():
    data = [line.rstrip() for line in open('Day10.txt', 'r')]

    signal = 1
    instructions_array, triggers = [], [19, 59, 99, 139, 179, 219]
    result = 0

    for index in range(len(data)):
        if data[index][:4] == "noop":
            instructions_array.append(0)
        else:
            instructions_array.append(0)
            instructions_array.append(int(data[index].split(' ')[1]))

    for index in range(len(instructions_array)):
        if index in triggers:
            print(index, signal)
            result += (index + 1) * signal
        signal += instructions_array[index]
    print(result)


def Day10_second_half():
    data = [line.rstrip() for line in open('Day10.txt', 'r')]
    sprite_index = 1
    sprite_positions = [0, 1, 2]
    instructions_array = []
    cycle = 1

    for index in range(len(data)):
        if data[index][:4] == "noop":
            instructions_array.append(0)
        else:
            instructions_array.append(0)
            instructions_array.append(int(data[index].split(' ')[1]))

    for row in range(6):
        for index in range(40):
            if cycle-1 in sprite_positions:
                print('#', end='')
            else:
                print('.', end='')
            sprite_index += instructions_array.pop(0)
            sprite_positions = [sprite_index - 1, sprite_index, sprite_index + 1]
            cycle += 1
        cycle -= 40
        print()
