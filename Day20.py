def day20_first_half():
    data = [int(line.rstrip()) for line in open('Day20.txt', 'r')]

    # print('Original data:', data)

    result_list = data[:]

    for num in data:
        # print('Number:', num, 'Current result:', result_list)
        index = result_list.index(num)

        if num >= 1 and num + index < len(result_list) + 1:
            # print('Positive w/o mod')
            result_list.pop(index)
            result_list.insert(index + num, num)
            # print(result_list)

        if num < 0 and num + index < 1:
            # print('Negative w/ wrap')
            result_list.pop(index)
            result_list.insert(index + num + len(result_list), num)
            # print(result_list)

        if num >= 1 and num + index > len(result_list) + 1:
            # print('Positive w/ wrap')
            result_list.pop(index)
            result_list.insert(index + num - len(result_list), num)
            # print(result_list)

        if num < 0 and num + index >= 1:
            # print('Negative w/o wrap')
            result_list.pop(index)
            result_list.insert(index + num, num)
            # print(result_list)

    index = result_list.index(0)
    first = result_list[(1000 + index) % len(result_list)]
    second = result_list[(2000 + index) % len(result_list)]
    third = result_list[(3000 + index) % len(result_list)]

    print(first, second, third)

    print(first + second + third)

    # if index+num > len(result_list):
    #     index = (index+num) % len(result_list)
    # else:
    #     index = index+num

    # result_list.insert(index, num)
    # print(result_list)
