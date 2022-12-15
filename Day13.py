import json


def Day13_first_half():
    data = [json.loads(line.rstrip()) for line in open('Day13Example.txt', 'r') if len(line.rstrip()) > 0]
    result = 0

    def to_list(number):
        return [number]

    def equality(list1, list2):
        while True:
            try:
                print(f"List1 len={len(list1)},List2 len={len(list2)}")
                if len(list1) == 0 and len(list2) == 0:
                    return True
                elif len(list1) == 0:
                    return True

                value_2 = list2.pop(0)
                value_1 = list1.pop(0)

                print(f"Value1: {value_1}, Value2: {value_2}")

                if isinstance(value_1, list) and isinstance(value_2, list):
                    if not equality(value_1, value_2):
                        return False
                elif (isinstance(value_1, list) and not isinstance(value_2, list)) or (
                        not isinstance(value_1, list) and isinstance(value_2, list)):
                    if not isinstance(value_1, list):
                        if not equality(to_list(value_1), value_2):
                            return False
                    if not isinstance(value_2, list):
                        if not equality(value_1, to_list(value_2)):
                            return False

                elif value_1 > value_2:
                    return False

            except IndexError:
                print('Index Error')
                if len(list2) == 0 and value_1 < value_2:
                    print(value_1, value_2)
                    return True
                elif len(list1) == 0:
                    print('List1 len = 0')
                    return True
                else:
                    print('Returning false')
                    return False

    print(equality(data[0], data[1]), '= True?')
    print(equality(data[2], data[3]), '= True?')
    print(equality(data[4], data[5]), ' = False?')
    print(equality(data[6], data[7]), '= True?')
    print(equality(data[8], data[9]), '= False?')
    print(equality(data[10], data[11]), '= True?')
    print(equality(data[12], data[13]), '= False?')

    # try:
    #     if isinstance(list1[index], list) and isinstance(list2[index], list):
    #         if not equality(list1[index], list2[index]):
    #             return False
    #     elif index > len(list1):
    #         return False
    #     elif (isinstance(list1[index], list) and not isinstance(list2[index], list)) or (
    #             not isinstance(list1[index], list) and isinstance(list2[index], list)):
    #         if not isinstance(list1[index], list):
    #             if not equality(to_list(list1[index]), list2[index]):
    #                 return False
    #         if not isinstance(list2[index], list):
    #             if not equality(list1[index], to_list(list2[index])):
    #                 return False
    #     elif list1[index] > list2[index]:
    #         return False
    # except IndexError:
    #     if len(list2) > len(list1):
    #         return True
    #     if len(list2) == 0:
    #         return False
    #     elif list2[index - 1] > list1[index - 1]:
    #         return True
    #     return False
    # return True

    # print(equality(data[2], data[3]))

    # for index in range(int(len(data) / 2)):
    #     # print()
    #     # print(f"Index {index + 1}")
    #     if equality(data[index * 2], data[index * 2 + 1]):
    #         # print(f"Index {index + 1} is True")
    #         result += index + 1
    # print(result)
