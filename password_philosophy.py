file = open('day_2.txt', 'r')
data = list(file.read().splitlines())

count  = 0
#part2
for i in data:
    string = i.split()
    pos_1,pos_2 = map(int, string[0].split('-'))
    digit = string[1][0]
    test = string[2]
    x = digit == test[pos_1-1]
    y = digit == test[pos_2-1]
    if x ^ y:
        count += 1
#part1 solution is below
#for i in data:
    #string = i.split()
    #mini,maxi = map(int, string[0].split('-'))
    #digit = string[1][0]
    #test = string[2]
    #x = test.count(digit)
    #if x >= int(mini) and x <= int(maxi):
        #count += 1
        
print(count)
        
    
    
