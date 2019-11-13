import argparse

<<<<<<< Updated upstream
print("Hell i am here")
=======
>>>>>>> Stashed changes

book = open("book.txt", "r")

def freq(str):
    # break the string into list of words
    str_list = str.split()

    # gives set of unique words
    unique_words = set(str_list)

    for words in unique_words:
        print('Frequency of ', words, 'is :', str_list.count(words))

def count(args):
    str = book
    freq(str)

def cli():
    parser = argparse.ArgumentParser(prog="main")
    subparsers = parser.add_subparsers(help="Sub Command Help")

    #Add Subparsers
    subparsers.add_parser("count", help="Prints number times each word is written in the book.txt").\
        set_defaults(func=count)

    #Parse the command line
    args = parser.parse_args()

    #Take the func argument, which points to our function and call it
    args.func(args)
<<<<<<< Updated upstream


book.close()
=======
>>>>>>> Stashed changes
