import string
def Day3_first_half():
    file = open('Day3.txt', 'r')
    values = [line.rstrip().replace(' ', '') for line in file]
    print(sum([(string.ascii_lowercase+string.ascii_uppercase).index(char)+1 for line in values for char in set(line[:int(len(line)/2)]) if char in line[int(len(line)/2):]]))


def Day3_second_half():
    file = open('Day3.txt', 'r')
    values = [line.rstrip().replace(' ', '') for line in file]
    print(sum([(string.ascii_lowercase+string.ascii_uppercase).index(char)+1 for i in range(int(len(values)/3)) for char in set(values[i*3]) if char in values[i*3+1] and char in values[i*3+2]]))

