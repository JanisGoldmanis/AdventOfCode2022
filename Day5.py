def Day5_first_half(debug=True):
    file = open('Day5.txt', 'r')
    values = [line.strip('\n') for line in file]

    column_indexes = 8
    instruction_index = column_indexes + 2
    stacks = values[:column_indexes]
    positions = values[column_indexes]
    instructions = values[instruction_index:]
    stack_count = int(positions[-1])
    max_stack_size = len(stacks)
    stack_list = []
    if debug:
        print("Stacks:", stacks)
        print("Positions:", positions)
        print("Instructions:", instructions)
        print("Count of stacks:", stack_count)
        print("Max stack size in input:", max_stack_size)
    for column in range(stack_count):
        stack = []
        for row in range(max_stack_size):
            try:
                value = stacks[max_stack_size - 1 - row][4 * column + 1]
                if value != ' ':
                    stack.append(stacks[max_stack_size - 1 - row][4 * column + 1])
            except:
                pass
        stack_list.append(stack)
    if debug:
        print("Stack List:", stack_list)

    instruction_lists = []
    for instruction in instructions:
        instruction_list = []
        temp_list = instruction.split(' ')
        instruction_list.append(int(temp_list[1]))
        instruction_list.append(int(temp_list[3]) - 1)
        instruction_list.append(int(temp_list[5]) - 1)
        instruction_lists.append(instruction_list)
    if debug:
        print(instruction_lists)

    for instruction in instruction_lists:
        if debug:
            print("Instruction:", instruction)

        size = instruction[0]
        origin = instruction[1]
        origin_size = len(stack_list[origin])
        target = instruction[2]
        stack_to_move = stack_list[origin][origin_size - size:]
        print("Moving stack before reverse:",stack_to_move)
        stack_to_move=list(reversed(stack_to_move))
        print("Moving stack after reverse:",stack_to_move)
        stack_list[origin] = stack_list[origin][:origin_size - size]
        if debug:
            print("Moving:", stack_to_move)
        for value in range(len(stack_to_move)):
            print(value)
            print(stack_to_move[value])
            stack_list[target].append(stack_to_move[value])
        if debug:
            print("Stacks after moving:")
            for stack in stack_list:
                print(stack)
    result = ''
    for stack in stack_list:
        print(stack)
        result+=stack[-1]
    print(result)

def Day5_second_half(debug=True):
    file = open('Day5.txt', 'r')
    values = [line.strip('\n') for line in file]

    column_indexes = 8
    instruction_index = column_indexes + 2
    stacks = values[:column_indexes]
    positions = values[column_indexes]
    instructions = values[instruction_index:]
    stack_count = int(positions[-1])
    max_stack_size = len(stacks)
    stack_list = []
    if debug:
        print("Stacks:", stacks)
        print("Positions:", positions)
        print("Instructions:", instructions)
        print("Count of stacks:", stack_count)
        print("Max stack size in input:", max_stack_size)
    for column in range(stack_count):
        stack = []
        for row in range(max_stack_size):
            try:
                value = stacks[max_stack_size - 1 - row][4 * column + 1]
                if value != ' ':
                    stack.append(stacks[max_stack_size - 1 - row][4 * column + 1])
            except:
                pass
        stack_list.append(stack)
    if debug:
        print("Stack List:", stack_list)

    instruction_lists = []
    for instruction in instructions:
        instruction_list = []
        temp_list = instruction.split(' ')
        instruction_list.append(int(temp_list[1]))
        instruction_list.append(int(temp_list[3]) - 1)
        instruction_list.append(int(temp_list[5]) - 1)
        instruction_lists.append(instruction_list)
    if debug:
        print(instruction_lists)

    for instruction in instruction_lists:
        if debug:
            print("Instruction:", instruction)

        size = instruction[0]
        origin = instruction[1]
        origin_size = len(stack_list[origin])
        target = instruction[2]
        stack_to_move = stack_list[origin][origin_size - size:]
        stack_list[origin] = stack_list[origin][:origin_size - size]
        if debug:
            print("Moving:", stack_to_move)
        for value in range(len(stack_to_move)):
            print(value)
            print(stack_to_move[value])
            stack_list[target].append(stack_to_move[value])
        if debug:
            print("Stacks after moving:")
            for stack in stack_list:
                print(stack)
    result = ''
    for stack in stack_list:
        print(stack)
        result+=stack[-1]
    print(result)
