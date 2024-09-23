def path_finder(maze):
    i, j, prev, index = 0, 0, (0,0), 0
    maze = maze.split("\n")
    possible_path, already = set(), set()
    
    while True:
        temp = []
        
        if i == len(maze[0])-1 and j == len(maze)-1:
            break
        if (j,i) in possible_path:
            possible_path.remove((j,i))
        # Right
        if i<len(maze[0])-1 and maze[j][i+1] == "." and (j,i+1) != prev and (j,i+1) not in already:
            temp.append((j,i+1))

        # Down
        if j<len(maze)-1 and maze[j+1][i] == "." and (j+1,i) != prev and (j+1,i) not in already:
            temp.append((j+1,i))

        # Up
        if j>0 and maze[j-1][i] == "." and (j-1,i) != prev and (j-1,i) not in already:
            temp.append((j-1,i))
        
        # Left
        if i>0 and maze[j][i-1] == "." and (j,i-1) != prev and (j,i-1) not in already:
            temp.append((j,i-1))
        
        already.add((j,i))
        if len(temp) == 1:
            prev = (j, i)
            i, j = temp[0][1], temp[0][0]
            
        if len(temp)>1:
            prev = (j,i)
            i,j = temp[0][1],temp[0][0]
            for x in range(1,len(temp)):
                possible_path.add(temp[x])
        
        if len(temp)==0:
            if index > len(possible_path)-1: 
                return False
            point = next(iter(possible_path))
            i,j = point[1],point[0]
    
    return True