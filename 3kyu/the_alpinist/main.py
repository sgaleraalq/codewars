from collections import deque

def path_finder(area):
    area, dict, queue = [list(line) for line in area.split("\n")], {(0,0):0}, deque([(0,0)])

    while queue:
        i,j = queue.popleft()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
            if 0 <= ni < len(area) and 0 <= nj < len(area[0]):
                cost = dict[(i,j)] + abs(int(area[ni][nj])-int(area[i][j]))
            
                if (ni,nj) not in dict or cost<dict[(ni,nj)]:
                    queue.append((ni,nj))
                    dict[(ni,nj)] = cost
        
    return dict[(len(area)-1,len(area)-1)]