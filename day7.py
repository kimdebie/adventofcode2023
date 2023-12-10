from collections import Counter, defaultdict

from utils import read_input

CARD_ORDER = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARD_ORDER_JOKERS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def check_type(cards):
    cards = [i for i in cards]
    if len(set(cards)) == 1: # five of a kind
        return 0
    if len(set(Counter(cards).values()) & set((4, 1))) == 2: # four of a kind
        return 1
    if len(set(Counter(cards).values()) & set((3, 2))) == 2: # full house
        return 2
    if 3 in Counter(cards).values(): # 3 of a kind
        return 3
    if sorted(list(Counter(cards).values())) == [1, 2, 2]: # two pair
        return 4
    if sorted(list(Counter(cards).values())) == [1, 1, 1, 2]: # one pair
        return 5
    if len(set(cards)) == 5:
        return 6
    return 7 # is this even possible?

def check_type_jokers(cards):
    all_cards = [i for i in cards if i != 'J']
    if not all_cards:
        return 0
    jokers = sum(i=='J' for i in cards)
    card_counts = Counter(all_cards)
    card_counts[max(all_cards,key=all_cards.count)] += jokers
    if len(set(card_counts.keys())) == 1: # five of a kind
        return 0
    if len(set(card_counts.values()) & set((4, 1))) == 2: # four of a kind
        return 1
    if len(set(card_counts.values()) & set((3, 2))) == 2: # full house
        return 2
    if 3 in card_counts.values(): # 3 of a kind
        return 3
    if sorted(list(card_counts.values())) == [1, 2, 2]: # two pair
        return 4
    if sorted(list(card_counts.values())) == [1, 1, 1, 2]: # one pair
        return 5
    if len(card_counts.values()) == 5:
        return 6
    return 7 # is this even possible?


def part12(cards_bids,jokers=False):

    card_order = CARD_ORDER_JOKERS if jokers else CARD_ORDER
    type_fn = check_type_jokers if jokers else check_type

    cards_types = defaultdict(list)
    for cards_bid in cards_bids:
        card_bid = cards_bid.split(' ')
        card, bid = card_bid[0], card_bid[1]
        cards_types[type_fn(card)].append((card, bid))

    cards_types = dict(sorted(cards_types.items()))
    for i, card_type in enumerate(cards_types.keys()):
        for j in range(4, -1, -1):
            cards_types[card_type].sort(key = lambda k: card_order.index(k[0][j]))
    bids_sorted = [int(card_bid[1]) for type in cards_types.values() for card_bid in type][::-1]
    winnings = sum((i+1)*int(bid) for i, bid in enumerate(bids_sorted))
    print(winnings)



if __name__ == '__main__':
    file_input = read_input('inputs/day7.txt')
    part12(file_input)
    part12(file_input, jokers=True)