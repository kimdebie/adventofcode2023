import re
from math import lcm

from utils import read_input

def part1(instructions):
    directions = instructions[0]
    tot_directions = len(directions)
    mapping = {
        re.findall(r'\w+', instruction)[0]: re.findall(r'\w+', instruction)[1:]
        for instruction in instructions[2:]
    }   
    steps = 0
    location = 'AAA'
    while True:
        if location == 'ZZZ':
            break
        direction = directions[steps % tot_directions]
        location = mapping[location][0 if direction == 'L' else 1]
        steps += 1

    print(steps)

def part2(instructions):
    directions = instructions[0]
    tot_directions = len(directions)
    mapping = {
        re.findall(r'\w+', instruction)[0]: re.findall(r'\w+', instruction)[1:]
        for instruction in instructions[2:]
    }   

    all_steps = []

    for loc in [loc for loc in mapping.keys() if loc[2] == 'A']:
        steps = 0
        while True:
            if loc[2] == 'Z':
                break
            loc = mapping[loc][0 if directions[steps % tot_directions] == 'L' else 1]
            steps += 1
        all_steps.append(steps)

    print(lcm(*all_steps))




if __name__ == '__main__':
    file_input = read_input('inputs/day8.txt')
    part1(file_input)
    part2(file_input)