import re


r'''
match - looks for a sequence at the beginning of a string
search - looks for the first match of the pattern
findall - Looks for all matches of a pattern. Returns the resulting strings as a list
finditer - Looks for all matches of a pattern. Returns an iterator
compile - compiles a regular expression. All of the above functions can then be applied to this object.
fullmatch - the entire string must match the described regular expression
sub - for replacement in strings
split - to split a string into parts

Called: re.match(a, b)

re - Library for working with regular expressions

. – any single character, except newline \n.
\ - character escape ('.' - looks for any character, '\.' - looks for a dot)
\d - matches any one digit and replaces the expression [0-9];
\D - excludes all digits and replaces [^0-9];
\w - replaces any number, letter, and underscore;
\W - any character except Latin, digits or underscore;
\s - matches any whitespace character;
\S describes any non-whitespace character;
\b - Beginning or end of a word (left is empty or non-letter, right is a letter and vice versa). Unlike the previous ones, matches a position, not a character
\B - Not a word boundary: either left and right are letters, or both left and right are NOT letters
[] - searches/replaces everything inside. Can accept the range [1-5A-Za-z] (that's 3 ranges, it's badly written)
* the letter ё is not included in the range a-z, it must be included separately
[^] - any character, except for the specified [^a] - except for a
() - grouping (either this or that)

Quantifiers:
{} - indicates the number of repetitions of the previous character {1}{2}{3}...
{1, 5} - 1 to 5 repetitions
{2,} - at least 2 repetitions
{,5} - no more than 5 repetitions
? – Zero or one occurrence, synonym for {0,1}
* – Zero or more, synonym for {0,}
+ - One or more, synonym for {1,}
$ - Looks for the end of a string. You need to put $ at the end of the expression (...$ - any 3 characters at the end of the line)
^ - Looks for the beginning of a line. You must put it at the beginning of the expression (^... - any 3 characters at the beginning of the line)



Examples:
\d{5} - any 5 digits
\d\d/\d\d/\d{4} – dates in dd/mm/yyyy format. Can be rewritten like this: \d{2}/\d{2}/\d{4}
.$ - any character at the end of the string
\.$ - dot at the end of the line
^\. - dot at the beginning of the line
[sw] - find all characters s and w, anywhere, in any order, at least together, at least one at a time
[^sw] - find all characters except s and w (all letters, numbers and spaces will be found one by one, except s, w)
^[^b] - find all lines that do not start with b
.*ing - words ending in ing
\s\w\w\w\s is a three-letter word (if there is a dot after the word, it will not be found). The output will contain words and spaces (' hell ')
\b\w\w\w\w\b is a 4 letter word, and fuck the dots and other punctuation. The output will only contain words ('hell')
\b\w{4}\b - similar, but with a quantifier
'''


def email_1():
    s = 'aasd@gmail.com'
    pattern = r'\w+@\w+\.\w+'
    print(re.findall(pattern, s))


email_1()


def any_4_letter_words():
    s = 'fucking. fucking hell! hell. HELL! 5555'
    pattern = r'\b\w\w\w\w\b'
    print(re.findall(pattern, s))


any_4_letter_words()


def any_email():
    s = 'hello1 hello22 hello333 asdasdasd@gmail.com hi@gmail.com'
    pattern = r'\w+@\w+[.][a-z]+'
    print(re.findall(pattern, s))


any_email()


def any_3_letters_words():
    """Any 5 numbers"""

    s = 'asd44444asdasd555555555577777888 asasdd asd dsa asdfasfjhsf fff'
    pattern = r'\b\w{3}\b'
    res = re.findall(pattern, s)
    print(res)


any_3_letters_words()


def replace():
    """Replacing an element in a string. Case-sensitive"""

    s = 'Hello, hello, Hello'
    s = re.sub('Hello', 'goodbye', s)
    print(s)


replace()


def list_of_letters():
    """Gets a list with all the letters. Ignores punctuation."""

    s = 'Hey, my name is Arkady'
    pattern = r'\w'
    res = re.findall(pattern, s)
    print(res)


list_of_letters()


def list_of_words():
    """Makes a list of words"""

    s = 'Hey, my name is Arkady'
    pattern = r'\w+'
    res = re.findall(pattern, s)
    print(res)


list_of_words()


def list_of_words_with_spaces():
    """List of words followed by a space"""

    s = 'Hey, my name is Arkady'
    pattern = r'\w+\s'
    res = re.findall(pattern, s)
    print(res)


list_of_words_with_spaces()


def long_pattern_search():
    s = 'Good afternoon, my name is Mr. Arkady A.A.'
    pattern = r'[A-Za-z]+\s'
    res = re.findall(pattern, s)
    print(res)


long_pattern_search()


def find_all_5_num():
    """Any 5 numbers"""

    s = 'asd44444asdasd555555555577777888'
    pattern = r'\d{5}'
    res = re.findall(pattern, s)
    print(res)


find_all_5_num()
