# List is mutable array
# Same elements two list are stored in different location


my_list = ["apple", 23, 4.6]
list_2 = ["ball", my_list]  # Nested list
print("normal list = ", my_list)
print("Nested list = ", list_2)

fruit = ['apple', 'mango', 'grapes', 'orange', 'guava', 'watermelon']
print("\nSlicing")
print(fruit[2]) # convert to string
print(fruit[0:3]) # 0 is included and 3 is excluded
print(fruit[0:6:2]) # 0 to 6th index with gape of 2 in index
print(fruit[::-1]) # reverse
print(fruit[-3])
print(fruit[-4:-1])

#append(any_thing)
# any_thing = string, int, list, tuple, dict etc
print("Size of list = ", len(fruit))
fruit.append("Lichies")
print("Append to list = ", fruit)

number =[]
for i in range(1, 20, 2):
    number.append(i)
print(number)

mix = ["cabbage", "beans", "pea"]
num = (10, 20, 30)
mix.append(fruit)
mix.append(num)
print(mix)

#insert(pos, value)
# sames as append put pos is specified
# default pos is at last
# all element shifts

# extend(values, values)
# same as append but it opens the substring
list_1 = [10, 20, 30, 40]
list_2 = [50, 60, 70]
list_1.extend(list_2) #list 2 is open and added one by one
print(list_1)

# Remove(item)
# one at a time
fruit.remove("apple")
print(fruit)

# pop(index)
fruit.pop() # last item is default
fruit.pop(1)
print(fruit)

#copy()
list_1 = [1, 2, 3, 4]
list_2 = [1, 2, 3, 4]
list_3 = list_1 # Changed is copyed
list_4 = list_2.copy() # Changed is not copyed
print(f"1 : {id(list_1)}\t2 : {id(list_2)}")
print(f"1 : {id(list_1)}\t3 : {id(list_3)}")
print(f"2 : {id(list_2)}\t4 : {id(list_4)}")
list_3.append(10)
print(id(list_1), list_1)
print(id(list_3), list_3)
list_4.append(20)
print(id(list_2), list_2)
print(id(list_4), list_4)

#clear()
#empty the list

#del list_name[index: index]
# permenant delention of list

#index(value, start_pos=0, end_po=len(list_name))
print(fruit.index('orange'))

#cout(value)
num = [1, 1, 1, 1, 2, 3, 4, 21, 1, 1 , 10]
print(num.count(1))

#reverse()
fruit.reverse()
print("Reverse = ", fruit)

# sort()
num.sort(reverse=False) # default reverse
fruit.sort(reverse=True)
print(fruit)
print(num)

# sort base on second value
def sort_second(value):
    return value[1]

number = [(1, 2, 3), (6, 5, 7), (10, 1, 9)]
number.sort(key=sort_second)
print(number)


# built in function
number = [22, 65, 34, 7, 23, 89]
print("Sum of list = ", sum(number))
print("Sum with starting 1000 = ", sum(number, 1000))
string = "a"
print("ascii unit only = ", ord(string))    # only unit string allowed
print("ascii unit to letter", chr(97))

# two list comparision
#Returns : This function returns 1, if first list is “greater” than second list, -1
# if first list is smaller than the second list
# else it returns 0 if both the lists are equal.

# list_1 = [1, 2, 3, 4, 5]
# list_2 = [1, 2, 3, 6, 7]
# list_3 = [1, 2, 3, 1, 1, 2]
# print("list 1 and list 2 = ", cmp(list_1, list_2))
# print("list 2 and list 3 = ", cmp(list_2, list_3))
# print("list 1 and list 1 (equal) = ", cmp(list_1, list_1))
# print("list 1 and list 2 = ", cmp(list_1, list_2))

number = [32, 65, 8, 23, 11, 98, 27, 74, 78, 0]
print("min = ", min(number))
print("max = ", max(number))
print("any = ", any(number)) # find for 1 true to give true ignore false
print("all = ", all(number)) # find for 1 false to give false and ignore true
print("len  = ", len(number), "\n\n")


#enumerate(iterable, start=0) # indexing start from 0
list_1 = [10, 20, 30, 40]
list_3 = enumerate(list_1) # list_3 is object not list
print(list(list_3))
for i, element in enumerate(list_1, start=2):
    print(f"{i} ) {element}")

# Comprehensison

even_list = [i for i in range(2, 9) if i % 2 == 0]
print(even_list)
squre_list = [i**2 for i in range(2, 11)]
print(squre_list)

# table of 5 in table form
a = 5
print("table of 5 :")
tabel = [[f"{a} X {b} = {a * b}"] for b in range(1, 11)]
for i in tabel:
    print(i)

word = [["apple", "red", "kite"], ["sky", "dog", "elephant"]]
small_word = [small
              for sub_list in word
              for small in sub_list
              if len(small) == 3]
print(small_word)

name = "T^ush@a*r Pr#asa*d!"
list_name = [letter
             for letter in name
             if ord(letter) in range(ord('a'), ord('z')+1) or
             ord(letter) in range(ord('A'), ord('Z')+1) or
             ord(letter) == 32]
print(list_name)
f_name = "".join(list_name)
print(f_name)

# lambda -> short function
# lambda <argument> : return (expression)
fun_1 = lambda x : (x % 2 == 0)
print(fun_1(2))

# filter
# filter(function, list)
age = [12, 43, 76, 8, 34, 33, 32, 89]
minors = list(filter(lambda x: (x < 18), age))
print(minors)

#map
# map(function, sequence) and list(map(str, squence))
name = ["simon", "rock", "rion", "muon"]
on_name = list(map(lambda x : x.upper(), name))
print(on_name)

str_age = list(map(str, age))
print(str_age)

# map and filter diff
on_name = list(map(lambda x : ("on" in x), name))
print(on_name)
on_name = list(filter(lambda x : ("on" in x), name))
print(on_name)

# both use
# print name in upper case and and print only "on" present only
new_name = list(map(lambda x: x.upper(), filter(lambda x: "on" in x, name)))
print(new_name)

# reduce
# print(reduce(func, sequence, starting_num))
from functools import reduce
number = [1, 2, 6, 43, 3, 4, 5]
factorial = reduce(lambda x, y: x * y, number)
print(factorial)

max_element = reduce(lambda x, y: x if x>y else y, number)
print(max_element)

s = list("HelloWorld!")
print(s)
# can be unpacked
a, b, c = [1, 2, 3]
print(a)

def un_list(a, b, c, d, e):
    print(a, b, c, d, e)

list_1 = [1, 2, 3, 4, 5]
un_list(*list_1)

def list_it(*args):
    list_1 = list(args)
    print(list_1)

list_it(1, 2, 3, 4, 5, 6)

#%%
