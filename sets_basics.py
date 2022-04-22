# Elements with no duplicates
# Is mutable

# set(iterable)
# mix values are allowed
# discard duplictes
# int are arrange in sorted order
set_1 = set("HelloWorld!")
print(set_1)

list_1 = ["Hello", "world", "hello", "world"]
set_1 = set(list_1)
print(set_1)

list_1 = [2, 5, 7, 4, 2, 1, 8, 5, 3 , 9, 1, 6, 3]
set_1 = set(list_1)
print(set_1)

# adding element
set_1.add(11)
set_1.add((12, 13))
print(set_1)

set_1.update([15, 13])
print(set_1)

# remove element
# remove(element) or discard(elemet)
# remove throw error if not fount discard dont throw error
set_1.remove(2)
# set_1.remove(2) Error
set_1.discard(2)
print(set_1)

set_1.discard((12, 13))
print(set_1)

# similarly
# pop(), clear(), copy(), union(), intersection(), difference(),
# issubset(), isdisjoint()

# frozenset is similerar to set but are non-mutable sets
# insert(), update(), pop(), remove(), discard() can't be used
#%%

#%%
