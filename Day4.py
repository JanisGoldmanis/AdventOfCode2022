def Day4_first_half(debug=False):
    file = open('Day4.txt', 'r')
    values = [line.rstrip().replace(' ', '').split(',') for line in file]
    list1, list2 = [], []
    for row in values:
        list1.append(row[0].split('-'))
        list2.append(row[1].split('-'))

    for i in range(len(list1)):
        for j in range(2):
            list1[i][j] = int(list1[i][j])
    for i in range(len(list1)):
        for j in range(2):
            list2[i][j] = int(list2[i][j])

    sum = 0
    if debug:
        print("Values: ", values)
        print("List1: ", list1)
        print("List2: ", list2)
    for index in range(len(list1)):
        if debug:
            print(list1[index][0], list1[index][1], " and ", list2[index][0], list2[index][1])
        if list1[index][0] >= list2[index][0] and list1[index][1] <= list2[index][1]:
            if debug:
                print("First within Second")
            sum += 1
        elif list1[index][0] <= list2[index][0] and list1[index][1] >= list2[index][1]:
            sum += 1
            if debug:
                print("Second within First")
        else:
            if debug:
                print("Not included")
        if debug:
            print(sum)

    # bit_array_list_1 = []
    # for interval in list1:
    #     bit_array = []
    #     for num in range(100):
    #         if num < interval[0]:
    #             bit_array.append(0)
    #         elif num >= interval[0] and num <= interval[1]:
    #             bit_array.append[1]
    #         else:
    #             bit_array.append(0)
    #     bit_array_list_1.append(bit_array)
    #
    # bit_array_list_2 = []
    # for interval in list2:
    #     bit_array = []
    #     for num in range(100):
    #         if num < interval[0]:
    #             bit_array.append(0)
    #         elif num >= interval[0] and num <= interval[1]:
    #             bit_array.append[1]
    #         else:
    #             bit_array.append(0)
    #     bit_array_list_2.append(bit_array)
    #
    # for index in range(len(list1)):
    #     print(bit_array_list_1[index])
    #     print(bit_array_list_2[index])
    #     print()

    print(sum)


def Day4_second_half(debug=False):
    file = open('Day4.txt', 'r')
    values = [line.rstrip().replace(' ', '').split(',') for line in file]
    list1, list2 = [], []
    for row in values:
        list1.append(row[0].split('-'))
        list2.append(row[1].split('-'))

    for i in range(len(list1)):
        for j in range(2):
            list1[i][j] = int(list1[i][j])
    for i in range(len(list1)):
        for j in range(2):
            list2[i][j] = int(list2[i][j])

    sum = 0
    if debug:
        print("Values: ", values)
        print("List1: ", list1)
        print("List2: ", list2)
    for index in range(len(list1)):
        if debug:
            print(list1[index][0], list1[index][1], " and ", list2[index][0], list2[index][1])
        if (list1[index][0] >= list2[index][0] and list1[index][0] <= list2[index][1]) or (
                list1[index][0] <= list2[index][0] <= list1[index][1]):
            if debug:
                print("First within Second")
            sum += 1
        elif (list1[index][1] >= list2[index][0] and list1[index][1] <= list2[index][1]) or (
                list1[index][0] <= list2[index][1] <= list1[index][1]):
            sum += 1
            if debug:
                print("Second within First")
        else:
            if debug:
                print("Not included")
        if debug:
            print(sum)
    print(sum)
