import re

# \   Used to drop the special meaning of character
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE
#     to match.
# ()  Enclose a group of REs

# \d   Matches any decimal digit, this is equivalent
#      to the set class [0-9].
# \D   Matches any non-digit character.
# \s   Matches any whitespace character.
# \S   Matches any non-whitespace character
# \w   Matches any alphanumeric character, this is
#      equivalent to the class [a-zA-Z0-9_].
# \W   Matches any non-alphanumeric character.

p = re.compile('[a-f]')
text = "Today we are learning regular expression"
# list is return
print(p.findall(text))

# + symbol join the word in the list
q = re.compile('\w+')

text = "today I wake up at 5:00 o'clock in the morning"
print(q.findall(text))

# Here ':', ' ' ,',' are not AlphaNumeric thus, the point where splitting occurs
print(re.split('\W+', 'On 12th Jan 2016, at 11:02 AM'))

# '\d+' denotes Numeric Characters or group of characters
# Splitting occurs at '12', '2016', '11', '02' only
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM'))


print(re.split('[a-c]+', 'On 12th Jan 2016, at 11:02 AM'))

# replace string
# re.sub(str_to_replace, replace_str, str, flag)
print(re.sub('and', '&', "me and my friend", flags=re.IGNORECASE))

# re.subn(str_to_replace, replace_str, str, flag)
# flag argument should be seperated by |
# return tuple with tuple[1] as no. of replaced
print(re.subn('and', '&', "me and my friend", flags=re.IGNORECASE))

# excape()
# return string with all \ for all non alphnumeric
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

# search(regex, string)
# reg is : string_cont whitespace numeric_cont_value
# it stop after first successful search
reg = r"([a-zA-Z]+) (\d+)"
ans = re.search(reg, "Dob is June 29")
print(ans.group(0))
print(ans.group(1))
print(ans.group(2))
print("start ind = ", ans.start())
print("End ind = ", ans.end())

# Email validation
reg_email = re.compile(r"""
            ^([a-zA-Z0-9_\.-]+) # starting(^) part of email
            @                   # @ symbol
            ([a-z0-9\.-_]+)     # domain name
            \.                  # . symbol
            ([a-z]{2,6})$          # end($) with len 2 to 6
            """, re.VERBOSE | re.IGNORECASE)
            
mat = re.fullmatch(reg_email, "tushar_202000216@smit.smu.edu.in")
print(mat.group(1))
print(mat.group(2))
print(mat.group(3))

# password validation
# Should have at least one number.
# Should have at least one uppercase and one lowercase character.
# Should have at least one special symbol.
# Should be between 6 to 20 characters long


# taditional method
def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

# re method

reg_pass = re.compile(r"""
                    ^(?=.*[a-z])    # should contain
                    (?=.*[A-Z])     # should contain
                    (?=.*\d)        # shound contain
                    (?=.*[!@#$%^&*?])    # shuld contain
                    [A-Za-z\d!@#$%^&*?]{6,20}$
                    """, re.VERBOSE)

password = re.search(reg_pass,"Gg@2002")
print(password.group(0))


#%%
