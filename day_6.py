file = open('day_6.txt', 'r')
data = file.read().split('\n\n')


all_ans = []
sums = 0
for i in data:
    seen = set()
    dicti = dict()
    count = 1
    for char in i:
        if char != '\n':
            dicti[char] = dicti.get(char,0) + 1
        else:
            count += 1
    for i in dicti:
        if dicti[i] == count:
            seen.add(i)
    sums += len(seen)
print(sums)
    