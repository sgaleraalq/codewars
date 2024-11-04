def smaller(arr):
    res = []
    for i in range(len(arr)):
        r = 0
        for j in range(i, len(arr)):
            if arr[j]<arr[i]: r+=1
        res.append(r)
    return res