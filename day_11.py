file = open('day_11.txt', 'r')
data = file.read().splitlines()


string = [list('-'+x+'-') for x in data]

col_length = len(string[0])

x = ['-']*col_length
string.append(x)
string.insert(0, x)
row_length = len(string)
listi = []
change_list = []
#part 1 code
#def empty_flood(i, j):
    #non = True
    #if string [i] [j] == 'L':
        #for k in range(i - 1, i+2):
            #for l in range(j - 1, j+2):
                #if string[k][l] == '#':
                    #non = False
                    #break
            #if non == False: break
        #else:
            #change_list.append((i, j))
    
#def occupy_flood(i, j):
    #count = 0
    #if string [i] [j] == '#':
        #for k in range(i - 1, i+2):
            #for l in range(j - 1, j+2):
                #if string[k][l] == '#':
                    #count += 1
        #if count >= 5: #bcoz I am counting the member itself
            #listi.append((i, j))         
    
#def fill(li, a):
    #if li:
        #for i in li:
            #string[i[0]] [i[1]] = a
        #return True
    #else:
        #return False
    
#def call(a):
    #for i in range(1, row_length):
        #for j in range(1, col_length):
            #if a == 1:
                #empty_flood(i, j)
            #else:
                #occupy_flood(i,j)
                
#while True:
    #choice1, choice2 = False, False
    #call(1)
    #if not fill(change_list, '#'): choice1 = True
    #change_list.clear()
    #call(0)
    #if not fill(listi, 'L'): choice2 = True
    #listi.clear()
    #if choice1 and choice2: break
#final_count = 0

#for i in string:
    #final_count += i.count('#')

#print(final_count)


#Part Two

def empty_flood(i, j):
    #empty flood modified for part 2
    if string [i] [j] == 'L':
        for x in [-1,1]:
            z = x if x == -1 else col_length
            for k in range(j, z, x):
                if k == j: continue
                if string[i + (k-j)] [k] == '-': break
                if string [i + (k-j)] [k] == 'L':
                    break
                elif string [i+(k-j)] [k] == '#':
                    return 
        for x in [-1, 1]:
            z  = x if x == -1 else col_length
            for k in range(j, z, x):
                if k == j:continue
                if string [i] [k] == 'L':
                    break
                elif string [i][k] == '#':
                    return
   
        for x in [-1, 1]:
            z  = x if x == -1 else row_length
            for k in range(i, z, x):
                if k == i:
                    continue
                if string [k] [j] == 'L':
                    break
                elif string [k][j] == '#':
                    return

        for x in [-1, 1]:
            z = x if x == -1 else row_length
            for k in range(j, z, x):
                if k == j: continue
                if string [i+(j-k)] [k] == '-': break
                if string [i + (j-k)] [k] == 'L':
                    break
                elif string [i + (j-k)] [k] == '#':
                    return
                    

        change_list.append((i, j))
    
def occupy_flood(i, j):
    count = 0
    if string [i] [j] == '#':
        for x in [-1,1]:
            z = x if x == -1 else col_length
            for k in range(j, z, x):
                if k == j: continue
                if string[i + (k-j)] [k] == '-': break
                if string [i + (k-j)] [k] == 'L':
                    break
                elif string [i+(k-j)] [k] == '#':
                    count += 1
                    break

        for x in [-1, 1]:
            z  = x if x == -1 else col_length
            for k in range(j, z, x):
                if k == j:continue
                if string [i] [k] == 'L':
                    break
                elif string [i][k] == '#':
                    count += 1
                    break
    
        for x in [-1, 1]:
            z  = x if x == -1 else row_length
            for k in range(i, z, x):
                if k == i:
                    continue
                if string [k] [j] == 'L':
                    break
                elif string [k][j] == '#':
                    count += 1
                    break     
       
        for x in [-1, 1]:
            z = x if x == -1 else row_length
            for k in range(j, z, x):
                if k == j: continue
                if string [i+(j-k)] [k] == '-': break
                if string [i + (j-k)] [k] == 'L':
                    break
                elif string [i + (j-k)] [k] == '#':
                    count += 1
                    break
                        
    if count >=5:
        listi.append((i, j))
            
def fill(li, a):
    if li:
        for i in li:
            string[i[0]] [i[1]] = a
        return True
    else:
        return False
    
def call(a):
    for i in range(1, row_length):
        for j in range(1, col_length):
            if a == 1:
                empty_flood(i, j)
            else:
                occupy_flood(i,j)
                
while True:
    choice1, choice2 = False, False
    call(1)
    if not fill(change_list, '#'): choice1 = True
    change_list.clear()
    call(0)
    if not fill(listi, 'L'): choice2 = True
    listi.clear()
    if choice1 and choice2: break
final_count = 0

for i in string:
    print(*i)
    final_count += i.count('#')

print(final_count)
