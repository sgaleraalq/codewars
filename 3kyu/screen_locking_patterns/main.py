def permutations(s):
    if len(s) == 1: return s
    final = []
    for i in range(len(s)):
        m = s[i]
        rest = s[:i]+s[i+1:]
        for y in permutations(rest):
            final.append(m+y)
    return final

def count_patterns_from(firstPoint, length):
    strings = "ABCDEFGHI"
    jumps   = {
        "AC":"B","AG":"D","AI":"E",
        "GA":"D","GI":"H","GC":"E",
        "IC":"F","IG":"H","IA":"E",
        "CA":"B","CI":"F","CG":"E",
        "DF":"E","BH":"E","FD":"E",
        "HB":"E"
    }
    # Base cases
    if length>=10 or length<=0: return 0
    if length == 1: return 1

    all = permutations(strings.replace(firstPoint,""))
    for x in range(len(all)):
        all[x] = firstPoint + all[x][:length-1]
    all = set(all)
    patterns = []
    for j in all:
        st = "possible"
        if len(j) == 2:
            if j not in jumps: patterns.append(j)
        
        if len(j)>2:
            for x in range(0,len(j)-1):
                if j[x:x+2] in jumps:
                    if j.find(jumps[j[x:x+2]])==-1 or j.find(jumps[j[x:x+2]])>j.find(j[x:x+2]): 
                        st = "impossible"
                        break
            if st == "possible":
                patterns.append(j)

    return len(set(patterns))