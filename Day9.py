def Day9_first_half(debug=False):
    letters, numbers = zip(
        *[(line.rstrip().split()[0], int(line.rstrip().split()[1])) for line in open('Day9.txt', 'r')])
    U, D, L, R = (-1, 0), (1, 0), (0, -1), (0, 1)
    t_array, h_array = [[1]], [[1]]
    H, T = [0, 0], [0, 0]
    dir_dict = {'U': U, 'D': D, 'L': L, 'R': R}

    def increase_array(m_array, m_direction, T=[], H=[]):
        if m_direction == 'L':
            for line in m_array:
                line.insert(0, 0)
            if len(T) > 0:
                T[1] += 1
                H[1] += 1
        if m_direction == 'R':
            for line in m_array:
                line.append(0)
        if m_direction == 'D':
            m_array.append([0] * len(m_array[0]))
        if m_direction == 'U':
            m_array.insert(0, [0] * len(m_array[0]))
            if len(T) > 0:
                T[0] += 1
                H[0] += 1

    for index in range(len(letters)):
        for num in range(numbers[index]):
            H[0], H[1] = H[0] + dir_dict[letters[index]][0], H[1] + dir_dict[letters[index]][1]
            if H[0] > len(h_array)-1 or H[1] > len(h_array[0]) - 1 or H[1] < 0 or H[0] < 0:  # Array too small
                increase_array(h_array, letters[index], T, H)
                increase_array(t_array, letters[index])
            h_array[H[0]][H[1]] = 1
            if (T[0] != H[0] and T[1] != H[1]) and (abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1):  # Diagonal
                if H[1] - T[1] < 0:
                    T[1] += -1
                else:
                    T[1] += 1
                if H[0] - T[0] < 0:
                    T[0] += -1
                else:
                    T[0] += 1
            else:
                if abs(H[1] - T[1]) > 1:  # Horizontal

                    if H[1] - T[1] < 0:
                        T[1] += -1
                    else:
                        T[1] += +1
                if abs(H[0] - T[0]) > 1:  # Vertical
                    if H[0] - T[0] < 0:
                        T[0] += -1
                    else:
                        T[0] += 1
            t_array[T[0]][T[1]] = 1
    result = sum([number for line in t_array for number in line])
    print(result)

def Day9_second_half(debug=False):
    letters, numbers = zip(
        *[(line.rstrip().split()[0], int(line.rstrip().split()[1])) for line in open('Day9.txt', 'r')])
    U, D, L, R = (-1, 0), (1, 0), (0, -1), (0, 1)
    t_array, h_array = [[1]], [[1]]
    positions = [[0, 0] for i in range(10)]
    dir_dict = {'U': U, 'D': D, 'L': L, 'R': R}

    def increase_array(m_array, m_direction, positions):
        if m_direction == 'L':
            for line in m_array:
                line.insert(0, 0)
            if len(T) > 0:
                for position in positions:
                    position[1] += 1
        if m_direction == 'R':
            for line in m_array:
                line.append(0)
        if m_direction == 'D':
            m_array.append([0] * len(m_array[0]))
        if m_direction == 'U':
            m_array.insert(0, [0] * len(m_array[0]))
            if len(T) > 0:
                for position in positions:
                    position[0] +=1

    for index in range(len(letters)):
        for num in range(numbers[index]):
            for pos_index in range(len(positions)-1):
                H = positions[pos_index]
                T = positions[pos_index+1]
                if pos_index == 0:
                    H[0], H[1] = H[0] + dir_dict[letters[index]][0], H[1] + dir_dict[letters[index]][1]
                if H[0] > len(h_array)-1 or H[1] > len(h_array[0]) - 1 or H[1] < 0 or H[0] < 0:  # Array too small
                    increase_array(h_array, letters[index], positions)
                    increase_array(t_array, letters[index], positions = [])
                h_array[H[0]][H[1]] = 1
                if (T[0] != H[0] and T[1] != H[1]) and (abs(H[1] - T[1]) > 1 or abs(H[0] - T[0]) > 1):  # Diagonal
                    if H[1] - T[1] < 0:
                        T[1] += -1
                    else:
                        T[1] += 1
                    if H[0] - T[0] < 0:
                        T[0] += -1
                    else:
                        T[0] += 1
                else:
                    if abs(H[1] - T[1]) > 1:  # Horizontal

                        if H[1] - T[1] < 0:
                            T[1] += -1
                        else:
                            T[1] += +1
                    if abs(H[0] - T[0]) > 1:  # Vertical
                        if H[0] - T[0] < 0:
                            T[0] += -1
                        else:
                            T[0] += 1
                if pos_index==8:
                    t_array[T[0]][T[1]] = 1
    result = sum([number for line in t_array for number in line])
    print(result)

