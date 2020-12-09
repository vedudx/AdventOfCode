file = open('day_3.txt', 'r')
data = file.read().splitlines()
row = []
for i in data:
    column = list(i)
    row.append(column)

right, down = 0,0
count = 0
prod = 1
x = 1
for i in [1,3,5,7,0]:
    count = 0
    right = 0
    down = 0
    while True:
        if i == 0:
            x = 2
            i = 1
        right += i
        right = right % len(column)
        down += x
        if down > len(row)-1:
            break
        if row [down] [right] == '#' or row[down] [right] == 'X':
            count += 1
            row [down] [right] = 'X'
        else:
            row [down] [right] = 'O'
     
    prod *= count
    print(count)
print(prod)