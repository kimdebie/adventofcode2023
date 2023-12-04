import re
from utils import read_input
from collections import defaultdict


def part1(cards):


    points = 0


    for card in cards:

        card_points = 0.5

        winning, mine = [re.findall(r'\d+', nr_list)
                         for nr_list in card.split(':')[1].split('|')]
        for m in mine:
            if m in winning:
                card_points *= 2
        
        points += card_points * (card_points > 0.5)

    print(points)


def part2(cards):

    card_counts = {i: 1 for i in range(len(cards))}

    for i, card in enumerate(cards):

        winning, mine = [re.findall(r'\d+', nr_list)
                         for nr_list in card.split(':')[1].split('|')]
        
        card_points = sum(m in winning for m in mine)

        for n in range(card_points):
            card_counts[i+n+1] += 1
    
    total_cards = sum(card_counts.values())
    print(total_cards)
       



if __name__ == '__main__':
    file_input = read_input('inputs/day4test.txt')
    part1(file_input)
    part2(file_input)
