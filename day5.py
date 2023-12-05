import re

from utils import read_input


def parse_mapping(map_part):
    return


def part1(map):
    seeds = re.findall(r'\d+', map[0])

    map_parts, map_part = [], []
    for row in map[2:]:
        if row != '\n':
            map_part.append(row)
        else:
            map_parts.append(parse_mapping((map_part)))
            map_part = []


if __name__ == '__main__':
    file_input = read_input('inputs/day5.txt')
    part1(file_input)
