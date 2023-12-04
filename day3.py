import re
from utils import read_input


def sanitize_schematic(schematic):
    # add line with . character before and after
    # and . character to the start and end of every line
    dots = ["." * len(schematic[0]) + "."]
    schematic = dots + ['.' + line + '.' 
                        for line in schematic] + dots

    return schematic


def part1(schematic):

    schematic = sanitize_schematic(schematic)
    
    parts_sum = 0

    for i, line in enumerate(schematic):
        for number in re.finditer(r'\d+', line):
            start_ix, end_ix = number.span()
            chars_around = (schematic[i-1][start_ix-1:end_ix+1] +
                            line[start_ix-1] + line[end_ix] + schematic[i+1][start_ix-1:end_ix+1])
            if len([c for c in chars_around if c != '.' and not c.isdigit()]) > 0:
                parts_sum += int(number[0])

    print(parts_sum)


def part2(schematic):

    schematic = sanitize_schematic(schematic)

    gears_sum = 0

    for i, line in enumerate(schematic):
        for star in re.finditer(r'\*', line):
            surrounding_ints = [
                number
                for adjacent_line in [schematic[i-1], line, schematic[i+1]]
                for number in re.finditer(r'\d+', adjacent_line)
            ]

            adjacents = [
                int(si[0])
                for si in surrounding_ints
                if set(range(star.start(), star.end())) & set(range(si.start()-1, si.end()+1))
            ]

            if len(adjacents) == 2:
                gears_sum += adjacents[0] * adjacents[1]

    print(gears_sum)



if __name__ == '__main__':
    file_input = read_input('inputs/day3.txt')
    part1(file_input)
    part2(file_input)
