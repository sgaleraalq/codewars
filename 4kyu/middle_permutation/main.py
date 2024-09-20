def middle_permutation(string):
    letters = sorted(string, reverse=True)
    start = letters.pop(len(string)//2)
    if len(string) % 2:
        start += letters.pop(len(string)//2)
    return start + "".join(letters)