from itertools import permutations
import math

def apply_op(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else math.inf

def generate_results(a,b,c,d,x,y,z):
    return [
        apply_op(apply_op(apply_op(a, x, b), y, c), z, d),
        apply_op(apply_op(a, x, b), y, apply_op(c, z, d)),
        apply_op(a, x, apply_op(b, y, apply_op(c, z, d))),
        apply_op(a, x, apply_op(apply_op(b, y, c), z, d)),
        apply_op(apply_op(a, x, apply_op(b, y, c)), z, d)
    ]

def make_str(a,b,c,d,x,y,z):
    return [
        f"(({a}{x}{b}){y}{c}){z}{d}",
        f"({a}{x}{b}){y}({c}{z}{d})",
        f"{a}{x}({b}{y}({c}{z}{d}))",
        f"{a}{x}(({b}{y}{c}){z}{d})",
        f"({a}{x}({b}{y}{c})){z}{d}"
    ]

def equal_to_24(a, b, c, d):
    ops = "+-*/"
    
    for perm in permutations([a, b, c, d]):
        for x in ops:
            for y in ops:
                for z in ops:
                    results = generate_results(perm[0], perm[1], perm[2], perm[3], x, y, z)
                    for (i, result) in enumerate(results):
                        if result == 24:
                            return make_str(perm[0],perm[1],perm[2],perm[3],x,y,z)[i]
    
    return "It's not possible!"