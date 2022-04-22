#input return all in string format
name = input("Enter your name : ")
print(f"name variable type = {type(name)}")
print(name)

number = int(input("enter a number : "))
print("Type cast by int() function")
# can be done to for float(), str() ->(default), list(), tuple(), dict()
print(f"type of number variable is : {type(number)}")
print(number)

print("Taking Multipe Input")
x, y, z = input("Enter any three no. : ").split()   # no need to press enter at every input
print(f"x = {x} and y = {y} and z = {z}")

# my_list = list(int(input("Enter the element : ").split()))    # Error
my_list = list(map(int, input("Enter the element : ").split())) #to get int values directly

print(my_list)
#%%
