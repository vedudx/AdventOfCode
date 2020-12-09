file = open('day_5.txt', 'r')
data = file.read().splitlines()
maxi = 0
a = [[0 for i in range(8)] for i in range(128)]
def find_seat(a):
    for i in range(128):
        for j in range(1, 7):
            if a[i] [j -1] == 1 and a[i] [j +1] == 1:
                if a[i] [j] == 0:
                    return (i, j)

def binary_back(i, count, lo, hi):
    mid = (lo + hi) // 2
    if count == 3:
        return max(lo, hi)
    if i[count] == 'L':
        return binary_back(i, count + 1, lo, mid)
    else:
        return binary_back(i, count + 1, mid + 1, hi)   
    
def binary_part(i, count, lo, hi):
    mid = (lo + hi)//2
    if count == 7:
        return min(lo, hi)

    if i[count] == 'F':
        return binary_part(i, count + 1, lo, mid)
    else:
        return binary_part(i, count + 1, mid+1, hi)
for i in data:
    row = binary_part(i,0, 0 , 127)
    col = binary_back(i[7:], 0, 0, 7)
    maxi = max(8*row+col, maxi)
    a[row] [col] += 1
ro,co = find_seat(a)
print(maxi)
print(8*ro+co)    
    

