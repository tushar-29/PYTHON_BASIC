# key: value structure data type

dict_1 = {1: "apple", 2: "ball", 3: "cat", 4: "dog"}
print(dict_1)

# list to dict
dict_2 = dict([(1, "apple"), (2, "ball")])
print(dict_2)

list_1 = list(dict_1.values()) # convert to list
print(dict_1.keys())
print(dict_1.values())
print(list_1)

# nested dict
dict_1 = {"a": "apple", "b": "ball",
          "number": {"1": 1, "2": 2}
          }
print(dict_1)

# index cretion
dict_1 = {}
dict_1["a"] = "apple"
dict_1["b"] = "ball"
dict_1["number"] = 1, 2, 3, 4, 5
dict_1["name"] = {"a": "Aryan", "b": "bishal"}
print(dict_1)

# getting element
print(dict_1["a"])
print(dict_1["number"][2])
print(dict_1["name"]["b"])
# using get(key_name)
print(dict_1.get("tellow")) # return none if not found
# print(dict_1["st"]) Error

# delete from dict
del dict_1["name"]["b"]
print(dict_1)
# deletion from key name throw error if not found
dict_1.pop("b")
print(dict_1)

# popitem() return pop() item form dict
print(dict_1.popitem())

# dict to str
print(str(dict_1))

# update existing or add
dict_1.update(b = "ball", a = "aeroplane")
print(dict_1)

# setdefault(key, return_default_value=None)
# get value by key or return none
print(dict_1.setdefault("a"))
print(dict_1.setdefault("c", "NOT FOUND"))


#   items()
#Returns: A view `object` that displays a list of a given
# dictionary’s (key, value) tuple pair.
print("\n\nItems")
print(dict_1.items())
for key, values in dict_1.items():
    print(f"{key} : {values}")

#iteritems()
print("\n\nItems")
print(dict_1.items())
for key, values in dict_1.items():
    print(f"{key} : {values}")


# # has_key(key)
# print(dict_1.has_key('a'))

# fromkey(dict_key_seq, dict_key=None)
list_1 = ['a', 'b', 'c', 'd', 'e']
list_2 = [1, 2]
dict_2 = dict.fromkeys(list_1)
print(dict_2)
dict_2 = dict.fromkeys(list_1, list_2)
print(dict_2)

def dict_kwargs(**kwargs):
    for key, values in kwargs.items():
        print(f"{key} -> {values}")

dict_kwargs(name="Tushar Prasad", age=19)
#%%
