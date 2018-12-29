import itertools
import enchant

if __name__ == "__main__":
    """ Solver for spellathon 
    
    File name: 37_spellathon.py
    Author: Aneesh P.A.
    Date created: 23/12/2018
    Python Version: 3.5
    Puzzle appears in Times of India news paper. Prints out all valid words with more than 4 letters in the given
    set. All words should contain the alpha letter.
    """
    p_word = 'baseman'
    alpha_letter = 'm'
    p_word = str(input("Please enter puzzle_word: "))
    alpha_letter = str(input("Please enter alpha_letter: "))
    mother_set = set()
    # word should contain more that 3 letters
    for i in range(3, len(p_word)):
        words = ["".join(x) for x in itertools.permutations(p_word, i+1)]
        mother_set.update(words)
    my_dict = enchant.Dict("en_US")
    word_list = list()
    for w in mother_set:
        if my_dict.check(w):
            word_list.append(w)
    # remove items without alpha_letter
    final_list = list()
    for w in word_list:
        try:
            a = w.index(alpha_letter)
            final_list.append(w)
        except ValueError:
            # print("ValueError: ", w)
            pass
    # remove plurals
    for w in final_list:
        try:
            a = final_list.index(w + 's')
        except ValueError:
            pass
        else:                           # if exception not raised; => word+'s' exists in the list
            final_list.remove(w + 's')
    print(sorted(final_list))


