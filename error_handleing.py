# syntax Error : Wrong Code written
sum = 10
if sum == 10: # missing colon (:)
    print("sum = ", sum)

# ZeroDivisionError : when any int or float divided by 0
num = 10 / 1 # 10 / 0
print(num)

# IndexError

list_1 = [1, 2, 3, 4]
try:
    print("Index 1 element = ", list_1[0])
    print("Index 10 element = ", list_1[10])
except IndexError:
    print("Index Error Occured")

# NameError

try:
    print("Vlaue of b is ", b)
    z = 10/0    # not executed
except (NameError, ZeroDivisionError): # bracket is necessory
    print("Error occured")


# try, except, else

def divide(a=1, b=1):
    try:
        c = a / b
    except(ZeroDivisionError):
        return 0
    else: # execute only when error is not raised any time
        return c

print(divide(3, 1))

# use of finally

def greet(string):
    try:
        print("Hello" + string)
    except(ValueError, TypeError):
        print("Error: Only Sring allowed")
    else:
        print("Have a good day")
    finally: # execute in all cases
        print("The end")

greet("Storm")
greet(1)


# raise

# x = 100
#
# if x >= 100:
#     raise Exception("Cant be grater then 100")


class MyError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))


try:
    raise (MyError(3 * 2))
 # show error but if that error is in except
# then execute excute except part

except MyError as error:
    print('A New Exception occured: ', error.value)





# BaseException

#  +-- Exception
#       1) StopIteration
#       2) StandardError

#       |    a) BufferError
#       |           i) ArithmeticError
#       |                   * FloatingPointError
#       |                   * OverflowError
#       |                   * ZeroDivisionError

      # |    b) AssertionError
      # |    c) AttributeError
      # |    d) EnvironmentError
      # |        i) IOError
      # |        ii) OSError
      # |             * WindowsError (Windows)
      # |             * VMSError (VMS)

      # |    e) EOFError
      # |    f) ImportError
      # |    g) LookupError
      # |        i) IndexError
      # |        ii) KeyError

      # |    h) MemoryError
      # |    I) NameError
      # |         i) UnboundLocalError

      # |    j) ReferenceError
      # |          i) RuntimeError
      # |         ii) NotImplementedError

      # |    k) SyntaxError
      # |         i) IndentationError
      # |               * TabError

      # |    l) SystemError
      # |    m) TypeError
      # |    n) ValueError

      # |          i) UnicodeError
      # |                * UnicodeDecodeError
      # |                * UnicodeEncodeError
      # |                * UnicodeTranslateError

      # 2) Warning
      #      a) DeprecationWarning
      #      b) PendingDeprecationWarning
      #      c) RuntimeWarning
      #      d) SyntaxWarning
      #      e) UserWarning
      #      f) FutureWarning

	  #  3) ImportWarning
	  #  4) UnicodeWarning
	  #  5) BytesWarning

