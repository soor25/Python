
# WhileLoops executes code if some condition is true

# create a condition
i = 1

# We dont want a infinate loop so while i is less than 10 it will repeat and add 1 until it is no longer less than 10
while i < 10:
    i = i + 1
    print(i)
    # We can also nest while loops
    if i == 6:
        break
