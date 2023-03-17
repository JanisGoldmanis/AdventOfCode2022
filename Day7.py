class directory:
    def __init__(self, name, parent):
        self.parent_dir = parent
        self.dir_name = name
        self.size = 0
        self.files = []
        self.directories = []

    def __str__(self):
        return self.dir_name

    def print_directories(self):
        result = []
        for directory in self.directories:
            result.append(str(directory))
        return result


def day7_first_half(debug=False):
    file = open('Day7.txt', 'r')
    values = [line.rstrip() for line in file]

    file_structure = directory('/', '-')

    main_folder = file_structure
    current_folder = file_structure
    current_parent = None

    values.pop(0)

    def append_values(current_folder, values):
        while len(values)>0:
            if values[0][0] != '$':
                if values[0][:4] == 'dir ':
                    if debug:
                        print(f'Adding Folder {values[0][4:]}')
                    current_folder.directories.append(directory(values[0][4:], current_folder))
                    if debug:
                        print(f"Current directories: {current_folder.print_directories()}")
                    values.pop(0)
                else:
                    if debug:
                        print(f"Adding file to directory {values[0]}")
                    current_folder.files.append(values.pop(0))
                    if debug:
                        print(f"Current files: {current_folder.files}")
            else:
                if debug:
                    print('Finished Adding files')
                break

    print()
    print(f'Starting generating structure')
    print()

    while len(values)>0:
        action = values.pop(0)
        if debug:
            print(f"Action: {action}")
        if action == "$ ls":
            if debug:
                print(f"Listing and adding directory contents for {current_folder}")
            append_values(current_folder, values)
        elif action == "$ cd ..":
            current_folder = current_parent
            current_parent = current_folder.parent_dir

        elif action[:4] == "$ cd":
            for directory_folder in current_folder.directories:
                if debug:
                    print('Switching directory')
                if directory_folder.dir_name == action[5:]:
                    current_parent = current_folder
                    current_folder = directory_folder

    print()
    print("Structure generated")
    print()

    def calculate_size(folder):
        size = 0
        for directory in folder.directories:
            size += calculate_size(directory)
        for file in folder.files:
            size += int(file.split(' ')[0])
        folder.size = size
        return size

    print('Calculating size')

    calculate_size(file_structure)

    print('Finished calculating size')



    def print_folder(folder, level, score):
        print(f"{' '*level}{folder.dir_name} size: {folder.size}")
        for directory in folder.directories:
            print_folder(directory, level+1, score)
        for file in folder.files:
            print(f"{' '*(level+1)}{file}")

    print_folder(file_structure, 0, 0)

    class Score:
        def __init__(self):
            self.best_score = 80000000

    score = Score()

    def evaluate_folder(folder, score, need_to_delete):
        for directory in folder.directories:
            if debug:
                print(directory)
            size = evaluate_folder(directory, score, need_to_delete)
            if size > need_to_delete and size < score.best_score:
                print(f'Size: {size}, to delete: {need_to_delete}, best score: {score.best_score}')
                score.best_score = size
        return folder.size



    print(f'Total size: {file_structure.size}')
    need_to_delete = abs(70000000 - file_structure.size - 30000000)
    print(f'Need to delete {need_to_delete}')


    # print('Checking size')
    size = evaluate_folder(file_structure, score, need_to_delete)
    # print(f'Size{size}')
    #
    print(f'result: {score.best_score}')










