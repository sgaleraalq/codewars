def recoverSecret(triplets):
    letters = list(set([l for t in triplets for l in t]))        
            
    for t in triplets * len(letters):
        for i in range(len(t)-1):
            a, b = letters.index(t[i]), letters.index(t[i+1])
            if( a > b ): letters[b], letters[a] = letters[a], letters[b]
            
    return ''.join(letters)