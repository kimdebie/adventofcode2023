import re

from utils import read_input


def parse_map_part(map_part):
    return [
        [int(i) for i in instruction] 
        for line in map_part
        if (instruction := re.findall(r'\d+', line))
    ]   


def parse_map(map):
    seeds = [int(i) for i in re.findall(r'\d+', map[0])]

    map_parts, map_part = [], []
    for row in map[3:]:
        if row != '':
            map_part.append(row)
        else:
            map_parts.append(parse_map_part((map_part)))
            map_part = []
    map_parts.append(parse_map_part((map_part)))

    return seeds, map_parts


def part1(seeds, parsed_map):
    seed_nrs = []
    for seed in seeds:
        next_seed = seed
        for map_part in parsed_map:
            for destination, source, range_length in map_part:
                if source < next_seed < source+range_length:
                    difference = destination - source
                    next_seed = next_seed + difference
                    break
        seed_nrs.append(next_seed)
    print(min(seed_nrs))


def part2(seeds_ranges, parsed_map):

    seeds_ranges = [seeds_ranges[i:i+2] for i in range(0, len(seeds_ranges), 2)]
    min_seed = min(s for s, r in seeds_ranges)
    max_seed = max(s+r for s, r in seeds_ranges)

    # at the start, assume there is only one range and that it maps as 0
    all_ranges = [(min_seed, max_seed, 0)]
    map_part = parsed_map[0]
    for destination_mp, source_mp, range_length_mp in map_part:
        covered_in_range = False
        for destination_ar, source_ar, range_length_ar in all_ranges:
            if destination_mp < destination_ar


    print("done")
            


if __name__ == '__main__':
    file_input = read_input('inputs/day5.txt')
    part1(*parse_map(file_input))
    part2(*parse_map(file_input))
