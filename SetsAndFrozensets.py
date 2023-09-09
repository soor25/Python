# Sets are just unique element containers
set_a = {'one', 'two','three'}

# Sets are mutable
set_a.add('four')
print(set_a)

# Sets are unordered so you cant use indexing to pull the value

# this creates a list of items you can add while add only allows for one item to be added
set_a.update(['five', 'six', 'seven'])
print(set_a)

# How to get rid of elements from the set we have two options

# Remove returns a error if the item is not in the set
set_a.remove('six')
print(set_a)

# Discard will just return none (value will be removed and if you call it again you wont see a error)
set_a.discard('six')

# we will try and remove the same item again and now we should get a error
#set_a.remove('six')

# Pop also allows us to remove a element from the set, it will remove the last element the issue is that sets are unordered so we dont know which element will be removed here.
set_a.pop()
print(set_a)

# Frozenset is the same as a set but now you dont want any of the values to change its immutable.
f_set_a = frozenset(set_a)