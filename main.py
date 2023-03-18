import argparse
from pathlib import Path
from pprint import pprint

from apps.calculations import RpnCalculation
from apps.interpreters import Interpreter

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--filepath', help='file path to fetch RPN files',
        default=f'/Users/ruijinghu/PycharmProjects/calcul_formation/samples')
    args = parser.parse_args()

    filepath = Path(args.filepath) / '1.txt'
    res = RpnCalculation.build_result(Interpreter(), filepath)
    pprint(res)
    filepath = Path(args.filepath)
    res = RpnCalculation.build_result(Interpreter(), filepath)
    pprint(res)
