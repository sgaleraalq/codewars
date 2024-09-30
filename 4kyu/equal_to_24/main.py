def permutations(lst: list) -> list:
    if len(lst) == 0: return []
    if len(lst) == 1: return [lst]
    
    result = []
    for i in range(len(lst)):
        number = lst[i]
        rem_lst = lst[:i] + lst[i+1:]
        
        for perm in permutations(rem_lst):
            result.append([number] + perm)

    return result

def combinations(operations: list, pos: int) -> list:
    result = []
    if pos == 1: return [[op] for op in operations]
    
    for op in operations:
        for comb in combinations(operations, pos-1):
            result.append([op]+comb)
        
    return result

def should_parenth(lst: list) -> bool:
    return any(op in lst for op in ["+", "-"]) and any(op in lst for op in ["*", "/"])

def parenthesis_comb(operators: list) -> list:
    results = []
    counts = operators.count("+") + operators.count("-")

    if counts == 1:
        if operators[0] in ("+" "-"):
            first_op = ["(",operators[0],")", operators[1], operators[2]]
            second_op = ["(",operators[0],"(", operators[1], ")", ")", operators[2]]
            return [operators, first_op, second_op]
        if operators[-1] in ("+" "-"):
            first_op = [operators[0], operators[1], "(", operators[2], ")"]
            second_op = [operators[0], "(", operators[1], "(", operators[2], ")", ")"]
            return [operators, first_op, second_op]
        else:
            first_op = [operators[0], "(", operators[1], ")", operators[2]]
            second_op = ["(", operators[0], "(", operators[1], ")", ")", operators[2]]
            third_op = ["(", "(", operators[0], ")", operators[1], ")", operators[2]]
            fourth_op = [operators[0], "(", "(", operators[1], ")", operators[2], ")"]
            fifth_op = [operators[0], "(", operators[1], "(", operators[2], ")", ")"]
            return [operators, first_op, second_op, third_op, fourth_op, fifth_op]
            
    if counts == 2:
        if (operators[0] in ("*", "/") or operators[-1] in ("*", "/")):
            if operators[0] in ("*" "/"):
                first_op = [operators[0], "(", operators[1], operators[2], ")"]
                second_op = [operators[0], "(", operators[1], ")", operators[2]]
                third_op = [operators[0], operators[1], "(", operators[2], ")"]                
            if operators[-1] in ("*" "/"):
                first_op = ["(", operators[0], operators[1], ")", operators[2]]
                second_op = ["(", operators[0], ")", operators[1], operators[2]]
                third_op = [operators[0], "(", operators[1], ")", operators[2]]
            return [operators, first_op, second_op, third_op]
        else:
            for op in operators:
                if op in ["+", "-"]:
                    results.extend(["(", op, ")"])
                else:
                    results.append(op)
        return [operators, results]

    return operators


def create_expression(l1: list, l2: list) -> str:
    i,j, expression = 0,0, ""
    while i<len(l1) or j<len(l2):
        if j<len(l2): 
            while l2[j] == "(":
                expression += "("
                j+=1
        if i<len(l1):
            expression += l1[i]
            i+=1
        if j<len(l2):
            expression += l2[j]
            j+=1
        if j<len(l2):
            while l2[j-1] == ")":
                if j == len(l2): break
                expression+=l2[j]
                j+=1

    return expression

def equal_to_24(a,b,c,d):
    perms = permutations([str(a),str(b),str(c),str(d)])
    operations = combinations(["+","-","*","/"], 3)

    for p in perms:
        for op in operations:
            if should_parenth(op):
                for op1 in parenthesis_comb(op):
                    expression = create_expression(p, op1)
                    try:
                        if eval(expression) == 24:
                            return expression
                    except ZeroDivisionError as e:
                        continue
            else:
                expression = create_expression(p, op)
                try:
                    if eval(expression) == 24:
                            return expression
                except ZeroDivisionError as e:
                    continue

    return "It\'s not possible!"