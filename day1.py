from itertools import groupby

# opens file and reads it
f = open('p1.txt', 'r')
content = f.read()
# splits the file into a list
numbers = content.splitlines()

# separates and groups each section by the spaces
elf = [list(g) for k, g in groupby(numbers, key=bool) if k]

# converts all the numbers to ints
for i in range(len(elf)):
    for j in range(len(elf[i])):
        elf[i][j] = (int(elf[i][j]))

totals = {}
# all the elves with their totals
for i in range(len(elf)):
    totals[i] = (sum(elf[i]))

# sorts from the greatest values to the least values and puts into a list as tuples
sorted_total = sorted(totals.items(), key=lambda x: x[1], reverse=True)

# answer to part 1
print(sorted_total[0])

total = 0
for i in range(3):
    total += sorted_total[i][1]

# answer to part 2
print(total)
