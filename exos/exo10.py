from pathlib import Path

from exos.exo9_bis import interpreter


def read_file(filename: Path):
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, 1):
            # treat blank/comment lines
            line = line.strip()
            if 0 == len(line) or "#" == line[0]:
                continue

            # interpret
            result = interpreter(line, line_number)
            print(result)


if __name__ == '__main__':
    fp = Path(__file__).parents[1] / 'samples' / '1.txt'
    print(Path(__file__).parent)
    read_file(fp)
