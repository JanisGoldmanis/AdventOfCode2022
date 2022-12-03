def Day1_first_half():
    file = open('Day2.txt', 'r')
    values = [line.rstrip().replace(' ', '') for line in file]
    dict = {'AX': 4, 'AY': 8, 'AZ': 3, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 7, 'CY': 2, 'CZ': 6}
    print(sum(dict.get(value) for value in values))

def Day2_second_half():
    file = open('Day2.txt', 'r')
    values = [line.rstrip().replace(' ', '') for line in file]
    dict = {'AX': 3, 'AY': 4, 'AZ': 8, 'BX': 1, 'BY': 5, 'BZ': 9, 'CX': 2, 'CY': 6, 'CZ': 7}
    sum(dict.get(value) for value in values)



