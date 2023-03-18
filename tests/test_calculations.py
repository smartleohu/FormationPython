from pathlib import Path
from unittest.mock import mock_open
import builtins
import pytest

from apps.calculations import RpnCalculation
from apps.interpreters import Interpreter


class TestCalculations:

    @pytest.fixture()
    def mock_file_path(self):
        return Path(__file__)

    @pytest.fixture()
    def interpreter(self):
        return Interpreter()

    @pytest.fixture
    def calculator(self, mock_file_path, interpreter):
        return RpnCalculation(interpreter, mock_file_path)

    def test_calculate(self, interpreter, calculator,
                       mock_file_path, monkeypatch):
        monkeypatch.setattr(builtins, 'open',
                            mock_open(read_data='2 5 + DUP *'))
        res = calculator.generate(mock_file_path, interpreter.interpret)
        assert res == {'2 5 + DUP *': [49.0]}
