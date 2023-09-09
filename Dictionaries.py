# Dictionaries are valued by key valued pairs like {"key1":"value1", "key2":"value2"}
our_dictionaries = {'key1':'value1', 'key2':'value2'}
print(our_dictionaries)

# Keys can be some type of property as you see below and you can make as many pairs as you like
our_dictionaries = {'name':'Doug', 'age':'12', 'location':'Texas'}
print(our_dictionaries)

# Dictionaries are very useful because we can use the keys to pull data from the dictionaries for example:
print(our_dictionaries['name']) # Doug will display

# another example
print(our_dictionaries['location']) # Prints Texas

# We can also change the values because dictionaries are mutable
our_dictionaries['name'] = 'Sam'
print(our_dictionaries)

# We can also add a new key and value to our dictionary
our_dictionaries['weight'] = '195lbs'
print(our_dictionaries)

print(our_dictionaries['weight'])

# To get rid of a valuse within a dictionary we can use Pop and the whole key is removed
our_dictionaries.pop('weight')
print(our_dictionaries)