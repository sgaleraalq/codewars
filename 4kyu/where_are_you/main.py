import re

class ResultList(list):
    def __init__(self, *args, i=0):
        super().__init__(*args)
        self.i = i

def i_am_here(path, result=ResultList([0, 0], i=0)): 
    commands = {"R": 2, "L": 2, "r": 1, "l": -1}
    for s in re.findall(r'\d+|[a-zA-Z]', path):
        result[result.i % 2] += int(s) if s.isdigit() and result.i in [1, 2] else -int(s) if s.isdigit() else 0
        result.i = (result.i+commands[s]) % 4 if s.isalpha() else result.i

    return result