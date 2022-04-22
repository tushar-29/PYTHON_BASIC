text = """Today I will learn error handling
and file handling in python"""


with open("file_1.txt", "w") as file:
    file.write(text)

with open("file_1.txt", "r") as file:

    # convert to list with each line as element
    # file.readline(no_fo_lines)
    list_1 = file.readlines()
    print(list_1)

    # string data
    # data = file.read()
    # print(data)

    for word in list_1:
        print(word.strip("\n"))


print("\n\n")

text = ["My name is ABC\n", "I live in Sikkim Gangtok\n"]

with open("file_1.txt", 'w') as file:
    file.write("Hello, \n")
    file.writelines(text)

with open("file_1.txt", "r") as file:
    print("\nfile.read()")
    print(file.read())
    file.seek(0) # come back to 0th pos at file

    print("\nfile.read(10)")
    print(file.read(10))
    file.seek(0)

    print("\nfile.readlines()")
    print(file.readlines())
    file.seek(0)

    print("\nfile.readline()")
    print(file.readline())
    file.seek(0)

    print("\nfile.readline(15), 15 is no. of char max in a line")
    print(file.readline(15))
    file.seek(0)
