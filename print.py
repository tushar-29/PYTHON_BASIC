# Printing Data
# Syntax: print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)
# Parameters:
# value(s) : Any value, and as many as you like. Will be converted to string before printed
# sep=’separator’ : (Optional) Specify how to separate the objects,
#                           if there is more than one.Default :’‘
# end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
# file : (Optional) An object with a write method. Default :sys.stdout
# flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False).
#           Default: False
# Returns: It returns output to the screen.


from time import sleep
from io import StringIO

print("Use of print() values")
print("Hello World!")
print('Different inverted comma use "MY" ')
print("Excape characte is '\\' ")   #excape character \
print("tab a\tz")   #tab character
print("""ssdasd
asdasd
sadas     sdf
                dsd""") #indent is copied strickly


# Parameter in print()
print("\n\nParameter 'end' use ")
print("Hello World!", end='\n') #Defaut end statement is '\n'
print("Put * at end", end='******')
print("   -NOTE : end statement is replace by * so line is not left")

print("\n\nSEPARATORS")
print('apple', 'ball', 'cat', sep="@")   #seperator default is : ''

print("\n\nParameter 'flush' use")
# flush True help to print each character seperatly rather then one go
# main used in command promt to delay print as used below
count = 3
for i in range(1, count+1):
    print(i, end=">>", flush=True) #default is False
    # sleep(i)
else:
    print('end')

print("\n\nParameter 'file' use")

#file deceleration
my_file = StringIO()

# Directry write in file `my_file` without printing
print("Hello", file=my_file)
# Get string from my_file to file_txt
file_txt = my_file.getvalue()
print(file_txt)

# sting and variable
x = 5
print("x = ", x)
x = 10
y = 20
print('x is 10 and y is 20')
print("x = {} and y = {}".format(x, y))
print("x = {0} and y = {1}".format(x, y))
print("x = {1} and y = {0}".format(x, y))

print("Use of fsting")
# use of fstring
print(f"{'x'} = {x} and {'y'} = {y}")

