import pprint
import collections


def words(filename):
    with open('book.txt', 'r') as file_:
        for line in file_:
            for word in line.split():
                yield word.lower()


counter = collections.Counter(words('/etc/services'))
sorted((key, value) for key, value in counter.items())

def sort(args):
    for value in counter.items() > 1000:



sorted_by_frequency =
sorted_by_frequency.reverse()
print('Sorted by frequency')
pprint.pprint(sorted_by_frequency)
