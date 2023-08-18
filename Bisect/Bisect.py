"""
The bisect module provides support for a list in sorted order using a bisection algorithm.

Feature set:
bisect.insort(list, elem), aka bisect.insort_right(list, elem) - inserts an element into a sorted list, while elem is
    located as far to the right as possible (all elements equal to it remain on the left).
bisect.insort_left(list, elem) - Insert an element into a sorted list, with elem positioned as far to the left as
    possible (all elements equal to it remain to the right).
bisect.bisect(list, elem), aka bisect.bisect_right(list, elem) - finds a place to insert an element into a sorted list,
    so that elem is located as far to the right as possible.
bisect.bisect_left(list, elem) - finds a place to insert an element in a sorted list, so that elem is located as far to
    the left as possible.
"""

import bisect
'''Searches for an element in a sorted list. It is in sorted.'''

file = open('C:/word.txt')
lis = []
for el in file:
    el = el.replace('\n', '')
    lis.append(el)
# Opens a file and turns it into a list, removing line breaks (there are many words in the file, each on a new line).


def search(my_list, word):
    """Takes a list and a word to be found.

     1. The variable index shows the place in the list, to the right of the search word (i.e. +1). This happens because
     bisect looks for the place where the given word must be placed in order to keep the list sorted.
     It takes a word, for example hello, looks for a place to put it, and the place turns out to be to the right of
     another word hello, which is already on the list. Those. he finds the word hello and offers to put another word
     hello to the right by 1.
     2. If it gets the index (where to put the word), and checks that the search word was in the previous place.
     3. If the word is in place, then the text is given, saying "your word was found, it is here ..."
     4. If there is no word (the index is another word, and not passed to the function), then it returns a different
        text.
     Why is there another word - because bisect just finds a place where you can put the word passed to it,
     he doesn't care if the word is in the list, he just looks for the right place.
     So it could happen that bisect has found a place for the given word hello, which will be immediately after hell."""

    index = bisect.bisect(my_list, word)
    if my_list[index - 1] == word:
        return f'Word {word} has index {index - 1}\n' \
               f'take a look yourself by executing:\n' \
               f'print(lis[{index - 1}])'
    else:
        return f'word {word} is missing'


print(search(lis, 'hello'))
print(lis[45100])
