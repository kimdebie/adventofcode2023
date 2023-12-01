from utils import read_input


def part1(lines):
    total_digits = sum(
        int(''.join([[c for c in line if c.isdigit()][i] for i in (0, -1)]))
        for line in lines
    )
    print(total_digits)


def part2(lines):
    replacements = {
        'one': 'on1e', 'two': 'tw2o', 'three': 'thre3e', 'four': 'fou4r',
        'five': 'fiv5e', 'six': 'si6x', 'seven': 'seve7n', 'eight': 'eigh8t',
        'nine': 'nin9e'
    }

    cleaned_lines = []
    for line in lines:
        for word, digit in replacements.items():
            line = line.replace(word, str(digit))
        cleaned_lines.append(line)

    part1(cleaned_lines)


if __name__ == '__main__':
    file_input = read_input('inputs/day1.txt')
    part1(file_input)
    part2(file_input)
