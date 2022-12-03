# https://adventofcode.com/2022/day/1

def Day1_first_half():
    """
    """
    f = open('Day1.txt', 'r')
    lines = []
    for l in f:
        lines.append(l.rstrip())
    current_dwarf_calories = 0
    largest_dwarf_calories = 0

    for line in lines:
        if line == "":
            current_dwarf_calories = 0
        else:
            current_dwarf_calories += int(line)
            if current_dwarf_calories > largest_dwarf_calories:
                largest_dwarf_calories = current_dwarf_calories
    print(largest_dwarf_calories)


def Day1_second_half(debug=False):
    """
    """
    f = open('Day1.txt', 'r')
    lines = []
    for l in f:
        lines.append(l.rstrip())
    current_dwarf_calories = 0
    largest_dwarf_calories = []
    largest_dwarf_calories.append(current_dwarf_calories)

    for line in lines:
        if line != "":
            if debug:
                print('Current calories:', current_dwarf_calories)
            current_dwarf_calories += int(line)
            if debug:
                print('Adding', line, 'Current calories:', current_dwarf_calories)
        else:
            if current_dwarf_calories > largest_dwarf_calories[0]:
                if debug:
                    print('New dwarf')
                if len(largest_dwarf_calories) < 3:
                    if debug:
                        print('Appending to list')
                    largest_dwarf_calories.append(current_dwarf_calories)
                    if debug:
                        print('Current list:', largest_dwarf_calories)
                else:
                    if debug:
                        print('Substituting dwarf')
                    largest_dwarf_calories[0] = current_dwarf_calories
                    if debug:
                        print('Current list:', largest_dwarf_calories)

            current_dwarf_calories = 0
            if debug:
                print('Sorting')
            largest_dwarf_calories.sort()
            if debug:
                print('Current list:', largest_dwarf_calories)
    # print(largest_dwarf_calories)
    print(sum(largest_dwarf_calories))
