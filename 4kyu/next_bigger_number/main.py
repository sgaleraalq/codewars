def permutations(n):
    if len(n) == 0: return  
    if len(n) == 1: return n
    final = []
    for i in range(len(n)):
        value = n[i]
        not_val = n[:i]+n[i+1:]
        for x in permutations(not_val):
            final.append(value+x)
    
    return set(final)
    
def next_bigger(n):
    n = str(n)
    for x in reversed(range(len(n)-1)):
        if int(n[x])<int(n[x+1]):
            permuted = sorted(permutations(n[x:]))
            for j in range(len(permuted)):
                if permuted[j] == str(n[x:]): return int(str(n[:x])+permuted[j+1])
    return -1