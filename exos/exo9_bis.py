from exos.exo8 import COMMANDS


def interpreter(text: str, line_number: int = 0):
    # decompose
    stack = []
    commands = text.split()

    # execute commands
    for command in commands:
        # is it a number?
        try:
            stack.append(float(command))
            continue
        except ValueError:
            pass

        # is it a command?
        try:
            fct = COMMANDS[command]
        except KeyError:
            print(F"ERROR[line={line_number}]: invalid command '{command}'")
            return

        # compute
        try:
            fct(stack)
        except Exception as e:
            print(
                F"ERROR {e}: [line={line_number}]: unknown error on executing "
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

    text_3 = '3 0 /'
    stack_3 = interpreter(text_3)
    print(stack_3)
