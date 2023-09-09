tuple_a = ('Cat', 'Dog', 'Mouse')

# Tuples does keep the order, so we can use indexing to pull values
print(tuple_a[1])

# Tuples are great when you want to create a list but dont want anyone to edit or change it its immutable(doesnt change)

tuple_a.append('Value')
print(tuple_a)

# This shouldnt work
tuple_a.insert('Bug')
print(tuple_a)