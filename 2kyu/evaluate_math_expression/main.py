import re

def replace_double_negatives(expression):
    def replacer(match):
        preceding_part = expression[:match.start()].strip()
        if preceding_part and preceding_part[-1].isdigit():
            return '+'
        else:
            return ''
    return re.sub(r'--', replacer, expression)

def make_calculations(numbers, ops, symbols):
    OPS = {
        "*": lambda a,b: a * b, 
        "/": lambda a,b: a / b,
        "+": lambda a,b: a + b,
        "-": lambda a,b: a - b
    }
    del_positions = []
    for o in range(len(ops)):
        if ops[o] in symbols:
            res = OPS[ops[o]](float(numbers[o]), float(numbers[o+1]))
            del_positions.append(o)
            numbers[o+1] = res
    return [num for i, num in enumerate(numbers) if i not in del_positions], [op for op in ops if op not in symbols]

def calc_with_no_parenth(expression):
    numbers = re.findall(r'[+-]?\d+(?:\.\d+)?', expression)
    ops = []
    for i in range(len(expression)-1):
        if expression[i] in ("+" "*" "/"):
            ops.append(expression[i])
        elif expression[i] == "-" and not expression[i+1].isdigit():
            ops.append(expression[i])

    while "*" in ops or "/" in ops:
        numbers, ops = make_calculations(numbers, ops, ["*", "/"])
    
    while "+" in ops or "-" in ops:
        numbers, ops = make_calculations(numbers, ops, ["+", "-"])
        
    return numbers[0]

def calc(expression):
    expression = replace_double_negatives(expression)    
    if "(" not in expression:
        return calc_with_no_parenth(expression)
    else:
        p = (None, None)
        for i in range(len(expression)):
            if expression[i] == "(":
                p = (i+1,None)
            if expression[i] == ")":
                p = (p[0], i)
                break

        return float(calc(expression[:p[0]-1] + str(calc_with_no_parenth(expression[p[0]:p[1]])) + expression[p[1]+1:]))