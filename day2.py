import re 

from utils import read_input


limits = {'red': 12, 'green': 13, 'blue': 14}


def part1(games):

    valid_games = 0

    for i, game in enumerate(games):
        game_valid = True
        for color, limit in limits.items():
            for match in re.findall(r'\d+ ' + color, game):
                if int(match.split(' ')[0]) > limit:
                    game_valid = False
        if game_valid:
            valid_games += i+1

    print(valid_games)


def part2(games):

    games_sum = 0
    
    for game in games:
        game_product = 1
        for color in limits.keys():
            game_product *= max(
                int(match.split(' ')[0])
                for match in re.findall(r'\d+ ' + color, game)
            )
        games_sum += game_product

    print(games_sum)


if __name__ == '__main__':
    file_input = read_input('inputs/day2.txt')
    part1(file_input)
    part2(file_input)
