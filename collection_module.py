from collections import Counter, OrderedDict, ChainMap, namedtuple

print(Counter([1, 2, 3, 1, 3, 2, 1, 1, 1, 2, 3, 3, 3, 2, 1, 2, 2]))
print(Counter(a=10, b=5, c=3))
print(Counter({'a': 13, 'b': 23}))

od = OrderedDict()
od['a'] = 10
od['b'] = 20
od['c'] = 5


def display(od_dict):
    for key, value in od_dict.items():
        print(f"{key} : {value}")


# sequence is maintain
display(od)
od.pop('a')
display(od)
od['a'] = 100
display(od)

# Chain_map(dic1, dic2, dic3, ...)
dict_1 = {'a': "apple", 'b': "ball"}
dict_2 = {'c': "cat", "d": "dog"}
chain_1 = ChainMap(dict_1, dict_2)
print(chain_1)
# list of dicts
print(chain_1.maps)
print(chain_1.keys())
print(chain_1.values())

dict_3 = {'e': "egg", "f": "fan"}
chain_2 = chain_1.new_child(dict_3)  # need to save
print(chain_1)
print(chain_2)

# nametuple(dec_varible, list_of_keys)
student = namedtuple('student', ['name', 'age', 'roll_no'])

s1 = student("Tushar Prasad", 19, 202000216)

print(s1[0])
print(s1.age)
print(getattr(s1, 'roll_no'))

list_1 = ["Tushar", 22, 202000216]
# name of dict should match with student list name
dict_1 = {"name": "Root", "age": 15, "roll_no": 202000216}

print(s1._asdict())
print(student._make(list_1))
print(student(**dict_1))

# key names
print(s1._fields)

# modify name
print(s1._replace(age=26))