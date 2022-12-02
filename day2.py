f = open('p2.txt', 'r')
content = f.read()

rock = 1
paper = 2
scissors = 3

win = 6
loss = 0
draw = 3

total = 0
# Split the input file
predictions = []
elf = []
user = []
for line in content:
    line = line.strip()
    if line:
        predictions.append(line)

# split predictions to the user choices and the elf choices
elf = predictions[::2]
user = predictions[1::2]

# part 1

# calculate the total based on the selections
for i in range(len(elf)):
    if elf[i] == 'A' and user[i] == 'X':
        total += draw + rock
    elif elf[i] == 'A' and user[i] == 'Y':
        total += win + paper
    elif elf[i] == 'A' and user[i] == 'Z':
        total += loss + scissors
    elif elf[i] == 'B' and user[i] == 'Y':
        total += draw + paper
    elif elf[i] == 'B' and user[i] == 'Z':
        total += win + scissors
    elif elf[i] == 'B' and user[i] == 'X':
        total += loss + rock
    elif elf[i] == 'C' and user[i] == 'Z':
        total += draw + scissors
    elif elf[i] == 'C' and user[i] == 'X':
        total += win + rock
    elif elf[i] == 'C' and user[i] == 'Y':
        total += loss + paper

# part 1 answer
print(f'part 1 total: {total}')

# part 2

# x = loss
# y = draw
# z = win

total = 0
for i in range(len(elf)):
    if elf[i] == 'A' and user[i] == 'X':
        total += loss + scissors
    elif elf[i] == 'A' and user[i] == 'Y':
        total += draw + rock
    elif elf[i] == 'A' and user[i] == 'Z':
        total += win + paper
    elif elf[i] == 'B' and user[i] == 'Y':
        total += draw + paper
    elif elf[i] == 'B' and user[i] == 'Z':
        total += win + scissors
    elif elf[i] == 'B' and user[i] == 'X':
        total += loss + rock
    elif elf[i] == 'C' and user[i] == 'Z':
        total += win + rock
    elif elf[i] == 'C' and user[i] == 'X':
        total += loss + paper
    elif elf[i] == 'C' and user[i] == 'Y':
        total += draw + scissors

# part 2 answer
print(f'part 2 total: {total}')
