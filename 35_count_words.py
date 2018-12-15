"""Count words.
# Taken from Udacity
Implement a function count_words() in Python that takes as input a string s and a number n, and returns the n most \
frequently-occuring words in s. The return value should be a list of tuples - the top n words paired with their \
respective counts [(<word>, <count>), (<word>, <count>), ...], sorted in descending count order.

You can assume that all input will be in lowercase and that there will be no punctuations or other characters (only \
letters and single separating spaces). In case of a tie (equal count), order the tied words alphabetically.

E.g.:
print count_words("betty bought a bit of butter but the butter was bitter")
Output:
[('butter', 2), ('a', 1), ('betty', 1)]
"""
import operator


def count_words(s, n):
    """Return the n most frequently occuring words in s.

    Count the number of occurences of each word in s
    Sort the occurences in descending order (alphabetically in case of ties)
    Return the top n words as a list of tuples (<word>, <count>)
    """
    list_words_count = []
    list_words = s.split()
    for words in list_words:
        list_words_count.append((words, list_words.count(words)))
    list_words_distinct_count = list(set(list_words_count))
    # order of sorting is important
    s1 = sorted(list_words_distinct_count, key=operator.itemgetter(0))  # alphabetical
    s2 = sorted(s1, key=operator.itemgetter(1), reverse=True)           # descending order of occurence
    top_n = s2[0:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()