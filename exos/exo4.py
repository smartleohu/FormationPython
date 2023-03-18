def dup(stack):
    stack.append(stack[-1])


def drop(stack):
    stack.pop()


def swap(stack):
    x, y = stack.pop(), stack.pop()
    stack.append(x)
    stack.append(y)


if __name__ == '__main__':
    stack_org = ['2', '5']
    stack_cpy = stack_org.copy()
    dup(stack_cpy)
    print(f"DUP on {stack_org} is {stack_cpy}")

    stack_cpy = stack_org.copy()
    drop(stack_cpy)
    print(f"DROP on {stack_org} is {stack_cpy}")

    stack_cpy = stack_org.copy()
    swap(stack_cpy)
    print(f"SWAP on {stack_org} is {stack_cpy}")
