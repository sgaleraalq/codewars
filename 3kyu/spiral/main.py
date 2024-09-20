def can_continue(spiral: list, i: int, j: int, direction: str, moves: dict) -> bool:
    extra_checks = {"right": (2, 0), "down": (0, -2), "left": (-2, 0), "up": (0, 2)}
    just_one = {"right": (1, 0), "down": (0, -1), "left": (-1, 0), "up":(0, 1)}
    
    di, dj = moves[direction]
    extra_di, extra_dj = extra_checks[direction]
    j_o_di, j_o_dj = just_one[direction]
    
    if spiral[i + j_o_di][j + j_o_dj] != 0:
        return None

    if spiral[i + di][j + dj] != 0:
        if spiral[i + extra_di][j + extra_dj] != 0 or spiral[i + j_o_di][j + j_o_dj]:
            return None
        return False
    
    return True

def spiralize(size):
    spiral = [[1] * size] + [[0]*(size-1)+[1]] + [[1]+[0]*(size-2)+[1] for _ in range(size - 3)] + [[1] * size]
    direction = "right"
    directions = {"up": "right", "right": "down", "down": "left", "left": "up"}
    moves = {"right": (0, 1), "down": (1, 0), "left": (0, -1),"up": (-1, 0)}
    i, j = 2, 1
    
    while True:
        keep = can_continue(spiral, i, j, direction, moves)
        if keep is None:
            break
        
        elif keep:
            spiral[i][j] = 1
            prev_position = i,j
            i, j = i + moves[direction][0], j + moves[direction][1]
        
        elif not keep:
            direction = directions[direction]
            i, j = prev_position
            i, j = i + moves[direction][0], j + moves[direction][1]    
    
    return spiral