file = open('day_8.txt', 'r')
data = file.read().splitlines()

def check(array):
    i = 0
    accum = 0
    n = len(array)
    visited = []
    while True:
        if i == n:
            return accum
        if i not in visited:
            visited.append(i)
        else:
            return 0
        
        if array[i] [0]  == 'nop':
            i+=1
        elif array[i] [0] == 'acc':
            accum += int(array[i][1])
            i+=1
        else:
            i = i + int(array[i][1])
    

def main():
    my_dict = {}
  
    instruct_array = []
    for i in data:
        instruct = i[:3]
        value = i[4:]
        instruct_array.append([instruct, value])
    
    for i in range(len(instruct_array)):
        pseudo_array = instruct_array.copy()
        if instruct_array[i][0] == 'nop':
            pseudo_array [i] [0] = 'jmp'
            accum = check(pseudo_array)
            if accum == 0:
                pseudo_array[i][0] = 'nop'
            else:
                break
        elif instruct_array[i][0] == 'jmp':
            pseudo_array [i] [0] = 'nop'
            accum = check(pseudo_array)
            if accum == 0:
                pseudo_array[i][0] = 'jmp'
            else:
                break            
    
    print(accum)
                
                
            
            
    
    
main()