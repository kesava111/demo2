with open('F:\list_1\list11.py')as file:
    data=file.read()
    words=data.split()
    for line in words:
        word=line.split()
        for lines in word:
            obj=lines.swapcase()
            print(obj)
    