# Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

# For example:

# # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})


def print_upper_words(words):
    '''Prints each word in a list in uppercase letters.'''
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    '''Prints each word in a list in uppercase letters if it starts with the letter 'e'.'''
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    '''Prints words in uppercase letters that start with given letters.'''

    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter.lower()):
                print(word.upper())
