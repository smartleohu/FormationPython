import math

from exos.exo4 import drop, dup, swap
from exos.exo7 import fct1, fct2
from pprint import pprint

COMMANDS = {'+': fct2(lambda x, y: x + y),
            '-': fct2(lambda x, y: x - y),
            '*': fct2(lambda x, y: x * y),
            '/': fct2(lambda x, y: x / y),
            '^': fct2(lambda x, y: x ** y),
            'COS': fct1(math.cos),
            'SIN': fct1(math.sin),
            'TAN': fct1(math.tan),
            'ACOS': fct1(math.acos),
            'ASIN': fct1(math.asin),
            "CEIL": fct1(math.ceil),
            'ATAN': fct1(math.atan),
            'LN': fct1(math.log),
            'LOG': fct1(math.log10),
            'EXP': fct1(math.exp),
            'ABS': fct1(math.fabs),
            'DUP': dup,
            'SWAP': swap,
            'DROP': drop,
            }

if __name__ == '__main__':
    pprint(COMMANDS)
    stack_org = [2, 1]

    for operator, fct in COMMANDS.items():
        stack_cpy = stack_org.copy()
        fct(stack_cpy)
        print(f"appliquer {operator} sur {stack_org} est {stack_cpy}")
