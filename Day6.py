def Day6_first_half():
    file = open('Day6.txt', 'r')
    data = [line.strip('\n') for line in file][0]
    length, result = 4, 0

    for index in range(len(data) - 3):
        i = index + length - 1
        char_list = []
        for data_entry_index in range(length):
            char_list.append(data[i - length + data_entry_index + 1])
        if len(list(set(char_list))) == length:
            print(index + length)
            break


def Day6_second_half():
    file = open('Day6.txt', 'r')
    data = [line.strip('\n') for line in file][0]
    length, result = 14, 0

    for index in range(len(data) - 3):
        i = index + length - 1
        char_list = []
        for data_entry_index in range(length):
            char_list.append(data[i - length + data_entry_index + 1])
        if len(list(set(char_list))) == length:
            print(index + length)
            break
