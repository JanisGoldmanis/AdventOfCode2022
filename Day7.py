def day7_first_half(debug=False):
    file = open('Day7Example.txt', 'r')
    values = [line.rstrip() for line in file]
    directory = [0, '/']
    values.pop(0)
    index = 0
    level = 0


    def folder_structure(directory,index):
        print(values[index])
        if values[index][:4] == "$ ls":
            index+=1
            print(values[index])
            while values[index][0] != "$":
                directory.append(values[index])
                index+=1
        return directory,index




    print(folder_structure(directory,index))






