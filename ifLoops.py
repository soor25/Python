# Must declare variables before calling them
x = 1
y = 2
z = 3

# If statements must end with a colon :
if x >y:
    print('x is less than y!')
    # The line of code below will execute only if the line above is false
else:
    print('Victory!')

# Python uses and, or
if x < y and y > z:
    print('yes')

if x < y or y > z:
    print('Hell yes!')