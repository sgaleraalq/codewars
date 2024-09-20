import copy
def encode_rail_fence_cipher(string,n):
    if string == "": return ""
    intervals, x = [""]*n, 1
    intervals[0] = string[0]
    while x < len(string):
        for i in range(1,len(intervals)):
            intervals[i] += string[x]
            x += 1
            if x >= len(string): return "".join(intervals)
        for j in reversed(range(len(intervals)-1)):
            intervals[j] += string[x]
            x += 1
            if x >= len(string): return "".join(intervals)
    
def decode_rail_fence_cipher(string, n):
    if string == "": return ""
    intervals, x = [""]*n, 1
    intervals[0] = string[0]
    while x < len(string):
        for i in range(1,len(intervals)):
            intervals[i] += string[x]
            x += 1
            if x == len(string): break
        if x == len(string): break
        for j in reversed(range(len(intervals)-1)):
            intervals[j] += string[x]
            x += 1
            if x == len(string): break
    w = 0
    for x in range(len(intervals)):
        intervals[x] = string[w:w+len(intervals[x])]
        w = w+len(intervals[x])
    final = intervals[0][0]
    intervals[0] = intervals[0][1:]
    while len(final)!=len(string):
        for x in range(1,len(intervals)):
            final += intervals[x][0]
            intervals[x] = intervals[x][1:]
            if len(final) == len(string): return final
        for y in reversed(range(len(intervals)-1)):
            final += intervals[y][0]
            intervals[y] = intervals[y][1:]
            if len(final) == len(string): return final
