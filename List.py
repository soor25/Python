our_list = ['a', 'b', 'c', 9, 5, 4.3]
print(our_list)

# Because our list is mutable we can add to the list
our_list.append('d')
print(our_list)

# indexing is taking out specific values from our list

print(our_list[0])

# insert is used to add a value to the list
our_list.insert(0, 'First element')
print(our_list)

# .remove is used to remove a value from the list
our_list.remove('b')
print(our_list)

# We can use pop to remove index (number) from the list
our_list.pop(1)
print(our_list)

# We can also nest list within lists. Here we can see the inside brackets are within the outside bracket displaying a list within a list.
nested_list = [[1,2,3],3,4,5]
print(nested_list)