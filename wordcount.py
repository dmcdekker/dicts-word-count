# put your code here.
import sys
from collections import Counter
import string
from operator import itemgetter

def word_count(filename):
    """Counts number of occurences of word in file"""
    
    word_counts = {}

    with open(filename) as file_:
        for line in file_:
            # strip white space
            words = line.split()
            # iterate over words and strip excess punctutation then add to dict
            for word in words:
                word = word.strip(",.\";:?_!").lower()
                word_counts[word] = word_counts.get(word, 0) + 1

    # print list of words and count
    for word, count in word_counts.iteritems():
        print "{} {}".format(word, count)


def word_count_2(filename):
    """Using collections.counter to count words"""

    with open(filename) as file_:
        # read file and lowercase all words
        words = file_.read().lower()
        # use translate to remove punc
        words = words.translate(None, string.punctuation)
        # call counter to count on split owrds
        word_counts = Counter(words.split())

    # print out items using iteritems (display, doesn't creat list) 
    for word, count in word_counts.iteritems():
        print "{} {}".format(word, count)

    return word_counts


def sort_output_alpha(word_counts):
    """Sort outout alpabetically"""

    for key, value in sorted(word_counts.items()):
        print "{} {}".format(key, value)


def sort_output_wc(word_counts):
    """Sort output by word count"""

    # use sorted to sort output by value (item[1] denotes second item)
    sorted_items = sorted(word_counts.items(), key=lambda item: item[1])

    for key, value in sorted_items:
        print "{} {}".format(value, key)


def sort_output_desc_asc(word_counts):
    """Sort output by descending key then ascending values"""

    # sort by item (-item[1] refers to reverse list of second item)
    sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    
    for key, value in sorted_items:
        print "{} {}".format(value, key)


