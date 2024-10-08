def get_number(num_str, reduce):
    for i in range(len(num_str) - 1, -1, -1):
        if int(num_str[i:]) > 10: 
            return int(str(int(num_str[0])+1)+num_str[-1]) if reduce and int(num_str[i:]) > 100 else int(num_str[i:])
    return int(num_str) 

def last_digit(lst):
    if len(lst) == 0: return 1
    if len(lst) == 1: return int(str(lst[-1])[-1])

    result = get_number(str(lst[-2]),True)**get_number(str(lst[-1]),True)
    lst[-2] = str(int(str(result).rstrip('0')[-1])+1) + "0" if str(result)[-2:] == "00" else get_number(str(result), False)
    return last_digit(lst[:-1])