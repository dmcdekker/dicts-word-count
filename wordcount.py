# put your code here.
import sys

"""def word_count(filename):
    
    word_counts = {}

    with open(filename) as file_:
        for line in file_:
            words = line.rstrip().split(" ")
            for word in words:
                word = word.strip(",.\";:?_!").lower()
                word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.iteritems():
        print "{} {}".format(word, count)



word_count(sys.argv[1])
"""

from collections import Counter
import string

def word_count_2(filename):

    with open(filename) as file_:
        words = file_.read().lower().strip().replace("\n", " ")
        words = words.translate(None, string.punctuation)
        word_counts = Counter(words.split(" "))

    for word, count in word_counts.iteritems():
        print "{} {}".format(word, count)

word_count_2(sys.argv[1])


