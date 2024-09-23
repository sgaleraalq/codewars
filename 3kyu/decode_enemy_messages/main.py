import copy
def succession(number, index):
    i, number1 = 0, copy.copy(number)
    while True:
        if number%67 == index: 
            return i
        i += 1
        number += number1
    
def decode(s):
    code,final = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? ", ""

    for i in range(len(s)):
        if s[i] not in code: 
            final += s[i]
        else: 
            final += code[succession(2**(i+1),code.index(s[i])+1)]
        
    return final