import re

from utils import read_input

def part12(sequences, end=True):

    extrapolations = 0

    for sequence in sequences:
        sequence = [int(i) for i in re.findall(r'-?\d+', sequence)]
        layers = [sequence]

        while not sum(i==0 for i in layers[-1]) == len(layers[-1]):
            differences = [layers[-1][i+1]-layers[-1][i] for i in range(len(layers[-1])-1)]
            layers.append(differences)
        layers[-1].append(0)

        for l in range(len(layers)-2, -1, -1):
            if end:
                new_digit = layers[l][-1] + layers[l+1][-1]
                layers[l].append(new_digit)
            else:
                new_digit = layers[l][0] - layers[l+1][0]
                layers[l] = [new_digit] + layers[l]
        extrapolations += new_digit


    print(extrapolations)

        


if __name__ == '__main__':
    file_input = read_input('inputs/day9.txt')
    part12(file_input)
    part12(file_input, end=False)