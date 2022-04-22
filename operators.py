# https://www.geeksforgeeks.org/operator-functions-in-python-set-1/
a = 10
b = 3
print("Arithmetic operators")
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # give float value
print(a // b)  # int division
print(a % b)
print(a ** b) # a to the power b

print("\nRelation Operators")
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

print("\nBitwise Operators")
# here a is 10 that is 0000 1010 in binary
# here b is 3 that is  0000 0011 in binary
print(a & b) # result in binary is 0000 0010 that is 2
print(a | b) # result in binary is 0000 1011 that is 11
print(~a) # (~)not operator= not(comp(0000 1010) - 1) is 0000 1011 tat is -11
print(a >> 2) # shift right by 2 0000 1010 = 0000 0010 = 2
print(a << 2) # shift right by 2 0000 1010 = 0010 1000 = 40

print("\nAssignment operator")
a = b
a += 10
a -= 10
a *= 1000
a **= 3
a /= 20
a //= 10
a %= 10
# a &= b
# a |= b
# a ^= b
# a >>= b
# a <<= b
print(f"a = {a} and b = {b}")

print("\nSpecial Operator")
a = "apple"
b = "apple"
c = "appleisgood"
x = 10
y = 10
z = 30
print(f"a = {id(a)} and b = {id(b)} and c = {id(c)}")
print(f"x = {id(x)} and y = {id(y)} and z = {id(z)}")
print(a is b)
print(a is c)
print(x is y)
print(x is z)
my_list = [10, 20, 30]
your_list = [10, 20, 30]
print(f"my_list = {id(my_list)} and yourlist = {id(your_list)}")
print(my_list is your_list) # flase
# similarly `not is` works

print("\nOperator 'in' ")
a = "apple" # check for sequence
print('g' in a)
print('A' in a)
print('ppe' in a)
# ppe does not match sequence apple due to l

print("Copyies")
a = [10, 20, 30]
b = a
c = [10, 20, 30]
# address of c and a is different but a, b are same
a.append(40)
# a and b both appends 40
print(f"a = {id(a)} and b = {id(b)} and c = {id(c)}")
print(a == b)

b = [10, 20, 30, 40]
# address of all 3 are different
print(f"a = {id(a)} and b = {id(b)} and c = {id(c)}")
print(a == b)



print("\n Operator Over Loadings")

class stduent:
    def __init__(self, a, b):
        self.a = a
        self. b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

a = stduent(10, 20)
b = stduent(30, 40)
print(a + b)
# similary we can perform many operation

import operator
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("\nOperator Function")
print(operator.add(10, 20))
print(operator.mod(10, 3))
print(operator.getitem(my_list, 5))

list_1 = []
list_2 = []
list_3 = list_1
if list_1 == list_3:
    print("== is true")
else:
    print("== is false")

print("is is true") if list_1 is list_2 else print("is is false")

print("== is ture") if list_1 == list_2 else print("== is false")
print("is is ture") if list_1 is list_3 else print("is is flase")

x = 10
print(True) if type(x) is int else print(False)
#%%
