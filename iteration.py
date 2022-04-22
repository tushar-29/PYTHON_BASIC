my_list = [10, 20, 30, 40, 50]

x = 10
y = 20
z = 15

if x < z < y:
    print(True)

for i in my_list:
    print(i, end="\t")

print()
for i in range(len(my_list)):
    print(my_list[i], end="\t")

x = 10
i = 0
print()
while i < x:
    print(i, end="\t")
    i += 1

# one for loop is break at a time
for i in range(2):
    print("\n", i)
    for j in range(100, 1001, 100):
        if(j < 201):
            print(j, end="\t")
        else:
            break

print()


def fun():
    pass

# looping technique
list_1 = ["apple", "ball", "cat", "dog", "egg", "fan"]
list_2 = list("abcdef")
print(list_1, list_2)

for ind, element in enumerate(list_1, 1):
    print(f"{ind}) {element}")

print(type(zip(list_1, list_2)))
for letter, word in zip(list_2, list_1):
    print(f"{letter} for {word}")

number = [2, 5, 7, 1, 8, 4, 2, 9, 1, 6, 3, 2]

for i in sorted(number):
    print(i, end="\t")
else:
    print()

for i in sorted(set(number)):
    print(i, end="\t")
else:
    print("\n")

# similarly we use reversed(iterat)


#%%
