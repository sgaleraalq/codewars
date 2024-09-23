from collections import deque

def path_finder(maze):
    m = [list(line) for line in maze.split("\n")]
    visited = [[False] * len(m[0]) for _ in range(len(m))]
    queue = deque([(0, 0, 0)])
    
    while queue:
        i, j, moves = queue.popleft()
        if visited[i][j]:
            continue
            
        visited[i][j] = True       
        
        if (i == len(m) - 1 and j == len(m) - 1):
            return moves
        
        for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if 0 <= ni < len(m) and 0 <= nj < len(m[0]) and not visited[ni][nj] and m[ni][nj] == ".":
                queue.append((ni, nj, moves + 1))
        
    return False