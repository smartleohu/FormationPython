import math

from apps.interfaces import IInterpreter
from apps.operators import drop, dup, fct1, fct2, swap


class Interpreter(IInterpreter):
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

    def interpret(self, text: str, line_number: int = 0):
        """
        interpret
        :param text: input line text
        :param line_number: line number in the file
        :return:
        """
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
                fct = self.COMMANDS[command]
            except KeyError:
                print(
                    F"ERROR[line={line_number}]: invalid command '{command}'")
                return

            # compute
            try:
                fct(stack)
            except Exception as e:
                print(
                    F"ERROR {e}: [line={line_number}]: unknown error on "
                    F"'executing {command}' witch stack {stack}")
                return

        return stack
