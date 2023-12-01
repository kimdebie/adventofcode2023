from typing import List


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        lines = [line.rstrip() for line in f][:-1]
    return lines
