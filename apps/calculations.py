from pathlib import Path
from typing import Callable, List, TypeVar, Type

from apps.interfaces import IInterpreter

TRpnCalculation = TypeVar("TRpnCalculation")


class RpnCalculation:
    def __init__(self, interpreter: IInterpreter, file_path: Path):
        self._interpreter = interpreter
        self._file_path = file_path
        self._result = {}

    @property
    def file_path(self) -> Path:
        return self._file_path

    @property
    def parser(self) -> Callable[[Path], TRpnCalculation]:
        if self.file_path.is_dir():
            return self.read_files
        elif self.file_path.is_file():
            return self.read_file

    @property
    def result(self) -> List[str]:
        res = []
        for line, r in self._result.items():
            res.append(f"{line} returns {r[0]}")
        return res

    @result.setter
    def result(self, value: dict):
        self._result = value

    @classmethod
    def build_result(cls: Type[TRpnCalculation], interpreter: IInterpreter,
                     file_path: Path) -> List[str]:
        return cls(interpreter, file_path).parser().result

    @staticmethod
    def generate(filename: Path, fct: Callable) -> dict:
        """
        generate mapping
        :param filename: file name
        :param fct:
        :return: line and calculated result mapping
        """
        result = {}
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, 1):
                # treat blank/comment lines
                line = line.strip()
                if 0 == len(line) or "#" == line[0]:
                    continue

                # interpret
                result[line] = fct(line, line_number)
        return result

    def read_file(self) -> TRpnCalculation:
        """
        read one file
        :return: RpnCalculation object
        """
        self.result = self.generate(self.file_path,
                                    self._interpreter.interpret)
        return self

    def read_files(self) -> TRpnCalculation:
        """
        read all txt files in a dir
        :return: RpnCalculation object
        """
        for fp in sorted(self.file_path.glob('*.txt')):
            print(fp)
            self.result = self.generate(fp, self._interpreter.interpret)
        return self
