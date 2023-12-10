import re

from utils import read_input

def part1(sequences):

    extrapolations = 0

    for sequence in sequences:
        sequence = [int(i) for i in re.findall(r'\d+', sequence)]
        layers = [sequence]

        while not sum(bool(i) for i in layers[-1]) == 0:
            differences = [layers[-1][i+1]-layers[-1][i] for i in range(len(layers[-1])-1)]
            layers.append(differences)
        layers[-1].append(0)
        for l in range(len(layers)-2, -1, -1):
            last_digit = layers[l][-1] + layers[l+1][-1]
            layers[l].append(last_digit)
        extrapolations += layers[0][-1]

    print(extrapolations)

        


if __name__ == '__main__':
    file_input = read_input('inputs/day9.txt')
    part1(file_input)