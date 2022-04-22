def local_scope(x):
    print("global scope in fun = ", x)
    # re-assign x means local scope of new object x
    # and has no link with list_1
    x = [10, 20]
    print("local scope in fun = ", x)

list_1 = [1, 2, 3, 4, 5, 6]
local_scope(list_1)
print("outside fun ",list_1)

print("args pack")
def args_exp(*args):
    print(type(args))
    print(args)

args_exp("my", "name", "is", "X")
args_exp(["my", "name"])

print("args un pack")
def un_pack(a, b, c):
    print(a, b, c)

# un_pack([1, 2, 3])  # Error of un-packing
un_pack(*[1, 2, 3])

print("kwarg pack")
def kwargs_exp(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

kwargs_exp(name="x", age=19)

print("kwarg unpack")
def un_pack_kwargs(name="x", age=19):
    print(name, age)

un_pack_kwargs(age=16, name="x")

# yield for return
def yield_exp():
    print("explain yield")  # 1st exe
    yield 1 # 1st exe return
    yield 2 # 2nd exe start here and return from here
    yield 3 # 3rd exe start here and return from here

for i in yield_exp():
    print(i)

def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

print("using for loop for yield")
for i in fib(10):
    print(i, end="\t")

print("\nusing function.next() function")

# Initialising
x = fib(4)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
# print(x.__next__())   # execution stops here


number = [10, 43, 654, 123, 13, 556, 13, 12, 56, 89]
filtered = filter(lambda x: x % 2 == 0, number)
print(list(filtered))

mapped = map(lambda x: x % 2 == 0, number)
print(list(mapped))

print("global and local veriable")


def scope():
    # print("Direct use of x in function = ", x)
    global x
    x = 10
    print("assign x in function = ", x)

x = 100
print("outside func = ", x)
scope()
print("x value outside func = ", x)

# First class Function

print("\nFirst Class Function")

def to_lower(string):
    return string.lower()

def to_upper(string):
    return string.upper()

def greet(func):
    str = "Hello World"
    print(func(str))


greet(to_upper)
greet(to_lower)

print("\nCalculator")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiple(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator(cal_fun, n1, n2):
    return cal_fun(n1, n2)

print(calculator(multiple, 3, 7))


#%%
