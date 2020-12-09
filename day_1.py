sums = []
from itertools import combinations 

file = open('day_1.txt', 'r')
data = list(map(int, file.read().splitlines()))
def pair():
    for i in range(len(sums)):
        for j in range(i, len(sums)):
            for k in range(i, len(sums)):
                if sums[i] + sums[j] + sums[k] == 2020:
                    print(sums[i], sums[j], sums[k])
                    return sums[i]*sums[j]*sums[k]  

#Alternative approach using itertools which will work for all the three paired combination
def findPairs(lst, K): 

    return [pair for pair in combinations(lst, 3) if sum(pair) == K]
        
sums = data
print(pair())
print(findPairs(sums, 2020))
