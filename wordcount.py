# put your code here.
import sys
from collections import Counter
import string
from operator import itemgetter

def word_count(filename):
    
    word_counts = {}

    with open(filename) as file_:
        for line in file_:
            words = line.split()
            for word in words:
                word = word.strip(",.\";:?_!").lower()
                word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.iteritems():
        print "{} {}".format(word, count)


def word_count_2(filename):

    with open(filename) as file_:
        words = file_.read().lower()
        words = words.translate(None, string.punctuation)
        word_counts = Counter(words.split())

    for word, count in word_counts.iteritems():
        print "{} {}".format(word, count)

    return word_counts


def sort_output_alpha(word_counts):
    for key, value in sorted(word_counts.items()):
        print "{} {}".format(key, value)


def sort_output_wc(word_counts):
    sorted_items = sorted(word_counts.items(), key=lambda item: item[1])

    for key, value in sorted_items:
        print "{} {}".format(value, key)


def sort_output_desc_asc(word_counts):
    sorted_items = sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))
    
    for key, value in sorted_items:
        print "{} {}".format(value, key)


