def Day11_first_half():
    class Monkey:
        def __init__(self, items, operation, test, true_target, false_target):
            self.items = items
            self.operation = operation
            self.test = test
            self.true_target = true_target
            self.false_target = false_target
            self.inspected = 0

    data = [line.rstrip() for line in open('Day10.txt', 'r')]

    signal = 1
    instructions_array, triggers = [], [19, 59, 99, 139, 179, 219]
    result = 0
    #Test
