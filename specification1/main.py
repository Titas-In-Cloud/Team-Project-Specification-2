import re
import sys
import matplotlib.pyplot as plt
from collections import Counter


def analyse_frequency(input_file):
    bad_chars = re.compile(r"[^a-zA-Z ]")

    word_frequency = Counter()
    char_frequency = Counter()

    for line in input_file:
        filtered_line = bad_chars.sub("", line).lower()
        words = filtered_line.split()

        word_frequency.update(words)
        char_frequency.update(filtered_line)

    return char_frequency, word_frequency


def main():
    if len(sys.argv) < 3:
        print(f"usage: {sys.argv[0]} <input.txt> <output.csv>")
        return

    with open(sys.argv[1], "r", encoding="utf8") as input_file:
        char_frequency, word_frequency = analyse_frequency(input_file)

    with open(sys.argv[2], "w", encoding="utf8") as output_file:
        for word, frequency in word_frequency.most_common():
            output_file.write(f"{word},{frequency}\n")
    print(char_frequency)

    plt.ylabel('Number of occurrences')
    plt.xlabel('Characters (including space)')
    plt.title('Frequency of characters bar chart')
    plt.bar(*zip(*char_frequency.most_common()))
    plt.show()


if __name__ == "__main__":
    main()