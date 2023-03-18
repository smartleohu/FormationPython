import math


def fct1(fct):
    def _fct(stack):
        stack.append(fct(stack.pop()))

    return _fct


def fct2(fct):
    def _fct(stack):
        y, x = stack.pop(), stack.pop()
        stack.append(fct(x, y))

    return _fct


if __name__ == '__main__':
    stack_org = [2, 10]
    stack_cpy = stack_org.copy()
    print(fct1(math.log10)(stack_cpy))
    print(f"apply LOG10 over {stack_org} is {stack_cpy}")

    stack_cpy = stack_org.copy()
    print(fct2(lambda x, y: x ** y)(stack_cpy))
    print(f"apply POWER over {stack_org} is {stack_cpy}")
