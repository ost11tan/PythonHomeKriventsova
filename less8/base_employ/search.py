def Search_Entry(file,name): 
    with open(file, 'r', encoding="utf-8") as data:
        for line in data:
            if name in line: 
                return line