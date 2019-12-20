'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

# def vowel_count(string):
#     lower_s = string.lower()
#     return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


def vowel_count(string_):
    vocales = [char for char in string_ if char in 'aeiou']

    dictionary = {
        'a': vocales.count('a'),
        'e': vocales.count('e'),
        'i': vocales.count('i'),
        'o': vocales.count('o'),
        'u': vocales.count('u')}
    clean_dictionary = {x: y for x, y in dictionary.items() if y != 0}
    return print(clean_dictionary)


vowel_count('awesome')  # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie')  # {'e': 2, 'i': 1}
vowel_count('Colt')  # {'o': 1}
