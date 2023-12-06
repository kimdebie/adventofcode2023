import re

from utils import read_input


def part1(races):
    times, distances = [[int(i) for i in re.findall(r'\d+', r)] for r in races]

    win_options = 1
    for time, record in zip(times, distances):
        win_options *= sum(
            ((time-press_time) * press_time) > record
            for press_time in range(time)
        )
    
    print(win_options)


def part2(race):
    time, record = [int("".join(i for i in r if i.isdigit())) for r in race]
    min_win_option = None
    for press_time in range(time):
        if ((time-press_time) * press_time) > record:
            min_win_option = press_time
            break
    print(len(range(time))-2*min_win_option+1)
    

if __name__ == '__main__':
    file_input = read_input('inputs/day6.txt')
    part1(file_input)
    part2(file_input)