from pathlib import Path

from exos.exo10 import read_file


def read_files(f_dir: Path):
    for fp in sorted(f_dir.glob('*.txt')):
        print(fp)
        read_file(fp)


if __name__ == '__main__':
    file_dir = Path(__file__).parents[1] / 'samples'
    print(file_dir)
    read_files(file_dir)
