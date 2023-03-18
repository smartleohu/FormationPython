from exos.exo8 import COMMANDS


def interpreter(text: str, line_number: int = 0):
    # decompose
    stack = []
    commands = text.split()

    # execute commands
    for command in commands:
        # is it a number?
        if str(command[-1]).replace('.', '').isdigit():
            stack.append(float(command))
            continue
        elif command in COMMANDS:
            fct = COMMANDS[command]
        else:
            print(
                F"ERROR: [line={line_number}]: unknown error on executing "
                F"'{command}' witch stack {stack}")
            return

        if command in ('+', '-', '*', '/'):
            if len(stack) > 1:
                fct(stack)
        elif len(stack) > 0:
            fct(stack)
        else:
            print(
                F"ERROR: [line={line_number}]: unknown error on executing "
                F"'{command}' witch stack {stack}")
            return

    return stack


if __name__ == '__main__':
    text_1 = '3 3.14 * 4 / DUP SIN SWAP /'
    stack_1 = interpreter(text_1)
    print(stack_1)

    text_2 = '3 pi * 4 / DUP SIN SWAP /'
    stack_2 = interpreter(text_2)
    print(stack_2)

    text_3 = '3 SIN /'
    stack_3 = interpreter(text_3)
    print(stack_3)

    # text_3 = '3 0 /'
    # stack_3 = interpreter(text_3)
    # print(stack_3)
