#****
#***
#**
#*
#**
#***
#****
# Part 1: Decreasing pattern from 4 to 1 asterisk
# range(start, stop, step) generates 4, 3, 2, 1
for i in range(4, 0, -1):
    print( "*" * i)

# Part 2: Increasing pattern from 2 to 4 asterisks
# range(start, stop) generates 2, 3, 4
for i in range(2, 5):
    print( "*" * i)
