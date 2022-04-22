# String is non mutable data type but can be re-initialise
# Del or modifing is not allowed at particular index
# Del or modifing entire string is allowed

string_1 = "apple, ball, {a}, {b}".format(a = "cat", b = "dog")
print(string_1)
string_1 = "{0:b}".format(10)
print("Binary repesentation = ", string_1)
string_1 = "{0:e}".format(294.32323)
print("Expontationa representation ", string_1)
string_1 = "{0:.3f}".format(1/6)
print("Float Representation ", string_1)
print("|{0:<20}|{1:^20}|{2:>20}|".format("Left", "middle", "right"))


class Person:
    age = 10
    name = 'Tushar'
print("\n\n{p.name} age is {p.age}\n\n".format(p=Person()))

string = "Hello today is a grate day for programming"

print(string[0:13]) # print element from index 0 to 11
print(string[::-1]) # reverse string
print(string[::2]) # leave 2 index
print(string[-15: -1]) # -ve indexing

# Built in funcions
print("\nFunction used")

string = "hello World 30"
# 1st letter as capital and all other small excape non alphabetic
print(string.capitalize())

# string_variable.center(width_size, fill_space_with=' ')
print(string.center(20, '*'))

# casefold change case of original ("Aggracive Lower")
print(string.casefold())

#string_var.count(sub_string, start_pos=0, end_pos=len(string_var))
print(string.count('o', 3, 10)) # chcks in lo World

# string.encode(encoding='UTF-8',errors='strict')
srting_1 = 'pythön!'
print(string_1.encode('UTF-8', 'strict'))    #throw error
print(string_1.encode('ascii', errors='replace'))   # error char is repace by ?

# string.find(sub_string, start_pos=0, end_pos) # return -1 if not found
# else return starting index of that sub_string
# string.rfind() work same but search from backword
print(string.find('o', 5, 9)) # finding second 0

# index() same as find but return error if not found
print(string.index('o', 5, 9))

#string_var.endwith(sub_string, start_pos=0, end_pos=len(starting_var))
#string_var.startswith(sub_string, start_pos=0, end_pos=len(starting_var))
print(string.endswith("30", 0, len(string)))

#change case
print("\n\nchange to lower case = ", string.lower())
print("change to upper case = ", string.upper())
print("change case = ", string.swapcase())

#strip(sub_string=' ')
string_2 = "   apple ball cat dog   "
print("\n\nstripping : ", string_2.strip())
print(string_2.strip(" ap"))
print(string_2.strip("ap"))

# partition(sub_string)
# string to list
# similarly we have lpartition() and rpartition
string_2 = "i am angry and i am mad"
print(string_2.partition("am")) # occure on only first one
print(string_2.partition("not"))

# replace(sub_string, replaced_string, no_of_time_to_replace)
song = 'Let it be, let it be, let it be, let it be'
# replacing only two occurences of 'let'
print("Replac\n", song.replace('let', "don't let", 2))



# isalnum() chcek for digit and letter
# return false even for white space
print("is alpha numeric = ", string.isalnum())
print("is alpha = ", string.isalpha())

# check for digit no matter its sub or super script but return false for 1/2
print("is digit = ", "1.23".isdigit())

# check for int in string so return false for super or subscript digit
print("is decimial = ", "1.23".isdecimal())

# true for fraction digit, sub-superscirpt
print("is numeric = ", "1.23".isnumeric())

# islower() ignore white space
print("is lower = ", string.islower())
print("is upper = ", string.isupper())
print("is printable (not \\t, \\n) = ", string.isprintable())
# check whitespace ignore non priantable like \t, \n
print("is whitespace = ", string.isspace())
# istitile() ignore non alpha
print("is title case = ", string.istitle())


#List string
list_1 = ['1', '2', '3', '4']
# sperator.join(iteratable)
# compert to string
print(", ".join(list_1))

s1 = "abc"
s2 = "123"
print(s1.join(s2))  # s2(s1[0]+s2(s1[1])+....

dict_1 = {'1': "apple", '2': "ball"}
print("-->".join(dict_1.values()))
print("-->".join(dict_1)) #with keys

# string.split(seperator, no_of_times_split=(whole string))
# convert to list
fruit = "apple, mango, banana, grapes, orange"
print(fruit.split(',', 2))
print(fruit.split(','))

# string.splitline(False)
fruit = "apple\nmango\ngrapes\n"
print(fruit.splitlines())
print(fruit.splitlines(True))




# String Tempelets
from string import Template
print("String Templets")
student = [('Aryan', 78), ('Bishal', 88), ('Sonam', 63)]
t = Template("$name has got $mark out of 90")
for i in student:
    print(t.substitute(name=i[0], mark=i[1]))

dict_2 = {"name": "Tushar", "age": 19}
print("{name} age is {age}".format(**dict_2))

# Dynamic
string = "{:{fill}{align}{width}}"
print(string.format("Hello World!", fill="*", align="^", width=20))
print(string.format("Hello World!", fill="-", align="<", width=20))

class Son:
    def __format__(self, format):
        if(format == 'age'):
            return '23'
        return 'None'


print("Adam's age is: {:age}".format(Son()))
#%%
