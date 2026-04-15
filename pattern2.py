#1
#3 5
#7 9 11
#13 15 17 19
rows = 4
current_num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(current_num, end=" ")
        current_num += 2
    print()
