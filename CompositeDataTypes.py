# list, tuple, dictionary, frozenset, set

# A list can store multiple data types and is mutable (can be changed)
our_list = ['a','b','c', 1.5]
print(our_list)

# Tuple
our_tuple = ('a','b','c')
print(our_tuple)

# Dictionary
# A dictionary is a made up of a volue and a key
our_dictionary = {'key1':'value1', 'name':'Thomas', 'height':'5'"'"'10'}
print(our_dictionary)

# Set
# Made up of a single element
# sets are also unordered and if you repeat anything in a set it will only be mentioned once
our_set = {'one', 'two', 'three'}
print(our_set)

# frozenset
# Parenthesis will be around it denoting it that its a frozen set
our_frozenset = frozenset(our_set)
print(our_frozenset)