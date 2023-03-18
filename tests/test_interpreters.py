import pytest

from apps.interpreters import Interpreter


class TestInterpreter:

    @pytest.fixture
    def interpreter(self):
        return Interpreter()

    @pytest.mark.parametrize("text, expected", [
        ("2 5 + DUP *", 49.0),
        ("12 0.5 SIN * 36 0.5 COS * + ABS LOG", 1.5722450079684882),
        ("3 3.14 * 4 / DUP SIN SWAP /", 0.30061609709062936)])
    def test_interpret(self, interpreter, text, expected):
        print(interpreter.interpret(text))
        assert interpreter.interpret(text) == [expected]
