def sudoku(puzzle):
    ranges, all_options, options = {0:0,1:0,2:0,3:3,4:3,5:3,6:6,7:6,8:6},{1,2,3,4,5,6,7,8,9},[]
    # To get all the positions of 0s in the sudoku and append to list
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0: 
                options.append((i,j))
    
    # While we still have positions to fill
    while len(options)>0:
        already_in = []
        for x in options:
            # row, column and square gets all the numbers that position CANNOT be
            row, column = set(puzzle[x[0]]), set(puzzle[w][x[1]] for w in range(9))
            square = set()
            for y in range(ranges[x[0]], ranges[x[0]]+3):
                for z in range(ranges[x[1]], ranges[x[1]]+3):
                    if puzzle[y][z] != 0: 
                        square.add(puzzle[y][z])
            row.remove(0), column.remove(0)
            union = (row.union(column)).union(square)
            
            # If there is only one possible number for that position
            if len(union) == 8:
                number = next(iter(all_options - union))
                puzzle[x[0]][x[1]] = number
                already_in.append(x)
                
        # Remove already filled position from the remaining list
        for inside in already_in:
            options.remove(inside)

    return puzzle