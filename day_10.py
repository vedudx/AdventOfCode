from collections import defaultdict
import heapq
file = open('day_10.txt', 'r')
data = file.read().splitlines()

li = []
heapq.heapify(li)
listi = [0]
diff = [0]*3

#I could have just used sort but I am familiarising myself with DS hence i did both :)
for i in data:
    heapq.heappush(li, int(i))
    listi.append(int(i))

prev_jolt = 0
while len(li) != 0:
    small = heapq.heappop(li)
    if small - prev_jolt <= 3:
        diff[small - prev_jolt-1]+=1
        prev_jolt = small
    else:
        break

print((diff[2]+1)*diff[0]) #add 1 for the personal adapter voltage

paths = defaultdict(int)
paths[0] = 1
listi.sort()
max_volt = listi[len(listi)-1] + 3
listi.append(max_volt)
for adapter in listi:
    for diff in range(1, 4):
        next_adapter = adapter + diff
        if next_adapter in listi:
            paths[next_adapter] += paths[adapter]
            print(paths[next_adapter], next_adapter)
print(paths[max_volt])

    
 