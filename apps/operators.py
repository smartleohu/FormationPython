def dup(stack: list) -> None:
    """
    duplicate
    :param stack: list
    :return:
    """
    stack.append(stack[-1])


def drop(stack: list) -> None:
    """
    drop
    :param stack: list
    :return:
    """
    stack.pop()


def swap(stack: list) -> None:
    """
    swap list last 2 elements
    :param stack: list
    :return:
    """
    x, y = stack.pop(), stack.pop()
    stack.append(x)
    stack.append(y)


def fct1(fct):
    def _fct(stack):
        stack.append(fct(stack.pop()))

    return _fct


def fct2(fct):
    def _fct(stack):
        y, x = stack.pop(), stack.pop()
        stack.append(fct(x, y))

    return _fct
