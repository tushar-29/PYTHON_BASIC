tuple_1 = (1, 2, 3, 4, "G", "rate")
print(tuple_1)
tuple_2 = (23, 54, 3)
tuple_3 = (tuple_1, tuple_2)
tuple_4 = tuple_1 + tuple_2
print(tuple_3)
print(tuple_4)

tuple_1 = ("HEllo")
print(tuple_1)
print(type(tuple_1)) #single element without comma is str

tuple_1 = ("Hello",)
print(tuple_1)
print(type(tuple_1))

# tuple_1[1] = 23 Not allowed
# insert , item deletion , replace after deceleration
# Tuples are non-mutable
tuple_1 = (1, 2, 3, 4)
tuple_2 = (1, 2, 3, 4)
tuple_3 = tuple_1
print(f"tuple 1 = {id(tuple_1)}, Tuple 2 = {id(tuple_2)}")
print(f"Tuple 1 {id(tuple_1)}, tuple 3 {id(tuple_3)}")

#list unpacking
a, b, *d = tuple_1
print(a, b, d)
#%%
