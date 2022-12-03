f = open('p3.txt', 'r')
content = f.read()

#a - z = 1- 26
#A - Z = 27 - 52
whole = content.split()
common = []
for i in range (len(whole)):
    size = int(len(whole[i])/2)
    first=(whole[i][:size])
    second=(whole[i][size:])
    for j in first:
        if j in second:
            common.append(j)
            break
total = 0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(common)):
    total += (letters.index(common[i]) + 1)


print(f'Part 1 : {total}')

# part 2
multi = []

with open('p3.txt') as j:
    count = 1
    elf1, elf2, elf3 = '', '', ''
    for line in j:
        line = line.strip()
        if count == 1:
            elf1 = line
            count += 1
        elif count == 2:
            elf2 = line
            count += 1
        elif count == 3:
            elf3 = line
            for l in elf1:
                if l in elf2:
                    if l in elf3:
                        multi.append(l)
                        count = 1
                        break


total = 0
for i in range(len(multi)):
    total += (letters.index(multi[i]) + 1)

print(f'Part 2: {total}')