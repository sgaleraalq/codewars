from itertools import permutations

def generate_ops(a,b,c,d,x,y,z) -> list:
    return [
        f"({a}{x}{b}){y}{c}{z}{d}",
        f"({a}{x}({b}{y}{c})){z}{d}",
        f"(({a}{x}{b}){y}{c}){z}{d}",
        f"({a}{x}{b}){y}({c}{z}{d})",
        f"{a}{x}{b}{y}({c}{z}{d})",
        f"{a}{x}({b}{y}({c}{z}{d}))",
        f"{a}{x}(({b}{y}{c}){z}{d})",
    ]

def equal_to_24(a,b,c,d):
    ops = "+-/*"
    for x in ops:
        for y in ops:
            for z in ops:
                if x == y == z:
                    if eval(str(a)+x+str(b)+y+str(c)+z+str(d)) == 24:
                        return str(a)+x+str(b)+y+str(c)+z+str(d)
                for (a,b,c,d) in permutations([a,b,c,d]):
                    for op in generate_ops(a,b,c,d,x,y,z):
                        try:
                            if eval(op) == 24:
                                return op
                        except ZeroDivisionError:
                            continue
    return "It's not possible!"