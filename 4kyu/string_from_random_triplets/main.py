def find_possibility(x,y,board,word):
    i = word[0]
    index = 1
    possibilities = set()
    already = set()
    while i!=word:
        tmp = []
        index = len(i)
        if y<len(board[0])-1 and (x,y+1) not in already and board[x][y+1] == word[index]:
            tmp.append((x,y+1))
            
        if y<len(board[0])-1 and x<len(board)-1 and (x+1,y+1) not in already and board[x+1][y+1] == word[index]:
            tmp.append((x+1,y+1))
        
        if x<len(board)-1 and (x+1,y) not in already and board[x+1][y] == word[index]:
            tmp.append((x+1,y))
        
        if x<len(board)-1 and y>0 and (x+1,y-1) not in already and board[x+1][y-1] == word[index]:
            tmp.append((x+1,y-1))
        
        if y>0 and (x,y-1) not in already and board[x][y-1] == word[index]:
            tmp.append((x,y-1))
        
        if y>0 and x>0 and (x-1,y-1) not in already and board[x-1][y-1] == word[index]:
            tmp.append((x-1,y-1))
        
        if x>0 and (x-1,y) not in already and board[x-1][y] == word[index]:
            tmp.append((x-1,y))
        
        if y<len(board[0])-1 and x>0 and (x-1,y+1) not in already and board[x-1][y+1] == word[index]:
            tmp.append((x-1,y+1))
            
        if len(tmp)>=1: 
            i+=word[index]
        if len(tmp)==1:
            x,y = tmp[0][0],tmp[0][1]
            already.add((x,y))
            continue
        if len(tmp)>1:
            x,y = tmp[0][0],tmp[0][1]
            already.add((x,y))
            for u in range(1,len(tmp)):
                possibilities.add(((tmp[u][0],tmp[u][1]),i))
            continue
        
        if len(tmp) == 0:
            if len(possibilities)>0:
                new = next(iter(possibilities))
                possibilities.remove(new)
                x,y,i = new[0][0], new[0][1], new[1]
                continue
        return False
    return True

def find_word(board, word):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == word[0]:
                if find_possibility(x,y,board,word):
                    return True
    return False