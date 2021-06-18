f = open('lotOfWords.txt', 'r')

final = []
for line in f:
    l = line.split()
    if len(l)<3:
        continue
    else:
        final.append(l[2])

print(final)