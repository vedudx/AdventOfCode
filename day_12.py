file = open('day_12.txt', 'r')
data = file.read().splitlines()

instruct = [[x[0], int(x[1:])] for x in data]

#Part 1
#start = 'E'
#dist = [0,0,0,0] # North, East, South, West

#current_d = 1
#for i in instruct:
    #if i[0] == 'F':
        #dist[current_d] += i[1]
    #elif i[0] == 'N':
        #dist[0] += i[1]
    #elif i[0] == 'E':
        #dist[1] += i[1]
    #elif i[0] == 'S':
        #dist[2] += i[1]
    #elif i[0] == 'W':
        #dist[3]+= i[1]
    #elif i[0] == 'L':
        #current_d = (current_d - i[1]//90) % 4
    #elif i[0] == 'R':
        #current_d = (current_d + i[1]//90) % 4

#print(abs(dist[0]-dist[2])+ abs(dist[1] - dist[3]))
        
#Part 2

dist = [0,0,0,0] # North, East, South, West
way_point = [1,10,0,0]

#some error in if way_point[0] and similar conditions
def rotate(l, value,x ,y):
    if l == 'R':
        if value == 0:
            return (x, y)
        elif value == 1:
            return (-y, x)
        elif value == 2:
            return (-x, -y)
        else:
            return (y, -x)
    if l == 'L':
        if value == 0:
            return (x, y)
        elif value == 1:
            return (y, -x)
        elif value == 2:
            return (-x, -y)
        else:
            return (-y,x)
for i in instruct:
    if i[0] == 'F':
        dist[0] += i[1]*way_point[0]
        dist[1] += i[1]*way_point[1]
    
    elif i[0] == 'N':
        way_point[0] += i[1]     
          
    elif i[0] == 'E':
        way_point[1] += i[1]            
          
    elif i[0] == 'S':
        way_point[0] -= i[1]
  
    elif i[0] == 'W':
        way_point[1] -= i[1]
            
    elif i[0] == 'L':
        x, y = way_point[0],  way_point[1]
        x,y = rotate(i[0], i[1]//90, x, y)
        way_point[0], way_point [1] = x,y
        
    elif i[0] == 'R':
        x = way_point[0]
        y = way_point[1] 
        x,y = rotate(i[0], i[1]//90, x, y)
        way_point[0], way_point [1] = x,y        


print(abs(dist[0]) + abs(dist[1]))

    